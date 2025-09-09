# 📚 Template Implementation Guide

This guide explains how TaskFlow AI implements each template from the parent directory, providing a step-by-step walkthrough for developers learning to use the templates.

## 🎯 **Purpose of This Guide**

- **For Template Users**: Learn how to apply templates to real projects
- **For Developers**: Understand the practical implementation of template concepts
- **For Teams**: See how templates coordinate across different aspects of development

---

## 🎨 **Frontend Template Implementation**

### **Template**: [`../general_frontend_template.md`](../general_frontend_template.md)

#### **Epic 0: Project Setup & Architecture Planning**

**Template Guidance**:
```markdown
- Initialize project with chosen framework (React/Vue/Angular/Svelte/Next.js/Nuxt.js)
- Set up development tools (ESLint, Prettier, Husky, lint-staged)
- Configure build tools (Vite/Webpack/Rollup)
```

**TaskFlow Implementation**:
```bash
# 1. Initialize Next.js project
npx create-next-app@latest taskflow-frontend --typescript --tailwind --app

# 2. Add development tools
npm install -D eslint prettier husky lint-staged @types/node

# 3. Configure package.json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "lint": "next lint",
    "format": "prettier --write ."
  },
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged"
    }
  }
}
```

**Key Files Created**:
- `frontend/package.json` - Project dependencies and scripts
- `frontend/next.config.js` - Next.js configuration
- `frontend/.eslintrc.json` - Linting rules
- `frontend/tailwind.config.js` - Styling configuration

#### **Epic 1: Layout & Navigation Systems**

**Template Guidance**:
```markdown
- Header/Navigation component with responsive design
- Footer component with links and information
- Sidebar (if applicable) with collapsible functionality
- Main content wrapper with proper spacing
```

**TaskFlow Implementation**:
```typescript
// frontend/src/components/layout/AppLayout.tsx
export function AppLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex h-screen bg-gray-50">
      <Sidebar />
      <div className="flex-1 flex flex-col">
        <Header />
        <main className="flex-1 overflow-auto p-6">
          {children}
        </main>
      </div>
    </div>
  )
}

// frontend/src/components/layout/Sidebar.tsx
export function Sidebar() {
  return (
    <aside className="w-64 bg-white shadow-sm">
      <nav className="p-4">
        <SidebarItem href="/dashboard" icon={HomeIcon}>
          Dashboard
        </SidebarItem>
        <SidebarItem href="/tasks" icon={TaskIcon}>
          Tasks
        </SidebarItem>
        <SidebarItem href="/projects" icon={ProjectIcon}>
          Projects
        </SidebarItem>
      </nav>
    </aside>
  )
}
```

#### **Epic 2: Component Library Development**

**Template Guidance**:
```markdown
- Button variants (primary, secondary, danger, ghost, etc.)
- Input fields (text, email, password, textarea, search)
- Form validation components with error states
- Loading states, spinners, and skeleton screens
```

**TaskFlow Implementation**:
```typescript
// frontend/src/components/ui/Button.tsx
interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'danger' | 'ghost'
  size?: 'sm' | 'md' | 'lg'
  loading?: boolean
  children: React.ReactNode
  onClick?: () => void
}

export function Button({ variant = 'primary', size = 'md', loading, children, onClick }: ButtonProps) {
  const baseClasses = 'font-medium rounded-lg transition-colors focus:outline-none focus:ring-2'
  const variantClasses = {
    primary: 'bg-blue-600 text-white hover:bg-blue-700 focus:ring-blue-500',
    secondary: 'bg-gray-200 text-gray-900 hover:bg-gray-300 focus:ring-gray-500',
    danger: 'bg-red-600 text-white hover:bg-red-700 focus:ring-red-500',
    ghost: 'text-gray-600 hover:bg-gray-100 focus:ring-gray-500'
  }
  const sizeClasses = {
    sm: 'px-3 py-1.5 text-sm',
    md: 'px-4 py-2 text-base',
    lg: 'px-6 py-3 text-lg'
  }

  return (
    <button
      className={`${baseClasses} ${variantClasses[variant]} ${sizeClasses[size]}`}
      onClick={onClick}
      disabled={loading}
    >
      {loading ? <Spinner /> : children}
    </button>
  )
}
```

---

## ⚙️ **Backend Template Implementation**

### **Template**: [`../general_backend_template.md`](../general_backend_template.md)

#### **Epic 0: Project Setup & Architecture Planning**

**Template Guidance**:
```markdown
- Initialize project with chosen framework (FastAPI/Django/Express/Spring/ASP.NET Core)
- Set up virtual environment and dependency management
- Configure development database and local services
```

**TaskFlow Implementation**:
```bash
# 1. Create Python virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Initialize FastAPI project
pip install fastapi uvicorn sqlalchemy alembic python-multipart

# 3. Create project structure
mkdir -p backend/app/{api,core,db,models,services,auth}
```

**Key Files Created**:
```python
# backend/main.py - Application entry point
from fastapi import FastAPI
from app.api.v1.api import api_router
from app.core.config import settings

app = FastAPI(
    title="TaskFlow AI API",
    description="Intelligent Task Management Platform API",
    version="1.0.0",
)

app.include_router(api_router, prefix="/api/v1")

# backend/app/core/config.py - Configuration management
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:pass@localhost/taskflow"
    SECRET_KEY: str = "your-secret-key"
    OPENAI_API_KEY: str = ""
    
    class Config:
        env_file = ".env"

settings = Settings()
```

#### **Epic 1: Authentication & Security Foundation**

**Template Guidance**:
```markdown
- User registration and login endpoints
- Password hashing and validation (bcrypt, Argon2)
- JWT/Session token management and refresh
- Password reset and email verification functionality
```

**TaskFlow Implementation**:
```python
# backend/app/auth/auth.py
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm="HS256")
    return encoded_jwt

# backend/app/api/v1/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/register")
async def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    # Check if user exists
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create new user
    hashed_password = get_password_hash(user_data.password)
    db_user = User(
        email=user_data.email,
        hashed_password=hashed_password,
        first_name=user_data.first_name,
        last_name=user_data.last_name
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return {"message": "User created successfully"}

@router.post("/token")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
```

---

## 🗄️ **Database Template Implementation**

### **Template**: [`../general_database_template.md`](../general_database_template.md)

#### **Epic 1: User & Authentication Schema**

**Template Guidance**:
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**TaskFlow Implementation**:
```python
# backend/app/models/user.py
from sqlalchemy import Column, String, Boolean, DateTime, UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    first_name = Column(String(100))
    last_name = Column(String(100))
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

# backend/alembic/versions/001_create_users_table.py
"""Create users table

Revision ID: 001
Revises: 
Create Date: 2024-01-15 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers
revision = '001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('users',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('hashed_password', sa.String(length=255), nullable=False),
        sa.Column('first_name', sa.String(length=100), nullable=True),
        sa.Column('last_name', sa.String(length=100), nullable=True),
        sa.Column('is_active', sa.Boolean(), nullable=True),
        sa.Column('is_verified', sa.Boolean(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)

def downgrade():
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
```

---

## 📊 **Project Management Template Implementation**

### **Template**: [`../project_management_template.md`](../project_management_template.md)

#### **Epic 0: Project Discovery & Planning**

**Template Guidance**:
```markdown
- Define project objectives and success criteria
- Identify key stakeholders and their roles
- Establish project boundaries and constraints
- Create project charter and initial requirements document
```

**TaskFlow Implementation**:

**Project Charter** (`docs/project_charter.md`):
```markdown
# TaskFlow AI Project Charter

## Project Objectives
- Create an AI-powered task management platform
- Achieve 10,000 active users within 12 months
- Generate $100K MRR through subscription model
- Demonstrate template implementation best practices

## Success Criteria
- 99.9% uptime SLA
- <200ms API response time
- 85% task completion rate
- 4.5+ user satisfaction rating

## Stakeholders
- Product Owner: Define requirements and priorities
- Tech Lead: Architecture and technical decisions
- Frontend Developer: UI/UX implementation
- Backend Developer: API and database development
- DevOps Engineer: Infrastructure and deployment
```

**Requirements Document** (`docs/requirements.md`):
- Functional requirements with acceptance criteria
- Non-functional requirements (performance, security)
- User personas and use cases
- Business requirements and constraints

---

## 🔄 **Cross-Template Integration**

### **How Templates Work Together**

#### **Frontend ↔ Backend Integration**
```typescript
// Frontend API service (Epic 5 - API Integration)
// frontend/src/services/api.ts
class TaskService {
  async createTask(taskData: CreateTaskRequest): Promise<Task> {
    const response = await fetch('/api/v1/tasks', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${getAuthToken()}`
      },
      body: JSON.stringify(taskData)
    })
    return response.json()
  }
}

// Backend API endpoint (Epic 3 - Core Business Entities)
// backend/app/api/v1/tasks.py
@router.post("/", response_model=TaskResponse)
async def create_task(
    task_data: TaskCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_task = Task(**task_data.dict(), user_id=current_user.id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
```

#### **Backend ↔ Database Integration**
```python
# Database model (Database Epic 2 - Core Business Schema)
class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    title = Column(String(255), nullable=False)
    description = Column(Text)
    priority = Column(Integer, default=2)
    status = Column(String(20), default="pending")
    
# Backend service (Backend Epic 3 - Core Business Entities)
class TaskService:
    def __init__(self, db: Session):
        self.db = db
    
    def create_task(self, task_data: TaskCreate, user_id: UUID) -> Task:
        db_task = Task(**task_data.dict(), user_id=user_id)
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task
```

---

## 🎯 **Implementation Best Practices**

### **1. Start with Templates**
- Read the complete template before starting
- Understand the epic flow and dependencies
- Adapt stories to your specific requirements

### **2. Follow Epic Sequence**
- Complete foundational epics first
- Don't skip setup and architecture phases
- Build incrementally with regular testing

### **3. Document Decisions**
- Record why you chose specific technologies
- Document deviations from template recommendations
- Keep architecture decisions updated

### **4. Test Early and Often**
- Implement testing from Epic 1
- Use test-driven development where appropriate
- Automate testing in CI/CD pipeline

### **5. Plan for Scale**
- Consider future requirements early
- Design for horizontal scaling
- Implement monitoring from the start

---

## 🚀 **Getting Started with Templates**

### **Step 1: Choose Your Templates**
1. Identify project type (web app, mobile app, API, etc.)
2. Select relevant templates from the parent directory
3. Read through all selected templates completely

### **Step 2: Plan Your Implementation**
1. Map template epics to your project needs
2. Estimate effort and create timeline
3. Set up project structure following templates

### **Step 3: Implement Incrementally**
1. Start with Epic 0 (setup) from each template
2. Work through epics in dependency order
3. Test and validate each epic completion

### **Step 4: Adapt and Evolve**
1. Customize templates for your specific needs
2. Document changes and rationale
3. Contribute improvements back to templates

---

This guide demonstrates that templates are not rigid frameworks but flexible blueprints that can be adapted to create successful real-world projects. Use TaskFlow AI as a reference implementation while building your own projects!
