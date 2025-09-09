"""
TaskFlow AI - Authentication Endpoints

Following Backend Template Epic 1: Authentication & Security Foundation
- User registration and login endpoints
- JWT token management and refresh
- Password reset functionality
"""

from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.security import (
    create_access_token,
    create_refresh_token,
    verify_password,
    get_password_hash,
    verify_token,
)
from app.db.database import get_db
from app.models.user import User
from app.schemas.auth import (
    UserCreate,
    UserLogin,
    Token,
    TokenRefresh,
    UserResponse,
    PasswordReset,
    PasswordResetConfirm,
)
from app.services.user_service import UserService
from app.services.email_service import EmailService
import structlog

logger = structlog.get_logger(__name__)
router = APIRouter()


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(
    user_data: UserCreate,
    db: Session = Depends(get_db),
) -> Any:
    """
    Register a new user
    
    Following Epic 1 - User Authentication System:
    - User registration with email validation
    - Password hashing and storage
    - Email verification (optional)
    """
    logger.info("user_registration_attempt", email=user_data.email)
    
    user_service = UserService(db)
    
    # Check if user already exists
    existing_user = user_service.get_user_by_email(user_data.email)
    if existing_user:
        logger.warning("registration_failed_user_exists", email=user_data.email)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )
    
    # Create new user
    try:
        user = user_service.create_user(user_data)
        logger.info("user_registration_success", user_id=str(user.id), email=user.email)
        
        # TODO: Send verification email
        # email_service = EmailService()
        # await email_service.send_verification_email(user)
        
        return UserResponse(
            id=user.id,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            is_active=user.is_active,
            is_verified=user.is_verified,
            created_at=user.created_at,
        )
        
    except Exception as e:
        logger.error("user_registration_failed", email=user_data.email, error=str(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create user account"
        )


@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
) -> Any:
    """
    User login with email and password
    
    Following Epic 1 - User Authentication System:
    - Email/password authentication
    - JWT token generation
    - Refresh token creation
    """
    logger.info("user_login_attempt", email=form_data.username)
    
    user_service = UserService(db)
    
    # Authenticate user
    user = user_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        logger.warning("login_failed_invalid_credentials", email=form_data.username)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    if not user.is_active:
        logger.warning("login_failed_inactive_user", email=form_data.username)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user account"
        )
    
    # Create tokens
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email, "user_id": str(user.id)},
        expires_delta=access_token_expires
    )
    
    refresh_token = create_refresh_token(
        data={"sub": user.email, "user_id": str(user.id)}
    )
    
    # Update last login
    user_service.update_last_login(user.id)
    
    logger.info("user_login_success", user_id=str(user.id), email=user.email)
    
    return Token(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="bearer",
        expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
    )


@router.post("/refresh", response_model=Token)
async def refresh_token(
    token_data: TokenRefresh,
    db: Session = Depends(get_db),
) -> Any:
    """
    Refresh access token using refresh token
    
    Following Epic 1 - JWT/Session token management and refresh
    """
    try:
        # Verify refresh token
        payload = verify_token(token_data.refresh_token)
        email = payload.get("sub")
        user_id = payload.get("user_id")
        
        if not email or not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token"
            )
        
        # Get user
        user_service = UserService(db)
        user = user_service.get_user_by_email(email)
        
        if not user or not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found or inactive"
            )
        
        # Create new tokens
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.email, "user_id": str(user.id)},
            expires_delta=access_token_expires
        )
        
        new_refresh_token = create_refresh_token(
            data={"sub": user.email, "user_id": str(user.id)}
        )
        
        logger.info("token_refresh_success", user_id=str(user.id))
        
        return Token(
            access_token=access_token,
            refresh_token=new_refresh_token,
            token_type="bearer",
            expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        )
        
    except Exception as e:
        logger.error("token_refresh_failed", error=str(e))
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token"
        )


@router.post("/forgot-password")
async def forgot_password(
    password_reset: PasswordReset,
    db: Session = Depends(get_db),
) -> Any:
    """
    Request password reset
    
    Following Epic 1 - Password reset functionality
    """
    logger.info("password_reset_request", email=password_reset.email)
    
    user_service = UserService(db)
    user = user_service.get_user_by_email(password_reset.email)
    
    if user:
        # Generate reset token
        reset_token = create_access_token(
            data={"sub": user.email, "type": "password_reset"},
            expires_delta=timedelta(hours=1)  # Reset token expires in 1 hour
        )
        
        # TODO: Send password reset email
        # email_service = EmailService()
        # await email_service.send_password_reset_email(user, reset_token)
        
        logger.info("password_reset_email_sent", email=password_reset.email)
    else:
        # Don't reveal if email exists or not for security
        logger.warning("password_reset_unknown_email", email=password_reset.email)
    
    return {"message": "If the email exists, a password reset link has been sent"}


@router.post("/reset-password")
async def reset_password(
    password_reset_confirm: PasswordResetConfirm,
    db: Session = Depends(get_db),
) -> Any:
    """
    Confirm password reset with token
    
    Following Epic 1 - Password reset functionality
    """
    try:
        # Verify reset token
        payload = verify_token(password_reset_confirm.token)
        email = payload.get("sub")
        token_type = payload.get("type")
        
        if not email or token_type != "password_reset":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid or expired reset token"
            )
        
        # Update user password
        user_service = UserService(db)
        user = user_service.get_user_by_email(email)
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        # Update password
        user_service.update_password(user.id, password_reset_confirm.new_password)
        
        logger.info("password_reset_success", user_id=str(user.id))
        
        return {"message": "Password has been reset successfully"}
        
    except Exception as e:
        logger.error("password_reset_failed", error=str(e))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or expired reset token"
        )
