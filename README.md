# PySLOS - Python Student Loan Origination System

## 🎯 Educational Project Overview

PySLOS is a **documentation-complete, implementation-ready** educational project designed to teach software development best practices through a real-world financial services application. This project demonstrates how to design a complete system *before* writing any code.

**Learning Objective**: Understand how comprehensive planning, architecture design, and test planning set the foundation for successful software development.

## 🏗️ What Is This Project?

This is a **Student Loan Origination System** - software that banks and financial institutions use to:
- Manage student borrower profiles
- Process loan applications 
- Calculate monthly payments and interest
- Validate loan terms and borrower eligibility

**Key Learning Point**: This project shows how complex business software is architected using **layered design patterns** that separate concerns and make code maintainable.

## 📚 Project Structure for Learning

This project is organized to demonstrate professional software development practices:

```
PySLOS/
├── docs/                           # Complete technical documentation
│   ├── PRD.md                     # Product Requirements (what to build)
│   ├── SYSTEM_DESIGN.md           # Architecture (how to build it) 
│   └── TEST_PLAN.md               # Testing Strategy (how to verify it works)
├── .github/
│   └── copilot-instructions.md    # AI coding assistant guidance
└── README.md                      # This introduction
```

### 🔍 Understanding Each Document

**📋 PRD.md (Product Requirements Document)**
- Defines the business problem and user needs
- Specifies exactly what features the system must have
- Contains business rules (loan limits, age requirements, etc.)
- **Learning Value**: See how business requirements translate to technical specifications

**🏛️ SYSTEM_DESIGN.md (System Architecture)**  
- Describes the **Modular Layered Architecture** pattern
- Explains how different parts of the system interact
- Defines data models and relationships
- **Learning Value**: Understand how complex systems are broken down into manageable components

**✅ TEST_PLAN.md (Testing Strategy)**
- Outlines Test-Driven Development (TDD) approach
- Specifies what types of tests to write and when
- Defines coverage goals and testing patterns
- **Learning Value**: Learn how testing drives better code design

**🤖 .github/copilot-instructions.md (AI Assistant Guide)**
- Provides context for AI coding assistants like GitHub Copilot
- Contains project-specific patterns and conventions
- **Learning Value**: See how to guide AI tools for better code generation

## 🏗️ System Architecture Overview

PySLOS uses a **Modular Layered Architecture** - a professional pattern that separates different responsibilities:

```
┌─────────────────────────────────────┐
│  Presentation Layer (Flask Web UI)  │  ← User Interface
├─────────────────────────────────────┤
│  Service Layer (Business Logic)     │  ← Domain Rules & Validation  
├─────────────────────────────────────┤
│  Financial Engine (Calculations)    │  ← Loan Math & Amortization
├─────────────────────────────────────┤
│  Data Access Layer (Repository)     │  ← Database Operations
├─────────────────────────────────────┤
│  Database Layer (SQLite).           │  ← Data Storage
└─────────────────────────────────────┘
```

**Why This Matters**: Each layer has a single responsibility, making the code:
- Easier to test (you can test business logic without a database)
- Easier to maintain (changes in one layer don't break others)
- Easier to understand (each layer has a clear purpose)

## 💰 Business Domain: Financial Services

This project teaches software development through a **financial services lens**:

### Core Business Entities
- **Individual**: Person's basic information (name, date of birth)
- **Student**: Individual + high school information  
- **Application**: Loan request (amount, interest rate, term length)

### Business Rules Examples
- Borrower must be 18+ years old
- Loan amount: $1,000 to $999,999.99
- Interest rates: 0.01% to 19.99% APR
- Loan terms: 1 to 360 months

**Learning Value**: See how business requirements become validation rules in code.

## 🛠️ Technology Stack

When implemented, this system will use:

- **Python 3.11+**: Modern language features
- **Flask**: Web framework for user interface
- **SQLAlchemy**: Database ORM with Repository pattern  
- **SQLite**: Relational database
- **pytest**: Test framework with 100% coverage goal
- **Marshmallow**: Data validation and serialization

**Design Patterns Used**:
- **Repository Pattern**: Clean data access
- **Factory Pattern**: Object creation
- **Domain Model Pattern**: Rich business objects

## 🧪 Test-Driven Development (TDD) Approach

This project emphasizes **TDD** - writing tests before implementation:

1. **Red**: Write a failing test that describes desired behavior
2. **Green**: Write minimal code to make the test pass  
3. **Refactor**: Improve code while keeping tests green

**Expected Test Organization**:
```
tests/
├── test_entities.py      # Domain model tests
├── test_repositories.py  # Data access tests
├── test_financial.py     # Loan calculation tests
└── test_services.py      # Business logic tests
```

## 🎓 Learning Outcomes

After studying this project, you should understand:

1. **Requirements Analysis**: How business needs become technical specifications
2. **System Architecture**: How to design maintainable, testable software  
3. **Domain Modeling**: How to represent business concepts in code
4. **Test Strategy**: How comprehensive testing drives better design
5. **Documentation**: How proper documentation enables team collaboration
6. **AI Integration**: How to guide AI coding assistants effectively

## 🚀 Next Steps for Implementation

This project is **ready for implementation**. The recommended sequence:

1. **Start with Entities** - Implement domain models (Individual, Student, Application)
2. **Build Financial Engine** - Create loan calculation logic
3. **Add Data Layer** - Implement repositories with SQLAlchemy
4. **Create Services** - Build business logic orchestration  
5. **Add Web Interface** - Implement Flask presentation layer

## 💡 Why This Approach Matters

This project demonstrates **professional software development practices**:

- **Plan First, Code Second**: Complete design before implementation reduces bugs and rework
- **Separation of Concerns**: Layered architecture makes complex systems manageable
- **Test-Driven Development**: Tests as specifications improve code quality
- **Domain-Driven Design**: Business concepts drive technical decisions
- **Documentation-Driven Development**: Clear documentation enables collaboration

---

**Ready to learn?** Start by reading `docs/PRD.md` to understand the business requirements, then explore `docs/SYSTEM_DESIGN.md` to see how those requirements become a technical architecture.
