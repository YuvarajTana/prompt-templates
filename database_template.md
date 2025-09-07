# Database Schema Design Template - Epic Breakdown

## Pre-Development Phase

### Epic 0: Database Architecture Planning
**Duration:** 1-2 weeks  
**Prerequisites:** Business requirements, data flow analysis, scalability requirements

#### Stories:
- **DB-001:** Database Technology Selection
  - Analyze data patterns (relational vs. document vs. graph)
  - Evaluate ACID vs. BASE requirements
  - Choose primary database (PostgreSQL/MySQL/MongoDB/etc.)
  - Plan for additional databases if needed (Redis, Elasticsearch)
  - **Acceptance Criteria:** Database technology stack approved and justified

- **DB-002:** Data Architecture Design
  - Define data domains and bounded contexts
  - Plan database separation strategy (single DB vs. multiple DBs)
  - Design data flow between services
  - Plan backup and disaster recovery strategy
  - **Acceptance Criteria:** High-level data architecture documented

- **DB-003:** Development Environment Setup
  - Set up local development databases
  - Configure database migration tools
  - Set up database version control strategy
  - Create development data seeding scripts
  - **Acceptance Criteria:** All developers can run database locally

**📋 Clarification Questions:**
- What's the expected data volume in 1-3 years?
- Do you need real-time analytics or just transactional data?
- Are there any compliance requirements (PCI, HIPAA, GDPR)?
- Do you need multi-region data distribution?
- What's the read-to-write ratio expectation?

---

## Phase 1: Core Entity Design

### Epic 1: User & Authentication Schema
**Duration:** 1-2 weeks  
**Dependencies:** Epic 0 complete

#### Stories:
- **DB-101:** User Management Schema
  - Users table with authentication fields
  - User profiles and extended attributes
  - User preferences and settings
  - Account status and lifecycle management
  - **Acceptance Criteria:** Complete user management data model

```sql
-- Example User Schema
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(100) UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    is_active BOOLEAN DEFAULT true,
    is_verified BOOLEAN DEFAULT false,
    last_login TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE user_profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    avatar_url VARCHAR(500),
    bio TEXT,
    phone VARCHAR(20),
    timezone VARCHAR(50) DEFAULT 'UTC',
    language VARCHAR(10) DEFAULT 'en',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

- **DB-102:** Role & Permission Schema
  - Roles table with hierarchical support
  - Permissions and capabilities
  - User-role assignments with context
  - Role inheritance and delegation
  - **Acceptance Criteria:** Flexible RBAC system implemented

```sql
-- Example RBAC Schema
CREATE TABLE roles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) UNIQUE NOT NULL,
    description TEXT,
    is_system BOOLEAN DEFAULT false,
    parent_role_id UUID REFERENCES roles(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE permissions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) UNIQUE NOT NULL,
    resource VARCHAR(100) NOT NULL,
    action VARCHAR(50) NOT NULL,
    description TEXT
);

CREATE TABLE user_roles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    role_id UUID REFERENCES roles(id) ON DELETE CASCADE,
    granted_by UUID REFERENCES users(id),
    context JSONB, -- For context-specific roles
    expires_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, role_id, context)
);
```

- **DB-103:** Session & Security Schema
  - User sessions and token management
  - Password reset and email verification
  - Login attempts and security logging
  - **Acceptance Criteria:** Comprehensive security tracking

### Epic 2: Core Business Entity Schema
**Duration:** 2-3 weeks  
**Dependencies:** Epic 1 complete

#### Stories:
- **DB-201:** Primary Business Entity Design
  - Main business object schema (products/posts/projects/etc.)
  - Entity relationships and hierarchies
  - Entity metadata and attributes
  - Entity lifecycle states
  - **Acceptance Criteria:** Core business data model complete

- **DB-202:** Entity Relationships & Associations
  - Many-to-many relationship tables
  - Hierarchical relationships (categories, tags)
  - Cross-entity references
  - Relationship metadata
  - **Acceptance Criteria:** All entity relationships properly modeled

- **DB-203:** Entity Versioning & History
  - Entity version tracking
  - Change history and audit trails
  - Soft delete implementation
  - **Acceptance Criteria:** Complete audit trail for business entities

**📋 Clarification Questions:**
- What are the core business entities in your domain?
- Do you need version control for business entities?
- What relationships exist between entities?
- Do you need soft deletes or hard deletes?
- What metadata needs to be tracked for each entity?

---

## Phase 2: Advanced Features Schema

### Epic 3: Content & Media Management
**Duration:** 2-3 weeks  
**Dependencies:** Epic 2 in progress

#### Stories:
- **DB-301:** File & Media Storage Schema
  - File metadata and storage references
  - Image/video processing status
  - File access permissions and sharing
  - File versioning and backups
  - **Acceptance Criteria:** Comprehensive file management system

```sql
-- Example File Management Schema
CREATE TABLE files (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    original_name VARCHAR(255) NOT NULL,
    stored_name VARCHAR(255) UNIQUE NOT NULL,
    file_path VARCHAR(1000) NOT NULL,
    file_size BIGINT NOT NULL,
    mime_type VARCHAR(100) NOT NULL,
    checksum VARCHAR(64),
    uploaded_by UUID REFERENCES users(id),
    storage_provider VARCHAR(50) DEFAULT 'local',
    is_public BOOLEAN DEFAULT false,
    expires_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE file_processing_jobs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    file_id UUID REFERENCES files(id) ON DELETE CASCADE,
    job_type VARCHAR(50) NOT NULL, -- resize, compress, analyze
    status VARCHAR(20) DEFAULT 'pending', -- pending, processing, completed, failed
    parameters JSONB,
    result JSONB,
    error_message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP
);
```

- **DB-302:** Content Management Schema
  - Rich content storage (HTML, Markdown)
  - Content templates and components
  - Content localization and translations
  - **Acceptance Criteria:** Flexible content management system

- **DB-303:** Tagging & Categorization
  - Hierarchical category system
  - Flexible tagging system
  - Entity-tag associations
  - **Acceptance Criteria:** Comprehensive content organization

### Epic 4: Communication & Notifications
**Duration:** 2-3 weeks  
**Dependencies:** Epic 3 in progress

#### Stories:
- **DB-401:** Notification System Schema
  - Notification templates and types
  - User notification preferences
  - Notification delivery tracking
  - **Acceptance Criteria:** Complete notification management

```sql
-- Example Notification Schema
CREATE TABLE notification_templates (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) UNIQUE NOT NULL,
    type VARCHAR(50) NOT NULL, -- email, push, in_app
    subject_template TEXT,
    body_template TEXT NOT NULL,
    variables JSONB, -- Available template variables
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE notifications (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    template_id UUID REFERENCES notification_templates(id),
    type VARCHAR(50) NOT NULL,
    title VARCHAR(255),
    message TEXT NOT NULL,
    data JSONB, -- Additional payload
    status VARCHAR(20) DEFAULT 'pending', -- pending, sent, failed, read
    sent_at TIMESTAMP,
    read_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

- **DB-402:** Messaging & Chat Schema (if needed)
  - Chat rooms/conversations
  - Message storage and threading
  - Message delivery status
  - **Acceptance Criteria:** Real-time messaging system support

- **DB-403:** Activity Feed & Timeline
  - User activity tracking
  - Feed generation and caching
  - Activity aggregation rules
  - **Acceptance Criteria:** Social activity feed system

**📋 Clarification Questions:**
- Do you need file processing capabilities (image resize, video transcode)?
- What notification channels are required (email, push, SMS)?
- Do you need real-time messaging/chat functionality?
- What activity tracking is needed for users?

---

## Phase 3: Analytics & Reporting Schema

### Epic 5: Analytics & Metrics Collection
**Duration:** 2-3 weeks  
**Dependencies:** Epic 4 in progress

#### Stories:
- **DB-501:** Event Tracking Schema
  - User behavior event logging
  - System performance metrics
  - Custom business metrics
  - **Acceptance Criteria:** Comprehensive analytics data collection

```sql
-- Example Analytics Schema
CREATE TABLE events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    session_id UUID,
    event_type VARCHAR(100) NOT NULL,
    event_name VARCHAR(100) NOT NULL,
    properties JSONB,
    user_agent TEXT,
    ip_address INET,
    referrer TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE user_sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    session_token VARCHAR(255) UNIQUE,
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ended_at TIMESTAMP,
    ip_address INET,
    user_agent TEXT,
    duration_seconds INTEGER
);
```

- **DB-502:** Reporting & Dashboard Schema
  - Pre-calculated report data
  - Dashboard configurations
  - Scheduled report definitions
  - **Acceptance Criteria:** Efficient reporting system support

- **DB-503:** A/B Testing & Feature Flags
  - Experiment definitions and configurations
  - User experiment assignments
  - Feature flag management
  - **Acceptance Criteria:** A/B testing and feature flag system

### Epic 6: Search & Discovery Schema
**Duration:** 1-2 weeks  
**Dependencies:** Epic 5 in progress

#### Stories:
- **DB-601:** Search Index Schema
  - Full-text search support
  - Search analytics and tracking
  - Search result ranking factors
  - **Acceptance Criteria:** Optimized search functionality

- **DB-602:** Recommendation System Schema
  - User preference tracking
  - Item similarity matrices
  - Recommendation caching
  - **Acceptance Criteria:** Recommendation engine data support

**📋 Clarification Questions:**
- What analytics and reporting requirements exist?
- Do you need real-time analytics or batch processing is fine?
- What search capabilities are required?
- Do you need recommendation system support?

---

## Phase 4: Performance & Scalability

### Epic 7: Database Optimization
**Duration:** 2-3 weeks  
**Dependencies:** Epic 6 complete

#### Stories:
- **DB-701:** Index Strategy Implementation
  - Query performance analysis
  - Strategic index creation
  - Composite index optimization
  - **Acceptance Criteria:** All critical queries perform under target thresholds

```sql
-- Example Index Strategies
-- For user lookup
CREATE INDEX idx_users_email_active ON users(email) WHERE is_active = true;

-- For time-based queries
CREATE INDEX idx_events_user_created ON events(user_id, created_at);

-- For search functionality
CREATE INDEX idx_content_search ON content USING gin(to_tsvector('english', title || ' ' || body));

-- For foreign key lookups
CREATE INDEX idx_user_roles_user_id ON user_roles(user_id);
CREATE INDEX idx_notifications_user_status ON notifications(user_id, status);
```

- **DB-702:** Partitioning Strategy
  - Table partitioning for large datasets
  - Time-based partitioning for logs/events
  - Hash partitioning for distributed data
  - **Acceptance Criteria:** Large tables are properly partitioned

- **DB-703:** Query Optimization
  - Slow query identification and optimization
  - Query plan analysis and improvement
  - Database statistics and maintenance
  - **Acceptance Criteria:** All queries meet performance SLA

### Epic 8: Caching & Data Access Patterns
**Duration:** 1-2 weeks  
**Dependencies:** Epic 7 in progress

#### Stories:
- **DB-801:** Caching Strategy Schema
  - Cache invalidation tracking
  - Cache warming strategies
  - Cache analytics and monitoring
  - **Acceptance Criteria:** Effective caching reduces database load

- **DB-802:** Read Replica Configuration
  - Read replica setup and routing
  - Data consistency strategies
  - Failover mechanisms
  - **Acceptance Criteria:** Read operations scaled across replicas

**📋 Clarification Questions:**
- What are the performance SLA requirements?
- Which queries/tables will have the highest load?
- Do you need database sharding capabilities?
- What caching strategies are preferred?

---

## Phase 5: Security & Compliance

### Epic 9: Data Security Implementation
**Duration:** 2-3 weeks  
**Dependencies:** Epic 8 complete

#### Stories:
- **DB-901:** Data Encryption Schema
  - Sensitive field encryption
  - Encryption key management
  - Data masking for non-production
  - **Acceptance Criteria:** Sensitive data is properly encrypted

- **DB-902:** Audit Trail & Compliance
  - Comprehensive audit logging
  - Data retention policies
  - Compliance reporting support
  - **Acceptance Criteria:** Full audit trail for compliance requirements

```sql
-- Example Audit Schema
CREATE TABLE audit_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    table_name VARCHAR(100) NOT NULL,
    record_id UUID NOT NULL,
    action VARCHAR(20) NOT NULL, -- INSERT, UPDATE, DELETE
    old_values JSONB,
    new_values JSONB,
    changed_by UUID REFERENCES users(id),
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ip_address INET,
    user_agent TEXT
);

-- Trigger function for audit logging
CREATE OR REPLACE FUNCTION audit_trigger_function()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'DELETE' THEN
        INSERT INTO audit_logs (table_name, record_id, action, old_values, changed_by, changed_at)
        VALUES (TG_TABLE_NAME, OLD.id, TG_OP, row_to_json(OLD), current_setting('app.current_user_id')::UUID, NOW());
    ELSIF TG_OP = 'UPDATE' THEN
        INSERT INTO audit_logs (table_name, record_id, action, old_values, new_values, changed_by, changed_at)
        VALUES (TG_TABLE_NAME, NEW.id, TG_OP, row_to_json(OLD), row_to_json(NEW), current_setting('app.current_user_id')::UUID, NOW());
    ELSIF TG_OP = 'INSERT' THEN
        INSERT INTO audit_logs (table_name, record_id, action, new_values, changed_by, changed_at)
        VALUES (TG_TABLE_NAME, NEW.id, TG_OP, row_to_json(NEW), current_setting('app.current_user_id')::UUID, NOW());
    END IF;
    RETURN COALESCE(NEW, OLD);
END;
$$ LANGUAGE plpgsql;
```

- **DB-903:** Data Privacy & GDPR Support
  - Personal data identification
  - Data anonymization capabilities
  - Right to be forgotten implementation
  - **Acceptance Criteria:** GDPR compliance features implemented

### Epic 10: Backup & Disaster Recovery
**Duration:** 1-2 weeks  
**Dependencies:** Epic 9 complete

#### Stories:
- **DB-1001:** Backup Strategy Implementation
  - Automated backup procedures
  - Point-in-time recovery setup
  - Backup validation and testing
  - **Acceptance Criteria:** Reliable backup and recovery system

- **DB-1002:** High Availability Setup
  - Database clustering configuration
  - Automatic failover mechanisms
  - Data synchronization monitoring
  - **Acceptance Criteria:** Database meets availability SLA

**📋 Clarification Questions:**
- What compliance standards need to be met?
- What's the required backup retention period?
- What are the RTO/RPO requirements?
- Do you need multi-region data replication?

---

## Phase 6: Migration & Maintenance

### Epic 11: Data Migration Strategy
**Duration:** 1-2 weeks  
**Dependencies:** Epic 10 complete

#### Stories:
- **DB-1101:** Migration Framework
  - Database version control system
  - Migration rollback procedures
  - Data validation after migrations
  - **Acceptance Criteria:** Safe, reliable database migrations

- **DB-1102:** Legacy Data Migration (if applicable)
  - Legacy system data extraction
  - Data transformation and cleaning
  - Migration validation and testing
  - **Acceptance Criteria:** Legacy data successfully migrated

### Epic 12: Monitoring & Maintenance
**Duration:** Ongoing  
**Dependencies:** Epic 11 complete

#### Stories:
- **DB-1201:** Database Monitoring
  - Performance monitoring dashboards
  - Alert configuration for issues
  - Capacity planning metrics
  - **Acceptance Criteria:** Proactive database monitoring in place

- **DB-1202:** Maintenance Procedures
  - Automated maintenance tasks
  - Database optimization schedules
  - Update and patching procedures
  - **Acceptance Criteria:** Database maintenance is automated and reliable

**📋 Clarification Questions:**
- Do you have legacy data that needs migration?
- What database monitoring tools are preferred?
- What's the maintenance window availability?
- Do you need automated database scaling?

---

## Success Metrics & Definition of Done

### Per Epic Success Criteria:
- ✅ Schema design reviewed and approved
- ✅ Performance benchmarks met
- ✅ Security requirements satisfied
- ✅ Data integrity constraints implemented
- ✅ Migration scripts tested
- ✅ Documentation updated

### Overall Database Success Metrics:
- **Performance:** Query response time < 100ms for 95% of queries
- **Reliability:** 99.9% database uptime
- **Scalability:** Handles expected data growth for 2+ years
- **Security:** Zero data breaches, encryption at rest and in transit
- **Compliance:** Meets all regulatory requirements

---

## Schema Design Best Practices

### Naming Conventions:
- **Tables:** Plural nouns (users, products, order_items)
- **Columns:** Snake_case (first_name, created_at, user_id)
- **Indexes:** idx_table_column(s) (idx_users_email, idx_orders_status_created)
- **Foreign Keys:** fk_table_referenced_table (fk_orders_users)

### Data Types Guidelines:
- **IDs:** UUID for distributed systems, BIGINT for single instance
- **Timestamps:** Always include created_at, updated_at
- **Strings:** VARCHAR with appropriate length limits
- **JSON:** JSONB in PostgreSQL for flexible schema
- **Money:** DECIMAL with fixed precision

### Relationship Guidelines:
- **Foreign Keys:** Always use foreign key constraints
- **Indexes:** Index all foreign keys and frequently queried columns
- **Cascading:** Be explicit about ON DELETE and ON UPDATE behavior
- **Normalization:** Aim for 3NF, denormalize only for performance

---

## Template Usage Guidelines

1. **Domain Adaptation:** Customize entities based on your business domain
2. **Scale Planning:** Design for 10x current requirements
3. **Technology Alignment:** Adapt constraints and features to chosen database
4. **Team Review:** Always have database design peer-reviewed
5. **Iterative Design:** Plan for schema evolution and migrations

**Remember:** Database schema is the foundation of your application. Invest time in getting it right early, as changes become more expensive over time!