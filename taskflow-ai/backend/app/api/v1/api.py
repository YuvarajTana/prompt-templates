"""
TaskFlow AI - API Router Configuration

Following Backend Template Epic 2: Core API Framework
- API versioning strategy
- Route organization and structure
- Endpoint grouping by functionality
"""

from fastapi import APIRouter

from app.api.v1.endpoints import auth, tasks, projects, users, ai

# Main API router for version 1
api_router = APIRouter()

# Authentication endpoints
api_router.include_router(
    auth.router,
    prefix="/auth",
    tags=["authentication"]
)

# User management endpoints
api_router.include_router(
    users.router,
    prefix="/users",
    tags=["users"]
)

# Task management endpoints
api_router.include_router(
    tasks.router,
    prefix="/tasks",
    tags=["tasks"]
)

# Project management endpoints
api_router.include_router(
    projects.router,
    prefix="/projects",
    tags=["projects"]
)

# AI-powered features endpoints
api_router.include_router(
    ai.router,
    prefix="/ai",
    tags=["ai-features"]
)
