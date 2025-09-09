"""
TaskFlow AI - Configuration Management

Following Backend Template Epic 0: Project Setup & Architecture Planning
- Environment-based configuration
- Security settings
- Database configuration
- External service configuration
"""

from typing import List, Optional
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings with environment variable support"""
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True
    )
    
    # Application Settings
    PROJECT_NAME: str = "TaskFlow AI"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = Field(default="development", description="Environment: development, staging, production")
    DEBUG: bool = Field(default=True, description="Debug mode")
    
    # Security Settings
    SECRET_KEY: str = Field(..., description="Secret key for JWT tokens")
    ALGORITHM: str = Field(default="HS256", description="JWT algorithm")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30, description="Access token expiration time")
    REFRESH_TOKEN_EXPIRE_DAYS: int = Field(default=7, description="Refresh token expiration time")
    
    # CORS Settings
    ALLOWED_HOSTS: List[str] = Field(
        default=["http://localhost:3000", "http://127.0.0.1:3000"],
        description="Allowed CORS origins"
    )
    
    # Database Settings
    DATABASE_URL: str = Field(..., description="PostgreSQL database URL")
    DATABASE_POOL_SIZE: int = Field(default=20, description="Database connection pool size")
    DATABASE_MAX_OVERFLOW: int = Field(default=30, description="Database max overflow connections")
    
    # Redis Settings (for caching and background jobs)
    REDIS_URL: str = Field(default="redis://localhost:6379/0", description="Redis URL")
    
    # AI/ML Settings
    OPENAI_API_KEY: Optional[str] = Field(default=None, description="OpenAI API key")
    OPENAI_MODEL: str = Field(default="gpt-4", description="OpenAI model to use")
    OPENAI_MAX_TOKENS: int = Field(default=1000, description="Max tokens for OpenAI requests")
    
    # Email Settings (for notifications)
    SMTP_HOST: Optional[str] = Field(default=None, description="SMTP server host")
    SMTP_PORT: int = Field(default=587, description="SMTP server port")
    SMTP_USERNAME: Optional[str] = Field(default=None, description="SMTP username")
    SMTP_PASSWORD: Optional[str] = Field(default=None, description="SMTP password")
    SMTP_FROM_EMAIL: Optional[str] = Field(default=None, description="From email address")
    
    # File Storage Settings
    UPLOAD_DIR: str = Field(default="uploads", description="Local upload directory")
    MAX_FILE_SIZE: int = Field(default=10_000_000, description="Max file size in bytes (10MB)")
    ALLOWED_FILE_TYPES: List[str] = Field(
        default=["image/jpeg", "image/png", "image/gif", "application/pdf", "text/plain"],
        description="Allowed file MIME types"
    )
    
    # External API Settings
    RATE_LIMIT_PER_MINUTE: int = Field(default=100, description="API rate limit per minute")
    
    # Logging Settings
    LOG_LEVEL: str = Field(default="INFO", description="Logging level")
    LOG_FORMAT: str = Field(default="json", description="Log format: json or text")
    
    # Monitoring Settings
    SENTRY_DSN: Optional[str] = Field(default=None, description="Sentry DSN for error tracking")
    
    @property
    def is_development(self) -> bool:
        """Check if running in development mode"""
        return self.ENVIRONMENT.lower() == "development"
    
    @property
    def is_production(self) -> bool:
        """Check if running in production mode"""
        return self.ENVIRONMENT.lower() == "production"
    
    @property
    def database_url_async(self) -> str:
        """Get async database URL for SQLAlchemy"""
        if self.DATABASE_URL.startswith("postgresql://"):
            return self.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)
        elif self.DATABASE_URL.startswith("sqlite://"):
            return self.DATABASE_URL.replace("sqlite://", "sqlite+aiosqlite://", 1)
        return self.DATABASE_URL


# Global settings instance
settings = Settings()


# Configuration validation
def validate_config():
    """Validate critical configuration settings"""
    errors = []
    
    if not settings.SECRET_KEY or len(settings.SECRET_KEY) < 32:
        errors.append("SECRET_KEY must be at least 32 characters long")
    
    if not settings.DATABASE_URL:
        errors.append("DATABASE_URL is required")
    
    if settings.ENVIRONMENT.lower() == "production":
        if settings.DEBUG:
            errors.append("DEBUG must be False in production")
        
        if not settings.SENTRY_DSN:
            errors.append("SENTRY_DSN is recommended for production")
    
    if errors:
        raise ValueError(f"Configuration errors: {', '.join(errors)}")


# Validate configuration on import
try:
    validate_config()
except ValueError as e:
    print(f"⚠️  Configuration Warning: {e}")
    if settings.is_production:
        raise
