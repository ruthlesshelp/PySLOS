# GitHub Copilot Instructions for PySLOS

## Project Overview

PySLOS is a Python-based Student Loan Origination System designed using modular layered architecture. This project follows TDD principles with comprehensive business domain modeling for financial services.

**Current Status**: Documentation-complete, implementation-ready project with detailed PRD, system design, and test plans.

## Architecture Overview

PySLOS implements a **Modular Layered Architecture** with these core layers:
- **Presentation Layer**: Flask web interface (future)
- **Service Layer**: Business logic and domain rules
- **Financial Engine**: Loan calculations and amortization
- **Data Access Layer**: SQLAlchemy ORM with Repository pattern
- **Database Layer**: SQLite for simplicity with normalized schema

**Key Design Patterns**: Repository, Factory, Domain Model, Data Mapper

## Project Structure

Expected structure when implemented:
- `src/` - Main business logic organized by domain
- `src/entities/` - Domain models (Individual, Student, Application)
- `src/repositories/` - Data access layer
- `src/services/` - Business logic and orchestration
- `src/financial/` - Loan calculation engine
- `tests/` - Comprehensive TDD test suite
- `docs/` - Complete technical documentation (PRD.md, SYSTEM_DESIGN.md, TEST_PLAN.md)

## Domain Knowledge

**Core Business Entities**:
- `Individual`: Personal info (first/last name, DOB, etc.)
- `Student`: Extends Individual with high school information
- `Application`: Loan details linked to Student (principal, APR, term)

**Critical Business Rules** (from docs/PRD.md):
- Borrower must be ≥ 18 years old
- Loan principal: $1,000–$999,999.99
- APR range: 0.01%–19.99%
- Loan term: 1–360 months
- One student can have multiple applications

**Financial Calculations**:
- Monthly payment using amortization formula
- APR to monthly rate conversion (6 decimal precision)

## Technology Stack

- **Framework**: Flask for web layer
- **ORM**: SQLAlchemy with Repository pattern
- **Database**: SQLite for simplicity
- **Testing**: pytest with 100% coverage target
- **Validation**: Marshmallow schemas
- **Python**: 3.11+ required

## Development Workflow

**TDD Implementation Pattern**:
1. Reference `docs/TEST_PLAN.md` for testing strategy
2. Write failing tests for business requirements
3. Implement minimum code to pass tests
4. Refactor while maintaining green tests

**Key Files for Context**:
- `docs/PRD.md` - Complete business requirements and user stories
- `docs/SYSTEM_DESIGN.md` - Detailed architecture and component design
- `docs/TEST_PLAN.md` - Testing strategy and patterns

## Testing Strategy

**Test Coverage**: Target 100% coverage using `pytest-cov`

```bash
pytest tests/ -v --cov=src --cov-report=html --cov-report=term-missing
```

**Test Organization** (per TEST_PLAN.md):
- `tests/test_entities.py` - Domain model tests
- `tests/test_repositories.py` - Data access tests  
- `tests/test_financial.py` - Loan calculation tests
- `tests/test_services.py` - Business logic tests

**Testing Patterns**:
- AAA pattern (Arrange, Act, Assert)
- Descriptive test names: `test_calculate_monthly_payment_with_valid_input_expect_correct_amount`
- Data-driven testing for boundary values
- Mock external dependencies (database, external services)

## Exception Handling Conventions

Use specific exceptions for different error conditions:
- `ValueError` - Invalid input parameters
- `BusinessRuleError` - Domain rule violations (custom exception)
- `DatabaseError` - Data persistence issues (custom exception)
- `NotImplementedError` - Placeholder for future features

## Implementation Priorities

When implementing, follow this sequence based on the architecture:
1. **Entities** - Start with domain models (Individual, Student, Application)
2. **Financial Engine** - Core loan calculation logic
3. **Repositories** - Data access layer with SQLAlchemy
4. **Services** - Business logic orchestration
5. **Flask Layer** - Web interface (last priority)