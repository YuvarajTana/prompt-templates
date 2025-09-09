# 🚀 TaskFlow AI - Development Setup Guide

This guide will help you set up and run TaskFlow AI locally. The project demonstrates how to implement the General Templates with a real-world AI-powered task management platform.

## 📋 Prerequisites

### Required Software
- **Python 3.11** (NOT 3.13 - compatibility issues with some packages)
- **Node.js 18+** and npm
- **Git** for version control

### Optional (for production)
- **PostgreSQL 14+** (we'll use SQLite for development)
- **Redis 6+** (for caching and background jobs)

## 🏗️ Project Structure

```
taskflow-ai/
├── backend/                 # FastAPI backend (Python)
├── frontend/                # Next.js frontend (TypeScript)
├── docs/                    # Documentation
├── scripts/                 # Development scripts
├── infrastructure/          # Infrastructure as code
├── README.md               # Project overview
├── TEMPLATE_MAPPING.md     # Template implementation mapping
└── DEVELOPMENT_GUIDE.md    # This file
```

## ⚙️ Backend Setup (FastAPI)

### 1. Navigate to Backend Directory
```bash
cd taskflow-ai/backend
```

### 2. Create Virtual Environment with Python 3.11
```bash
# Use Python 3.11 specifically (NOT 3.13)
python3.11 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Verify Python Version
```bash
python --version
# Should show: Python 3.11.x
```

### 4. Upgrade pip
```bash
pip install --upgrade pip
```

### 5. Install Dependencies
```bash
pip install -r requirements.txt
```

### 6. Set Up Environment Variables
```bash
# Copy the environment template
cp env.example .env

# The .env file is already configured for development with:
# - SQLite database (no PostgreSQL needed)
# - Development-friendly settings
# - Secure secret key for development
```

### 7. Create Database Tables
```bash
python -c "from app.db.database import create_tables; create_tables(); print('✅ Database tables created')"
```

### 8. Test Backend Import
```bash
python -c "import main; print('✅ Backend imports successfully')"
```

### 9. Run the Backend Server
```bash
# Start the development server
python main.py

# Or use uvicorn directly
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The backend will be available at:
- **API**: http://localhost:8000
- **Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## 🎨 Frontend Setup (Next.js)

### 1. Navigate to Frontend Directory
```bash
cd taskflow-ai/frontend
```

### 2. Install Dependencies
```bash
npm install
```

### 3. Set Up Environment Variables
```bash
# Create environment file
echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
```

### 4. Run the Frontend Development Server
```bash
npm run dev
```

The frontend will be available at:
- **Application**: http://localhost:3000

## 🧪 Testing the Setup

### Backend Tests
```bash
cd backend
source venv/bin/activate

# Test API health
curl http://localhost:8000/health

# Test API documentation
open http://localhost:8000/docs  # macOS
# or visit http://localhost:8000/docs in your browser
```

### Frontend Tests
```bash
cd frontend

# Run linting
npm run lint

# Run type checking
npm run type-check

# Test development server
npm run dev
# Visit http://localhost:3000
```

## 🔧 Development Workflow

### 1. Daily Development
```bash
# Terminal 1: Backend
cd taskflow-ai/backend
source venv/bin/activate
python main.py

# Terminal 2: Frontend  
cd taskflow-ai/frontend
npm run dev
```

### 2. Code Quality
```bash
# Backend formatting
cd backend
black .
isort .
flake8

# Frontend formatting
cd frontend
npm run lint:fix
npm run format
```

### 3. Database Operations
```bash
cd backend
source venv/bin/activate

# Reset database (development only)
python -c "from app.db.database import drop_tables, create_tables; drop_tables(); create_tables(); print('✅ Database reset')"

# Check database connection
python -c "from app.db.database import check_database_connection; print('✅ Connected' if check_database_connection() else '❌ Connection failed')"
```

## 🐛 Troubleshooting

### Python 3.13 Compatibility Issues
**Problem**: Installation fails with pydantic-core compilation errors
**Solution**: Use Python 3.11 instead of 3.13
```bash
# Remove existing venv
rm -rf venv

# Create new venv with Python 3.11
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Import Path Issues (Frontend)
**Problem**: Module not found errors for @/components/*
**Solution**: Ensure tsconfig.json has correct path mapping
```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  }
}
```

### Database Connection Issues
**Problem**: Database connection errors
**Solution**: Check if SQLite file is created and accessible
```bash
# Verify database file exists
ls -la taskflow.db

# Recreate if needed
python -c "from app.db.database import create_tables; create_tables()"
```

### Port Already in Use
**Problem**: Port 8000 or 3000 already in use
**Solution**: 
```bash
# Kill processes on port 8000
lsof -ti:8000 | xargs kill -9

# Kill processes on port 3000  
lsof -ti:3000 | xargs kill -9

# Or use different ports
uvicorn main:app --port 8001  # Backend
npm run dev -- --port 3001   # Frontend
```

## 📊 Template Implementation Status

This project demonstrates the following template implementations:

### ✅ Completed
- **Backend Epic 0**: Project setup with FastAPI
- **Backend Epic 1**: Authentication system with JWT
- **Database Epic 0-1**: User schema with SQLite
- **Frontend Epic 0**: Next.js setup with TypeScript
- **Frontend Epic 1**: Layout and navigation structure

### 🔄 In Progress
- **Backend Epic 2**: Core API framework
- **Backend Epic 3**: Business logic implementation
- **Frontend Epic 2**: Component library
- **Frontend Epic 3**: State management

### 📋 Planned
- **Backend Epic 4**: AI integration with OpenAI
- **Backend Epic 5**: External service integration
- **Frontend Epic 4**: Forms and data input
- **Frontend Epic 5**: API integration layer

## 🎯 Next Development Steps

1. **Complete Authentication UI** - Build login/register forms
2. **Implement Task Management** - CRUD operations for tasks
3. **Add AI Features** - OpenAI integration for task prioritization
4. **Build Team Features** - Collaboration and sharing
5. **Deploy to Production** - Cloud deployment setup

## 📚 Learning Resources

- [Template Mapping Guide](./TEMPLATE_MAPPING.md) - See how templates map to code
- [Template Implementation Guide](./docs/TEMPLATE_IMPLEMENTATION_GUIDE.md) - Step-by-step implementation
- [FastAPI Documentation](https://fastapi.tiangolo.com/) - Backend framework
- [Next.js Documentation](https://nextjs.org/docs) - Frontend framework
- [General Templates](../) - Original template files

## 🤝 Contributing

1. Follow the template guidelines
2. Write tests for new features
3. Update documentation
4. Use conventional commit messages
5. Create pull requests with clear descriptions

---

**Happy coding! 🚀** 

This project serves as both a functional application and a learning resource for implementing the General Templates in real-world projects.
