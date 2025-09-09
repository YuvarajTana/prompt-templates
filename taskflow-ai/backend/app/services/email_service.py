"""
TaskFlow AI - Email Service

Placeholder email service for sending notifications
Following Backend Template Epic 4: Advanced Business Logic
"""

import structlog

logger = structlog.get_logger(__name__)


class EmailService:
    """
    Email service for sending notifications
    
    TODO: Implement actual email sending functionality
    """
    
    def __init__(self):
        self.enabled = False  # Disable by default for development
    
    async def send_verification_email(self, user, verification_token: str = None):
        """Send email verification email"""
        if not self.enabled:
            logger.info("email_verification_disabled", user_id=str(user.id), email=user.email)
            return
        
        # TODO: Implement actual email sending
        logger.info("send_verification_email", user_id=str(user.id), email=user.email)
    
    async def send_password_reset_email(self, user, reset_token: str):
        """Send password reset email"""
        if not self.enabled:
            logger.info("password_reset_email_disabled", user_id=str(user.id), email=user.email)
            return
        
        # TODO: Implement actual email sending
        logger.info("send_password_reset_email", user_id=str(user.id), email=user.email)
