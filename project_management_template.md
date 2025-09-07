# General Project Management Template - Epic Breakdown

A comprehensive template for managing any type of real-world project using LLM assistance. This template provides a structured approach to project planning, execution, and delivery regardless of the project domain or technology stack.

## Pre-Project Phase

### Epic 0: Project Discovery & Planning
**Duration:** 1-3 weeks  
**Prerequisites:** Initial project idea or requirements, stakeholder identification

#### Stories:
- **PM-001:** Project Scope Definition
  - Define project objectives and success criteria
  - Identify key stakeholders and their roles
  - Establish project boundaries and constraints
  - Create project charter and initial requirements document
  - **Acceptance Criteria:** Clear project scope documented and approved by stakeholders

- **PM-002:** Requirements Analysis
  - Gather functional and non-functional requirements
  - Identify user personas and use cases
  - Document business rules and constraints
  - Prioritize requirements using MoSCoW or similar method
  - **Acceptance Criteria:** Complete requirements document with priorities

- **PM-003:** Technical Architecture Planning
  - Choose technology stack based on requirements
  - Design high-level system architecture
  - Identify integration points and external dependencies
  - Plan development environment and tools
  - **Acceptance Criteria:** Technical architecture approved, development environment ready

- **PM-004:** Project Planning & Estimation
  - Break down project into phases and milestones
  - Estimate effort for each component
  - Create project timeline and resource allocation
  - Identify risks and mitigation strategies
  - **Acceptance Criteria:** Project plan approved, team assigned, timeline established

**📋 Clarification Questions:**
- What is the primary business objective of this project?
- Who are the end users and what are their needs?
- What are the technical constraints and preferences?
- What is the budget and timeline constraints?
- What are the success metrics and KPIs?
- Are there any compliance or regulatory requirements?
- What is the expected project scale and complexity?

---

## Phase 1: Foundation & Setup

### Epic 1: Development Environment & Standards
**Duration:** 1-2 weeks  
**Dependencies:** Epic 0 complete

#### Stories:
- **PM-101:** Development Environment Setup
  - Set up development tools and IDEs
  - Configure version control and branching strategy
  - Set up project management tools (Jira, Trello, etc.)
  - Create development documentation standards
  - **Acceptance Criteria:** All team members can access and use development environment

- **PM-102:** Code Quality & Standards
  - Establish coding standards and conventions
  - Set up code review processes
  - Configure automated testing frameworks
  - Set up continuous integration pipeline
  - **Acceptance Criteria:** Code quality standards documented and automated

- **PM-103:** Project Documentation Framework
  - Create documentation templates and structure
  - Set up knowledge management system
  - Establish communication protocols
  - Create project status reporting templates
  - **Acceptance Criteria:** Documentation framework ready for use

### Epic 2: Core Infrastructure Setup
**Duration:** 2-3 weeks  
**Dependencies:** Epic 1 in progress

#### Stories:
- **PM-201:** Infrastructure Foundation
  - Set up hosting and deployment environments
  - Configure monitoring and logging systems
  - Set up backup and disaster recovery
  - Implement security baseline configurations
  - **Acceptance Criteria:** Infrastructure ready for development and testing

- **PM-202:** Data Management Setup
  - Design data architecture and storage strategy
  - Set up database and data management tools
  - Implement data backup and recovery procedures
  - Configure data security and access controls
  - **Acceptance Criteria:** Data management infrastructure operational

- **PM-203:** Integration & API Foundation
  - Design API architecture and standards
  - Set up API documentation and testing tools
  - Configure external service integrations
  - Implement API security and rate limiting
  - **Acceptance Criteria:** Integration framework ready for development

**📋 Clarification Questions:**
- What hosting and deployment options are preferred?
- What monitoring and alerting requirements exist?
- What are the data storage and backup requirements?
- What external services need integration?
- What are the security and compliance requirements?

---

## Phase 2: Core Development

### Epic 3: Core Feature Development
**Duration:** 4-6 weeks  
**Dependencies:** Epic 2 complete

#### Stories:
- **PM-301:** Primary Feature Implementation
  - Develop core business functionality
  - Implement user interface and user experience
  - Create data models and business logic
  - Build API endpoints and services
  - **Acceptance Criteria:** Core features functional and tested

- **PM-302:** User Management & Authentication
  - Implement user registration and authentication
  - Create user profiles and preferences
  - Set up role-based access control
  - Implement security measures and validation
  - **Acceptance Criteria:** User management system operational

- **PM-303:** Data Processing & Business Logic
  - Implement core business rules and workflows
  - Create data validation and processing logic
  - Build reporting and analytics capabilities
  - Implement error handling and recovery
  - **Acceptance Criteria:** Business logic implemented and validated

### Epic 4: Advanced Features & Integrations
**Duration:** 3-4 weeks  
**Dependencies:** Epic 3 in progress

#### Stories:
- **PM-401:** Advanced Functionality
  - Implement complex business workflows
  - Add advanced user interface features
  - Create automation and scheduling capabilities
  - Build notification and communication systems
  - **Acceptance Criteria:** Advanced features functional and user-tested

- **PM-402:** External Integrations
  - Integrate with third-party services and APIs
  - Implement data import/export functionality
  - Create webhook and event handling
  - Build real-time communication features
  - **Acceptance Criteria:** External integrations working reliably

- **PM-403:** Performance & Scalability
  - Optimize application performance
  - Implement caching strategies
  - Add load balancing and scaling capabilities
  - Optimize database queries and data access
  - **Acceptance Criteria:** Performance meets requirements under expected load

**📋 Clarification Questions:**
- What are the most critical features for initial release?
- What external services or APIs need integration?
- What are the performance and scalability requirements?
- What automation or workflow features are needed?
- What notification and communication features are required?

---

## Phase 3: Testing & Quality Assurance

### Epic 5: Comprehensive Testing
**Duration:** 2-3 weeks  
**Dependencies:** Epic 4 complete

#### Stories:
- **PM-501:** Automated Testing Implementation
  - Create unit test suites for all components
  - Implement integration testing
  - Set up end-to-end testing scenarios
  - Configure automated test execution
  - **Acceptance Criteria:** Comprehensive test coverage with automated execution

- **PM-502:** Manual Testing & Quality Assurance
  - Conduct user acceptance testing
  - Perform security testing and vulnerability assessment
  - Execute performance and load testing
  - Conduct usability testing and feedback collection
  - **Acceptance Criteria:** All testing phases completed with issues resolved

- **PM-503:** Bug Fixing & Optimization
  - Fix identified bugs and issues
  - Optimize performance based on test results
  - Improve user experience based on feedback
  - Implement security fixes and improvements
  - **Acceptance Criteria:** All critical issues resolved, performance optimized

### Epic 6: Documentation & Training
**Duration:** 1-2 weeks  
**Dependencies:** Epic 5 in progress

#### Stories:
- **PM-601:** Technical Documentation
  - Create comprehensive technical documentation
  - Document API specifications and usage
  - Create system architecture documentation
  - Write deployment and maintenance guides
  - **Acceptance Criteria:** Complete technical documentation available

- **PM-602:** User Documentation & Training
  - Create user manuals and help documentation
  - Develop training materials and tutorials
  - Create video demonstrations and guides
  - Set up user support and feedback systems
  - **Acceptance Criteria:** User documentation complete, training materials ready

**📋 Clarification Questions:**
- What level of test coverage is required?
- What types of testing are most critical for this project?
- Who will be using the system and what training do they need?
- What documentation is required for maintenance and support?
- What user support mechanisms are needed?

---

## Phase 4: Deployment & Launch

### Epic 7: Production Deployment
**Duration:** 1-2 weeks  
**Dependencies:** Epic 6 complete

#### Stories:
- **PM-701:** Production Environment Setup
  - Configure production infrastructure
  - Set up production monitoring and alerting
  - Implement production security measures
  - Configure backup and disaster recovery
  - **Acceptance Criteria:** Production environment ready and secure

- **PM-702:** Deployment Pipeline
  - Create automated deployment processes
  - Set up staging and production promotion
  - Implement rollback procedures
  - Configure deployment monitoring
  - **Acceptance Criteria:** Reliable deployment pipeline operational

- **PM-703:** Go-Live Preparation
  - Conduct final production testing
  - Prepare go-live checklist and procedures
  - Set up user communication and support
  - Create launch monitoring and response plan
  - **Acceptance Criteria:** Ready for production launch

### Epic 8: Launch & Post-Launch Support
**Duration:** 2-4 weeks  
**Dependencies:** Epic 7 complete

#### Stories:
- **PM-801:** Production Launch
  - Execute go-live procedures
  - Monitor system performance and stability
  - Provide immediate user support
  - Collect and address launch feedback
  - **Acceptance Criteria:** Successful production launch with stable operation

- **PM-802:** Post-Launch Monitoring & Support
  - Monitor system performance and user feedback
  - Address any post-launch issues
  - Provide user training and support
  - Collect metrics and performance data
  - **Acceptance Criteria:** System stable, users supported, metrics collected

- **PM-803:** Project Closure & Handover
  - Conduct project retrospective and lessons learned
  - Complete project documentation
  - Hand over to maintenance team
  - Create project closure report
  - **Acceptance Criteria:** Project successfully closed and handed over

**📋 Clarification Questions:**
- What is the preferred deployment strategy?
- What monitoring and alerting is needed post-launch?
- Who will provide ongoing support and maintenance?
- What metrics and KPIs need to be tracked?
- What is the handover process to the maintenance team?

---

## Success Metrics & Definition of Done

### Per Epic Success Criteria:
- ✅ All acceptance criteria met
- ✅ Stakeholder approval obtained
- ✅ Quality gates passed
- ✅ Documentation updated
- ✅ Team knowledge transfer completed
- ✅ Risk mitigation measures implemented

### Overall Project Success Metrics:
- **Delivery:** Project delivered on time and within budget
- **Quality:** All quality gates passed, minimal post-launch issues
- **User Satisfaction:** User acceptance criteria met, positive feedback
- **Technical:** Performance requirements met, security standards satisfied
- **Business:** Business objectives achieved, ROI targets met

---

## Template Usage Guidelines

### 1. Project Type Adaptation
- **Web Applications:** Focus on Epic 3-4 for core development
- **Mobile Apps:** Add mobile-specific epics for platform development
- **Data Projects:** Emphasize Epic 2 for data infrastructure
- **AI/ML Projects:** Add specialized epics for model development
- **Enterprise Systems:** Include additional compliance and integration epics

### 2. Team Size Considerations
- **Small Teams (1-3 people):** Combine epics, focus on core functionality
- **Medium Teams (4-8 people):** Follow template as structured
- **Large Teams (9+ people):** Break epics into smaller stories, add coordination epics

### 3. Technology Stack Adaptation
- **Modern Web Stack:** Focus on cloud-native, microservices architecture
- **Legacy Systems:** Add migration and modernization epics
- **Mobile-First:** Prioritize responsive design and mobile performance
- **Enterprise:** Include additional security, compliance, and integration epics

### 4. Industry-Specific Considerations
- **Healthcare:** Add HIPAA compliance and data privacy epics
- **Finance:** Include PCI compliance and financial regulations
- **E-commerce:** Add payment processing and inventory management
- **Education:** Include accessibility and learning management features

---

## Risk Management Framework

### Common Project Risks:
- **Technical Risks:** Technology choices, integration challenges, performance issues
- **Resource Risks:** Team availability, skill gaps, budget constraints
- **Timeline Risks:** Scope creep, dependency delays, external factors
- **Quality Risks:** Testing gaps, user acceptance issues, performance problems

### Risk Mitigation Strategies:
- **Early Identification:** Regular risk assessment and monitoring
- **Contingency Planning:** Backup plans for critical components
- **Stakeholder Communication:** Regular updates and expectation management
- **Quality Gates:** Multiple checkpoints and validation stages

---

## Communication & Collaboration

### Stakeholder Communication:
- **Project Sponsors:** Weekly status reports, milestone reviews
- **End Users:** Regular demos, feedback sessions, user testing
- **Development Team:** Daily standups, sprint reviews, retrospectives
- **Support Teams:** Knowledge transfer, documentation, training

### Documentation Standards:
- **Technical:** Architecture decisions, API documentation, deployment guides
- **User:** User manuals, help documentation, training materials
- **Project:** Status reports, lessons learned, handover documentation

---

**Remember:** This template is designed to be flexible and adaptable. Always customize it based on your specific project requirements, team capabilities, and organizational context. The key is to maintain the structured approach while adapting the details to your unique situation.
