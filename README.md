# General-Purpose Development Templates

A comprehensive collection of structured prompt templates designed to guide development teams through any type of real-world project using LLM assistance. These templates break down large development initiatives into manageable epics and user stories with clear acceptance criteria, dependencies, and success metrics.

## 📋 Overview

This repository contains five comprehensive templates that cover the complete development lifecycle for any project type:

- **Project Management Template** - Complete project planning, execution, and delivery framework
- **General Backend Development Template** - Comprehensive backend API and service development
- **General Database Design Template** - Complete database architecture and schema design
- **General Frontend Development Template** - Modern frontend application development
- **Legacy Templates** - Original specialized templates (backend_template.md, database_template.md, frontend_template.md)

Each template is structured as a series of epics with detailed user stories, acceptance criteria, and clarification questions to ensure thorough planning and execution for any project domain.

## 🚀 Quick Start

1. **Choose your template** based on your development focus
2. **Review the epic structure** to understand the development phases
3. **Customize the stories** to match your specific project requirements
4. **Use clarification questions** to gather missing requirements
5. **Follow the dependencies** to ensure proper development order

## 📁 Template Structure

### Project Management Template (`project_management_template.md`)

**8 Epics covering 4 phases:**
- **Phase 0:** Project Discovery & Planning
- **Phase 1:** Foundation & Setup (Environment, Infrastructure)
- **Phase 2:** Core Development (Features, Integrations)
- **Phase 3:** Testing & Quality Assurance
- **Phase 4:** Deployment & Launch (Production, Support)

**Key Features:**
- Complete project lifecycle management
- Risk management and mitigation strategies
- Stakeholder communication and collaboration
- Quality gates and success metrics
- Deployment and handover procedures
- Adaptable to any project type or domain

### General Backend Development Template (`general_backend_template.md`)

**12 Epics covering 6 phases:**
- **Phase 0:** Project Setup & Architecture Planning
- **Phase 1:** Core API Foundation (Authentication, API Framework)
- **Phase 2:** Business Logic Implementation (Core Entities, Advanced Logic)
- **Phase 3:** Integration & External Services (APIs, AI/ML, WebSockets)
- **Phase 4:** Performance & Scalability (Optimization, Monitoring)
- **Phase 5:** Security & Compliance (Advanced Security, Testing)
- **Phase 6:** Deployment & Operations (CI/CD, Production Operations)

**Key Features:**
- Technology-agnostic backend development
- Complete authentication and authorization system
- RESTful API development with documentation
- External service integrations (payment, AI/ML, real-time)
- Performance optimization and caching strategies
- Security hardening and compliance
- Comprehensive testing and deployment pipeline

### General Database Design Template (`general_database_template.md`)

**12 Epics covering 6 phases:**
- **Phase 0:** Database Architecture Planning
- **Phase 1:** Core Entity Design (User Management, Business Entities)
- **Phase 2:** Advanced Features Schema (Content Management, Notifications)
- **Phase 3:** Analytics & Reporting Schema (Event Tracking, Search)
- **Phase 4:** Performance & Scalability (Optimization, Caching)
- **Phase 5:** Security & Compliance (Encryption, Audit Trails)
- **Phase 6:** Migration & Maintenance (Data Migration, Monitoring)

**Key Features:**
- Database technology-agnostic design
- Complete user management and RBAC system
- Business entity modeling with relationships
- File and media management schema
- Analytics and event tracking
- Performance optimization with indexing and partitioning
- Security compliance and audit trails
- Migration strategies and maintenance procedures

### General Frontend Development Template (`general_frontend_template.md`)

**10 Epics covering 5 phases:**
- **Phase 0:** Project Setup & Architecture Planning
- **Phase 1:** Core UI Foundation (Layout, Component Library)
- **Phase 2:** Business Logic & State Management (State Architecture, Forms)
- **Phase 3:** API Integration & Data Management (HTTP Client, Real-time)
- **Phase 4:** Performance & Production Readiness (Optimization, Testing)
- **Phase 5:** Deployment & Monitoring (CI/CD, Production Monitoring)

**Key Features:**
- Framework-agnostic frontend development
- Modern component library development
- Comprehensive state management
- API integration with caching and real-time features
- Performance optimization and code splitting
- Accessibility and SEO compliance
- Testing strategy (unit, integration, E2E)
- Production deployment and monitoring

### Legacy Templates (Original Specialized Versions)

- **`backend_template.md`** - Original backend template (QA through Voice specific)
- **`database_template.md`** - Original database template (QA through Voice specific)
- **`frontend_template.md`** - Original frontend template (QA through Voice specific)

## 🎯 How to Use These Templates

### 1. Project Planning Phase
- Start with the **Project Management Template** for overall project planning
- Review relevant technical templates (Backend, Database, Frontend)
- Identify which epics apply to your specific project needs
- Use clarification questions to gather missing requirements
- Estimate timelines based on team size and complexity

### 2. Development Phase
- Follow epic dependencies to ensure proper development order
- Use acceptance criteria as definition of done for each story
- Regularly review and update based on changing requirements
- Track progress against success metrics
- Coordinate between different templates for full-stack projects

### 3. Customization Guidelines
- **Project Type Adaptation:** Modify templates based on your project domain (web app, mobile, enterprise, etc.)
- **Technology Adaptation:** Adjust stories based on your chosen tech stack
- **Scale Consideration:** Modify complexity based on expected system scale
- **Team Expertise:** Consider team experience when estimating and planning
- **Business Domain:** Add domain-specific epics as needed
- **Compliance Needs:** Add additional security/compliance epics if required

### 4. Template Selection Guide
- **Full-Stack Projects:** Use Project Management + Backend + Database + Frontend templates
- **Backend-Only Projects:** Use Project Management + Backend + Database templates
- **Frontend-Only Projects:** Use Project Management + Frontend templates
- **Database-Heavy Projects:** Use Project Management + Database templates
- **Simple Projects:** Use Project Management template only

## 📊 Success Metrics

Each template includes comprehensive success metrics:

### Project Management Success Metrics
- **Delivery:** Project delivered on time and within budget
- **Quality:** All quality gates passed, minimal post-launch issues
- **User Satisfaction:** User acceptance criteria met, positive feedback
- **Technical:** Performance requirements met, security standards satisfied
- **Business:** Business objectives achieved, ROI targets met

### Backend Success Metrics
- **Performance:** API response time < 200ms for 95% of requests
- **Reliability:** 99.9% uptime SLA
- **Security:** Zero critical vulnerabilities, security audit passed
- **Scalability:** Handles expected peak load without degradation
- **Code Quality:** 85%+ test coverage, code review approval required

### Database Success Metrics
- **Performance:** Query response time < 100ms for 95% of queries
- **Reliability:** 99.9% database uptime
- **Scalability:** Handles expected data growth for 2+ years
- **Security:** Zero data breaches, encryption at rest and in transit
- **Compliance:** Meets all regulatory requirements

### Frontend Success Metrics
- **Performance:** First Contentful Paint < 1.5s, Largest Contentful Paint < 2.5s
- **Accessibility:** WCAG 2.1 AA compliance, keyboard navigation
- **Code Quality:** 90%+ test coverage, no critical security vulnerabilities
- **User Experience:** Task completion rate > 95%, user satisfaction > 4/5
- **SEO:** Good Lighthouse scores, proper meta tags and structured data

## 🔧 Best Practices

### General Guidelines
- Always validate requirements before starting development
- Use clarification questions to fill knowledge gaps
- Follow epic dependencies to avoid rework
- Regular code reviews and testing throughout development
- Document decisions and architectural choices
- Start with Project Management template for overall coordination

### Technology-Specific Guidelines
- **Project Management:** Focus on stakeholder communication and risk management
- **Backend:** Choose appropriate frameworks based on team expertise and project requirements
- **Database:** Design for 10x current requirements, plan for schema evolution
- **Frontend:** Prioritize accessibility and performance from the start

### Template Integration Guidelines
- Use Project Management template as the master coordination template
- Coordinate between technical templates for full-stack projects
- Ensure consistent naming conventions across all templates
- Align success metrics and acceptance criteria across templates

## 🤝 Contributing

These templates are designed to be living documents that evolve with best practices. If you have improvements or additional templates to contribute:

1. Fork the repository
2. Create your feature branch
3. Add your improvements with clear documentation
4. Submit a pull request with detailed description

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you have questions about using these templates or need help customizing them for your specific project:

1. Review the clarification questions in each template
2. Check the template usage guidelines
3. Open an issue for specific questions or suggestions

## 🔄 Version History

- **v2.0** - General-purpose templates for any project type
  - Added Project Management template for complete project lifecycle
  - Created general-purpose Backend, Database, and Frontend templates
  - Made templates technology and domain agnostic
  - Added comprehensive integration guidelines
  - Enhanced success metrics and best practices

- **v1.0** - Initial release with specialized templates
  - Backend, Database, and Frontend templates (QA through Voice specific)
  - Comprehensive epic breakdowns with detailed user stories
  - Success metrics and best practices included
  - Ready for immediate use in development projects

---

**Remember:** These templates are starting points designed to accelerate your development planning for any type of project. Always customize them based on your specific project requirements, team capabilities, and business constraints. The Project Management template should be your starting point for any new project!
