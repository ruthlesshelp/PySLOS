System design for the Python-based Student Loan Origination System (SLOS).

---

## 🧩 System Design Document  
**System Name**: PySLOS – Python Student Loan Origination System  
**Version**: 1.0  
**Date**: August 15, 2025  
**Author**: Stephen Ritchie

---

### 1. System Overview

#### 1.1 Purpose  
This document outlines the system architecture, components, data models, and design principles for PySLOS, a Python-based student loan origination platform.

#### 1.2 Scope  
Covers:
- Application architecture and layers
- Component interactions
- Data models and schema
- Design patterns
- Technology stack
- Security and performance

#### 1.3 System Context  
PySLOS is a web-based application for managing student loan applications, borrower profiles, and financial calculations.

---

### 2. System Architecture

#### 2.1 Architectural Pattern  
**Modular Layered Architecture** with separation of concerns:
- Presentation Layer (Flask Web UI)
- Service Layer (Business Logic)
- Data Access Layer (SQLAlchemy ORM)
- Financial Calculation Engine
- PostgreSQL Database

#### 2.2 Layer Descriptions

- **Presentation Layer**: Flask-based web interface for user interaction, input validation, and error handling.
- **Service Layer**: Implements domain logic, validation, and orchestration of operations.
- **Financial Layer**: Handles amortization calculations and interest rate conversions.
- **Data Access Layer**: SQLAlchemy ORM with repository pattern for CRUD operations.
- **Database Layer**: PostgreSQL with normalized schema and indexed relationships.

---

### 3. Component Design

#### 3.1 Core Components

- **Entities**:
  - `Individual`: Personal info
  - `Student`: High school info
  - `Application`: Loan terms

- **Repositories**:
  - `StudentRepository`
  - `ApplicationRepository`
  - `IndividualRepository`

- **Financial Engine**:
  - `LoanCalculator`: Computes monthly payments using amortization formula

#### 3.2 Design Patterns

- **Repository Pattern**: Abstracts data access logic
- **Factory Pattern**: Centralized instantiation of repositories
- **Domain Model Pattern**: Rich objects encapsulating business rules
- **Data Mapper Pattern**: SQLAlchemy ORM mappings

---

### 4. Data Architecture

#### 4.1 Schema Design

- **Individual Table**: Stores personal info
- **Student Table**: Extends Individual with school data
- **Application Table**: Stores loan details linked to Student

#### 4.2 Data Access Strategies

- **Session Management**: Scoped sessions per request
- **Transaction Handling**: Explicit boundaries with rollback on failure
- **Caching**: SQLAlchemy session-level caching; no L2 cache

---

### 5. Security Architecture

- **Authentication**: Role-based access via Flask-Login
- **Authorization**: Decorators for route protection
- **Input Validation**: Marshmallow schemas
- **SQL Injection Prevention**: ORM parameterization
- **Audit Logging**: Structured logs with user actions

---

### 6. Performance Architecture

- **Response Times**:
  - Application creation: < 2s
  - Payment calculation: < 100ms
  - Data retrieval: < 1s
  - DB operations: < 500ms

- **Optimization**:
  - Indexed foreign keys
  - Lazy loading
  - Connection pooling

---

### 7. Technology Stack

- **Language**: Python 3.11+
- **Frameworks**: Flask, SQLAlchemy, Marshmallow
- **Database**: PostgreSQL
- **Testing**: Pytest, FactoryBoy, Coverage.py
- **Deployment**: Docker, Gunicorn, Nginx

---

### 8. Deployment Architecture

- **App Deployment**: Docker container with Flask app
- **DB Deployment**: PostgreSQL container with volume persistence
- **Config Management**: `.env` files and config classes

---

### 9. Error Handling & Validation

- **Exception Hierarchy**:
  - `ValidationError`
  - `BusinessRuleError`
  - `DatabaseError`

- **Validation Framework**:
  - Input: Marshmallow
  - Business Rules: Custom validators

---

### 10. Testing Strategy

- **Unit Tests**: Domain logic and financial calculations
- **Integration Tests**: DB operations and API endpoints
- **Edge Cases**: Boundary conditions and invalid inputs

---

### 11. System Integration

- **Internal**: Flask routes → Service layer → Repositories
- **External**: REST API for integration with financial systems

---

### 12. Maintenance & Evolution

- **Extensibility Points**:
  - Add new loan types
  - Plug-in calculation modules
  - Support multi-user access

- **Technical Debt**:
  - Upgrade to async support
  - Add structured logging (e.g., Loguru)
  - Introduce role-based dashboards
