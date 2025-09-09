"""
TaskFlow AI - Database Configuration

Following Database Template Epic 0: Database Architecture Planning
- Database connection management
- Session handling
- Connection pooling
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import StaticPool

from app.core.config import settings
import structlog

logger = structlog.get_logger(__name__)

# Create database engine
engine = create_engine(
    settings.DATABASE_URL,
    pool_size=settings.DATABASE_POOL_SIZE,
    max_overflow=settings.DATABASE_MAX_OVERFLOW,
    pool_pre_ping=True,  # Verify connections before use
    echo=settings.DEBUG,  # Log SQL queries in debug mode
)

# Create session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for all models
Base = declarative_base()


def get_db() -> Session:
    """
    Dependency to get database session
    
    Following Epic 0 - Database connection management
    """
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.error("database_session_error", error=str(e))
        db.rollback()
        raise
    finally:
        db.close()


def create_tables():
    """
    Create all database tables
    
    Following Epic 0 - Database setup
    """
    logger.info("creating_database_tables")
    Base.metadata.create_all(bind=engine)
    logger.info("database_tables_created")


def drop_tables():
    """
    Drop all database tables (for testing/development)
    """
    logger.warning("dropping_database_tables")
    Base.metadata.drop_all(bind=engine)
    logger.warning("database_tables_dropped")


# Database health check
def check_database_connection() -> bool:
    """
    Check if database connection is healthy
    """
    try:
        db = SessionLocal()
        db.execute("SELECT 1")
        db.close()
        return True
    except Exception as e:
        logger.error("database_connection_failed", error=str(e))
        return False
