PRD for Python-based Student Loan Origination System (SLOS).

---

## 📝 Product Requirements Document (PRD)
**Product Name**: PySLOS – Python Student Loan Origination System  
**Version**: 1.0  
**Date**: August 15, 2025  
**Author**: Stephen Ritchie

---

### 1. Executive Summary
PySLOS is a Python-based application designed to manage the origination of student loans. It enables loan officers, financial administrators, and system administrators to create, track, and validate student loan applications. The system emphasizes modularity, data integrity, and performance, and is built using Flask, SQLAlchemy, and PostgreSQL.

---

### 2. Product Overview

#### 2.1 Purpose
PySLOS streamlines student loan origination by offering:
- Student profile management
- Loan application lifecycle management
- Financial calculations (monthly payments, interest)
- Robust data validation and audit logging

#### 2.2 Target Users
- **Loan Officers**: Create and manage loan applications
- **Financial Administrators**: Validate loan parameters
- **System Administrators**: Configure and maintain system data

#### 2.3 Key Benefits
- Automated financial calculations
- Centralized data management
- Standardized workflows
- Audit trails and validation enforcement

---

### 3. Functional Requirements

#### 3.1 Student Management
- **Create Profile**: First name, last name, middle initial, suffix, DOB (must be in the past), high school info
- **Retrieve Profile**: Search by unique student ID
- **Update Profile**: Modify personal and school info
- **Delete Profile**: Soft delete with cascade options; prevent deletion if active applications exist

#### 3.2 Loan Application Management
- **Create Application**: Link to student, input principal, APR, term; auto-generate ID
- **Retrieve Application**: Search by ID; show full details and status
- **Update Application**: Modify terms and status; maintain audit trail
- **Delete Application**: Validate before deletion; preserve data integrity

#### 3.3 Financial Calculations
- **Monthly Payment**: Use amortization formula
- **Interest Rate Conversion**: APR → monthly rate (rounded to 6 decimals)

#### 3.4 Data Validation
- **Principal**: $1,000–$999,999.99
- **APR**: 0.01%–19.99%
- **Term**: 1–360 months
- **DOB**: Must be in the past; borrower ≥ 18 years old

---

### 4. Technical Requirements

#### 4.1 Architecture
- **Layers**: Flask (presentation), service layer (business logic), SQLAlchemy (data access), calculation engine
- **Frameworks**: Flask, SQLAlchemy, Marshmallow, Pytest
- **Database**: PostgreSQL
- **Language**: Python 3.11+

#### 4.2 Data Models
- **Individual**: Personal info
- **Student**: High school info, linked to Individual
- **Application**: Loan details, linked to Student

#### 4.3 Design Patterns
- Repository pattern for data access
- Factory pattern for service instantiation

---

### 5. Business Rules
- Borrower must be ≥ 18 years old
- Loan amount: $1,000–$999,999.99
- APR: 0.01%–19.99%
- Term: 1–360 months
- One student → many applications
- Unique constraints on IDs

---

### 6. User Stories

#### Loan Officer
- Create student application
- Modify existing application
- Calculate monthly payments

#### System Administrator
- Manage student data (CRUD)
- Maintain audit logs

#### Financial Administrator
- Validate loan parameters
- Enforce business rules

---

### 7. Non-Functional Requirements
- **Usability**: Web-based UI with clear prompts
- **Reliability**: 99.9% uptime; ACID compliance
- **Security**: Role-based access; SQL injection prevention
- **Maintainability**: Modular code; inline documentation
- **Scalability**: Support for 50+ concurrent users

---

### 8. Constraints & Assumptions
- PostgreSQL required
- Web deployment on Linux or Windows
- USD-only operations
- Users have basic computer literacy

---

### 9. Glossary
- **APR**: Annual Percentage Rate
- **Amortization**: Loan repayment over time
- **Principal**: Original loan amount
- **Term**: Loan duration in months
- **CRUD**: Create, Read, Update, Delete
- **ORM**: Object-Relational Mapping
