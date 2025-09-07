# General Database Design Template - Epic Breakdown

A comprehensive template for database design that can be adapted for any type of project - from simple web applications to complex enterprise systems. This template provides a structured approach to designing robust, scalable, and maintainable database architectures.

## Pre-Development Phase

### Epic 0: Database Architecture Planning
**Duration:** 1-2 weeks  
**Prerequisites:** Business requirements, data flow analysis, scalability requirements

#### Stories:
- **DB-001:** Database Technology Selection
  - Analyze data patterns (relational vs. document vs. graph vs. time-series)
  - Evaluate ACID vs. BASE requirements
  - Choose primary database (PostgreSQL/MySQL/MongoDB/Cassandra/etc.)
  - Plan for additional databases if needed (Redis, Elasticsearch, InfluxDB)
  - **Acceptance Criteria:** Database technology stack approved and justified

- **DB-002:** Data Architecture Design
  - Define data domains and bounded contexts
  - Plan database separation strategy (single DB vs. multiple DBs vs. microservices)
  - Design data flow between services and systems
  - Plan backup, disaster recovery, and data retention strategy
  - **Acceptance Criteria:** High-level data architecture documented

- **DB-003:** Development Environment Setup
  - Set up local development databases
  - Configure database migration tools and version control
  - Set up database testing and seeding strategies
  - Create development data management procedures
  - **Acceptance Criteria:** All developers can run database locally

**📋 Clarification Questions:**
- What's the expected data volume in 1-3 years?
- Do you need real-time analytics or just transactional data?
- Are there any compliance requirements (PCI, HIPAA, GDPR)?
- Do you need multi-region data distribution?
- What's the read-to-write ratio expectation?
- What are the data consistency requirements?
- Do you need offline capabilities or always-online?

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
-- Example User Schema (PostgreSQL)
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
  - Main business object schema (products/posts/projects/orders/etc.)
  - Entity relationships and hierarchies
  - Entity metadata and attributes
  - Entity lifecycle states and transitions
  - **Acceptance Criteria:** Core business data model complete

- **DB-202:** Entity Relationships & Associations
  - Many-to-many relationship tables
  - Hierarchical relationships (categories, tags, taxonomies)
  - Cross-entity references and foreign keys
  - Relationship metadata and constraints
  - **Acceptance Criteria:** All entity relationships properly modeled

- **DB-203:** Entity Versioning & History
  - Entity version tracking and change history
  - Audit trails and change logs
  - Soft delete implementation
  - Data archival and retention policies
  - **Acceptance Criteria:** Complete audit trail for business entities

**📋 Clarification Questions:**
- What are the core business entities in your domain?
- Do you need version control for business entities?
- What relationships exist between entities?
- Do you need soft deletes or hard deletes?
- What metadata needs to be tracked for each entity?
- What are the data retention requirements?

---

## Phase 2: Advanced Features Schema

### Epic 3: Content & Media Management
**Duration:** 2-3 weeks  
**Dependencies:** Epic 2 in progress

#### Stories:
- **DB-301:** File & Media Storage Schema
  - File metadata and storage references
  - Image/video processing status and results
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
  - Rich content storage (HTML, Markdown, JSON)
  - Content templates and components
  - Content localization and translations
  - Content approval workflows
  - **Acceptance Criteria:** Flexible content management system

- **DB-303:** Tagging & Categorization
  - Hierarchical category system
  - Flexible tagging system with metadata
  - Entity-tag associations and relationships
  - Tag analytics and usage tracking
  - **Acceptance Criteria:** Comprehensive content organization

### Epic 4: Communication & Notifications
**Duration:** 2-3 weeks  
**Dependencies:** Epic 3 in progress

#### Stories:
- **DB-401:** Notification System Schema
  - Notification templates and types
  - User notification preferences
  - Notification delivery tracking
  - Notification analytics and metrics
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
  - Message delivery status and read receipts
  - Message search and filtering
  - **Acceptance Criteria:** Real-time messaging system support

- **DB-403:** Activity Feed & Timeline
  - User activity tracking and logging
  - Feed generation and caching strategies
  - Activity aggregation rules and algorithms
  - Social features and interactions
  - **Acceptance Criteria:** Social activity feed system

**📋 Clarification Questions:**
- Do you need file processing capabilities (image resize, video transcode)?
- What notification channels are required (email, push, SMS)?
- Do you need real-time messaging/chat functionality?
- What activity tracking is needed for users?
- Do you need content moderation or approval workflows?

---

## Phase 3: Analytics & Reporting Schema

### Epic 5: Analytics & Metrics Collection
**Duration:** 2-3 weeks  
**Dependencies:** Epic 4 in progress

#### Stories:
- **DB-501:** Event Tracking Schema
  - User behavior event logging
  - System performance metrics
  - Custom business metrics and KPIs
  - Event aggregation and rollup
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
  - Pre-calculated report data and aggregations
  - Dashboard configurations and layouts
  - Scheduled report definitions
  - Report sharing and permissions
  - **Acceptance Criteria:** Efficient reporting system support

- **DB-503:** A/B Testing & Feature Flags
  - Experiment definitions and configurations
  - User experiment assignments and tracking
  - Feature flag management and rollouts
  - Experiment results and analytics
  - **Acceptance Criteria:** A/B testing and feature flag system

### Epic 6: Search & Discovery Schema
**Duration:** 1-2 weeks  
**Dependencies:** Epic 5 in progress

#### Stories:
- **DB-601:** Search Index Schema
  - Full-text search support and indexing
  - Search analytics and tracking
  - Search result ranking factors
  - Search suggestions and autocomplete
  - **Acceptance Criteria:** Optimized search functionality

- **DB-602:** Recommendation System Schema
  - User preference tracking and modeling
  - Item similarity matrices and algorithms
  - Recommendation caching and performance
  - Recommendation feedback and learning
  - **Acceptance Criteria:** Recommendation engine data support

**📋 Clarification Questions:**
- What analytics and reporting requirements exist?
- Do you need real-time analytics or batch processing is fine?
- What search capabilities are required?
- Do you need recommendation system support?
- What A/B testing capabilities are needed?

---

## Phase 4: Performance & Scalability

### Epic 7: Database Optimization
**Duration:** 2-3 weeks  
**Dependencies:** Epic 6 complete

#### Stories:
- **DB-701:** Index Strategy Implementation
  - Query performance analysis and optimization
  - Strategic index creation and maintenance
  - Composite index optimization
  - Index monitoring and tuning
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
  - Partition maintenance and management
  - **Acceptance Criteria:** Large tables are properly partitioned

- **DB-703:** Query Optimization
  - Slow query identification and optimization
  - Query plan analysis and improvement
  - Database statistics and maintenance
  - Query caching and optimization
  - **Acceptance Criteria:** All queries meet performance SLA

### Epic 8: Caching & Data Access Patterns
**Duration:** 1-2 weeks  
**Dependencies:** Epic 7 in progress

#### Stories:
- **DB-801:** Caching Strategy Schema
  - Cache invalidation tracking and management
  - Cache warming strategies and procedures
  - Cache analytics and monitoring
  - Cache consistency and synchronization
  - **Acceptance Criteria:** Effective caching reduces database load

- **DB-802:** Read Replica Configuration
  - Read replica setup and routing
  - Data consistency strategies
  - Failover mechanisms and monitoring
  - Load balancing and distribution
  - **Acceptance Criteria:** Read operations scaled across replicas

**📋 Clarification Questions:**
- What are the performance SLA requirements?
- Which queries/tables will have the highest load?
- Do you need database sharding capabilities?
- What caching strategies are preferred?
- What are the consistency requirements?

---

## Phase 5: Security & Compliance

### Epic 9: Data Security Implementation
**Duration:** 2-3 weeks  
**Dependencies:** Epic 8 complete

#### Stories:
- **DB-901:** Data Encryption Schema
  - Sensitive field encryption and key management
  - Encryption key rotation and management
  - Data masking for non-production environments
  - Encryption performance optimization
  - **Acceptance Criteria:** Sensitive data is properly encrypted

- **DB-902:** Audit Trail & Compliance
  - Comprehensive audit logging and tracking
  - Data retention policies and enforcement
  - Compliance reporting support
  - Audit log analysis and monitoring
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
  - Personal data identification and classification
  - Data anonymization capabilities
  - Right to be forgotten implementation
  - Data portability and export
  - **Acceptance Criteria:** GDPR compliance features implemented

### Epic 10: Backup & Disaster Recovery
**Duration:** 1-2 weeks  
**Dependencies:** Epic 9 complete

#### Stories:
- **DB-1001:** Backup Strategy Implementation
  - Automated backup procedures and scheduling
  - Point-in-time recovery setup
  - Backup validation and testing
  - Cross-region backup replication
  - **Acceptance Criteria:** Reliable backup and recovery system

- **DB-1002:** High Availability Setup
  - Database clustering configuration
  - Automatic failover mechanisms
  - Data synchronization monitoring
  - Health checks and monitoring
  - **Acceptance Criteria:** Database meets availability SLA

**📋 Clarification Questions:**
- What compliance standards need to be met?
- What's the required backup retention period?
- What are the RTO/RPO requirements?
- Do you need multi-region data replication?
- What are the data privacy requirements?

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
  - Migration testing and validation
  - **Acceptance Criteria:** Safe, reliable database migrations

- **DB-1102:** Legacy Data Migration (if applicable)
  - Legacy system data extraction
  - Data transformation and cleaning
  - Migration validation and testing
  - Data quality assurance
  - **Acceptance Criteria:** Legacy data successfully migrated

### Epic 12: Monitoring & Maintenance
**Duration:** Ongoing  
**Dependencies:** Epic 11 complete

#### Stories:
- **DB-1201:** Database Monitoring
  - Performance monitoring dashboards
  - Alert configuration for issues
  - Capacity planning metrics
  - Database health monitoring
  - **Acceptance Criteria:** Proactive database monitoring in place

- **DB-1202:** Maintenance Procedures
  - Automated maintenance tasks
  - Database optimization schedules
  - Update and patching procedures
  - Performance tuning and optimization
  - **Acceptance Criteria:** Database maintenance is automated and reliable

**📋 Clarification Questions:**
- Do you have legacy data that needs migration?
- What database monitoring tools are preferred?
- What's the maintenance window availability?
- Do you need automated database scaling?
- What are the ongoing maintenance requirements?

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
- **Maintainability:** Clear schema documentation, automated migrations

---

## Schema Design Best Practices

### Naming Conventions:
- **Tables:** Plural nouns (users, products, order_items)
- **Columns:** Snake_case (first_name, created_at, user_id)
- **Indexes:** idx_table_column(s) (idx_users_email, idx_orders_status_created)
- **Foreign Keys:** fk_table_referenced_table (fk_orders_users)
- **Constraints:** ck_table_column (ck_users_email_format)

### Data Types Guidelines:
- **IDs:** UUID for distributed systems, BIGINT for single instance
- **Timestamps:** Always include created_at, updated_at
- **Strings:** VARCHAR with appropriate length limits
- **JSON:** JSONB in PostgreSQL for flexible schema
- **Money:** DECIMAL with fixed precision
- **Booleans:** Use BOOLEAN, avoid 0/1 or 'Y'/'N'

### Relationship Guidelines:
- **Foreign Keys:** Always use foreign key constraints
- **Indexes:** Index all foreign keys and frequently queried columns
- **Cascading:** Be explicit about ON DELETE and ON UPDATE behavior
- **Normalization:** Aim for 3NF, denormalize only for performance
- **Constraints:** Use check constraints for data validation

---

## Template Usage Guidelines

### 1. Database Technology Adaptation
- **PostgreSQL:** Use advanced features like JSONB, arrays, custom types
- **MySQL:** Focus on InnoDB engine, consider partitioning
- **MongoDB:** Design for document structure and embedded data
- **Cassandra:** Plan for wide-column design and eventual consistency
- **Redis:** Use for caching, sessions, and real-time data

### 2. Scale Planning
- **Small Scale:** Single database, basic indexing
- **Medium Scale:** Read replicas, query optimization
- **Large Scale:** Sharding, partitioning, distributed architecture
- **Enterprise:** Multi-region, disaster recovery, compliance

### 3. Domain-Specific Considerations
- **E-commerce:** Orders, inventory, payments, customer data
- **Healthcare:** Patient data, HIPAA compliance, audit trails
- **Finance:** Transactions, compliance, fraud detection
- **Education:** Learning management, content, assessments
- **Social:** User relationships, content, activity feeds

### 4. Team Review Process
- **Architecture Review:** High-level design and technology choices
- **Schema Review:** Table design and relationships
- **Performance Review:** Indexing and query optimization
- **Security Review:** Data protection and access controls
- **Compliance Review:** Regulatory requirements and audit trails

---

## Integration Points

### Backend Integration:
- Schema design should align with API requirements
- Performance optimization coordinates with backend caching
- Security measures integrate with authentication system

### Frontend Integration:
- Data structure should support UI requirements
- Search functionality aligns with frontend search features
- Real-time features coordinate with WebSocket implementation

### DevOps Integration:
- Backup strategies align with infrastructure requirements
- Monitoring integrates with application monitoring
- Migration procedures coordinate with deployment pipeline

---

**Remember:** Database schema is the foundation of your application. Invest time in getting it right early, as changes become more expensive over time. Always design for your expected scale and consider future growth!
