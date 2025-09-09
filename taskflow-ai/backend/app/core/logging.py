"""
TaskFlow AI - Logging Configuration

Following Backend Template Epic 0: Project Setup & Architecture Planning
- Structured logging setup
- Environment-based log configuration
- Request/response logging
"""

import logging
import sys
from typing import Any, Dict

import structlog
from structlog.types import EventDict

from app.core.config import settings


def add_correlation_id(logger: Any, method_name: str, event_dict: EventDict) -> EventDict:
    """Add correlation ID to log entries"""
    # In a real application, you'd get this from request context
    # For now, we'll use a simple approach
    event_dict["correlation_id"] = getattr(logger, "_correlation_id", None)
    return event_dict


def add_service_info(logger: Any, method_name: str, event_dict: EventDict) -> EventDict:
    """Add service information to log entries"""
    event_dict["service"] = "taskflow-ai-api"
    event_dict["version"] = settings.VERSION
    event_dict["environment"] = settings.ENVIRONMENT
    return event_dict


def setup_logging():
    """Configure structured logging for the application"""
    
    # Configure standard library logging
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=getattr(logging, settings.LOG_LEVEL.upper()),
    )
    
    # Configure structlog
    processors = [
        structlog.contextvars.merge_contextvars,
        add_service_info,
        add_correlation_id,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.add_log_level,
        structlog.processors.StackInfoRenderer(),
        structlog.dev.set_exc_info,
    ]
    
    if settings.LOG_FORMAT.lower() == "json":
        # JSON logging for production
        processors.append(structlog.processors.JSONRenderer())
    else:
        # Pretty console logging for development
        processors.extend([
            structlog.dev.ConsoleRenderer(colors=True),
        ])
    
    structlog.configure(
        processors=processors,
        wrapper_class=structlog.make_filtering_bound_logger(
            getattr(logging, settings.LOG_LEVEL.upper())
        ),
        logger_factory=structlog.PrintLoggerFactory(),
        cache_logger_on_first_use=True,
    )


def get_logger(name: str = None) -> structlog.BoundLogger:
    """Get a configured logger instance"""
    if name:
        return structlog.get_logger(name)
    return structlog.get_logger()
