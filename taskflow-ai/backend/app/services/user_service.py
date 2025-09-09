"""
TaskFlow AI - User Service

Following Backend Template Epic 3: Core Business Entities
- User management business logic
- User CRUD operations
- Authentication and authorization logic
"""

from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlalchemy.orm import Session
import structlog

from app.core.security import verify_password, get_password_hash
from app.models.user import User, LoginAttempt
from app.schemas.auth import UserCreate, UserUpdate

logger = structlog.get_logger(__name__)


class UserService:
    """
    User service for business logic operations
    
    Following Backend Epic 3 - User Management
    """
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_user_by_id(self, user_id: UUID) -> Optional[User]:
        """Get user by ID"""
        return self.db.query(User).filter(User.id == user_id).first()
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        """Get user by email address"""
        return self.db.query(User).filter(User.email == email.lower()).first()
    
    def create_user(self, user_data: UserCreate) -> User:
        """
        Create a new user
        
        Following Epic 3 - User profile CRUD operations
        """
        # Hash the password
        hashed_password = get_password_hash(user_data.password)
        
        # Create user instance
        db_user = User(
            email=user_data.email.lower(),
            hashed_password=hashed_password,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            is_active=True,
            is_verified=False,  # Email verification required
        )
        
        # Save to database
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        
        logger.info("user_created", user_id=str(db_user.id), email=db_user.email)
        
        return db_user
    
    def update_user(self, user_id: UUID, user_data: UserUpdate) -> Optional[User]:
        """
        Update user profile
        
        Following Epic 3 - User profile CRUD operations
        """
        user = self.get_user_by_id(user_id)
        if not user:
            return None
        
        # Update fields
        update_data = user_data.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(user, field, value)
        
        user.updated_at = datetime.utcnow()
        
        self.db.commit()
        self.db.refresh(user)
        
        logger.info("user_updated", user_id=str(user.id))
        
        return user
    
    def authenticate_user(self, email: str, password: str) -> Optional[User]:
        """
        Authenticate user with email and password
        
        Following Epic 1 - User authentication system
        """
        # Log the login attempt
        self._log_login_attempt(email, success=False)  # Default to failed, update if successful
        
        user = self.get_user_by_email(email)
        if not user:
            logger.warning("authentication_failed_user_not_found", email=email)
            return None
        
        if not verify_password(password, user.hashed_password):
            logger.warning("authentication_failed_invalid_password", email=email)
            return None
        
        if not user.is_active:
            logger.warning("authentication_failed_inactive_user", email=email)
            return None
        
        # Update successful login attempt
        self._log_login_attempt(email, success=True)
        
        logger.info("user_authenticated", user_id=str(user.id), email=email)
        
        return user
    
    def update_last_login(self, user_id: UUID) -> None:
        """Update user's last login timestamp"""
        user = self.get_user_by_id(user_id)
        if user:
            user.last_login = datetime.utcnow()
            self.db.commit()
    
    def update_password(self, user_id: UUID, new_password: str) -> bool:
        """
        Update user password
        
        Following Epic 1 - Password reset functionality
        """
        user = self.get_user_by_id(user_id)
        if not user:
            return False
        
        # Hash new password
        hashed_password = get_password_hash(new_password)
        user.hashed_password = hashed_password
        user.updated_at = datetime.utcnow()
        
        self.db.commit()
        
        logger.info("password_updated", user_id=str(user.id))
        
        return True
    
    def verify_email(self, user_id: UUID) -> bool:
        """Mark user email as verified"""
        user = self.get_user_by_id(user_id)
        if not user:
            return False
        
        user.is_verified = True
        user.email_verified_at = datetime.utcnow()
        user.updated_at = datetime.utcnow()
        
        self.db.commit()
        
        logger.info("email_verified", user_id=str(user.id))
        
        return True
    
    def deactivate_user(self, user_id: UUID) -> bool:
        """
        Deactivate user account
        
        Following Epic 3 - Account deactivation
        """
        user = self.get_user_by_id(user_id)
        if not user:
            return False
        
        user.is_active = False
        user.updated_at = datetime.utcnow()
        
        self.db.commit()
        
        logger.info("user_deactivated", user_id=str(user.id))
        
        return True
    
    def delete_user(self, user_id: UUID) -> bool:
        """
        Delete user account (soft delete by deactivation)
        
        Following Epic 3 - Account deletion and data export
        """
        # In a real application, you might want to:
        # 1. Export user data first
        # 2. Anonymize data instead of deleting
        # 3. Handle related data (tasks, projects, etc.)
        
        return self.deactivate_user(user_id)
    
    def get_user_preferences(self, user_id: UUID) -> dict:
        """
        Get user preferences
        
        Following Epic 3 - User preferences and settings management
        """
        user = self.get_user_by_id(user_id)
        if not user:
            return {}
        
        return user.preferences or {}
    
    def update_user_preferences(self, user_id: UUID, preferences: dict) -> bool:
        """Update user preferences"""
        user = self.get_user_by_id(user_id)
        if not user:
            return False
        
        # Merge with existing preferences
        current_prefs = user.preferences or {}
        current_prefs.update(preferences)
        
        user.preferences = current_prefs
        user.updated_at = datetime.utcnow()
        
        self.db.commit()
        
        logger.info("user_preferences_updated", user_id=str(user.id))
        
        return True
    
    def _log_login_attempt(self, email: str, success: bool, ip_address: str = None, user_agent: str = None) -> None:
        """
        Log login attempt for security tracking
        
        Following Epic 1 - Login attempts and security logging
        """
        login_attempt = LoginAttempt(
            email=email.lower(),
            ip_address=ip_address,
            user_agent=user_agent,
            success=success,
            failure_reason=None if success else "authentication_failed"
        )
        
        self.db.add(login_attempt)
        try:
            self.db.commit()
        except Exception as e:
            logger.error("failed_to_log_login_attempt", error=str(e))
            self.db.rollback()
    
    def get_failed_login_attempts(self, email: str, hours: int = 1) -> int:
        """Get number of failed login attempts in the last N hours"""
        from datetime import timedelta
        
        cutoff_time = datetime.utcnow() - timedelta(hours=hours)
        
        count = (
            self.db.query(LoginAttempt)
            .filter(
                LoginAttempt.email == email.lower(),
                LoginAttempt.success == False,
                LoginAttempt.attempted_at >= cutoff_time
            )
            .count()
        )
        
        return count
    
    def is_account_locked(self, email: str, max_attempts: int = 5) -> bool:
        """Check if account is locked due to too many failed attempts"""
        failed_attempts = self.get_failed_login_attempts(email)
        return failed_attempts >= max_attempts
