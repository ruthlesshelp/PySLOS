# Lesson 01: Domain Entities and TDD Foundation

## 🎯 Learning Objectives

By the end of this lesson, you will:
- Understand how to implement domain entities using TDD
- Create the foundational data models for the PySLOS system
- Set up the project structure and testing framework
- Practice the Red-Green-Refactor TDD cycle

## 📋 What You'll Build

In this lesson, you'll implement the three core domain entities:

1. **Individual** - Base person entity with personal information
2. **Student** - Extends Individual with high school information  
3. **Application** - Loan application linked to a Student

## 🏗️ Project Setup Tasks

### Step 1: Create Project Structure
Create the following directories and files:

```
src/
├── __init__.py
├── entities/
│   ├── __init__.py
│   ├── individual.py
│   ├── student.py
│   └── application.py
└── exceptions.py

tests/
├── __init__.py
├── test_entities.py
└── conftest.py

requirements.txt
pytest.ini
```

### Step 2: Install Dependencies
Create `requirements.txt` with:
```
pytest>=7.0.0
pytest-cov>=4.0.0
```

### Step 3: Configure Testing
Create `pytest.ini` for test configuration.

## 🧪 TDD Implementation Sequence

### Phase 1: Individual Entity
Following TDD (Red-Green-Refactor):

**Business Requirements** (from docs/PRD.md):
- First name, last name (required)
- Middle initial, suffix (optional)
- Date of birth (required, must be in past)
- Must be 18+ years old for loan eligibility

**TDD Steps**:
1. Write failing test for Individual creation
2. Implement minimal Individual class
3. Write failing test for age validation
4. Implement age validation logic
5. Refactor for clean code

### Phase 2: Student Entity  
**Business Requirements**:
- Inherits from Individual
- High school name (required)
- High school city, state (required)
- High school graduation year (optional)

**TDD Steps**:
1. Write failing test for Student creation
2. Implement Student inheriting from Individual
3. Write failing test for high school validation
4. Implement validation logic
5. Refactor for clean code

### Phase 3: Application Entity
**Business Requirements**:
- Linked to a Student
- Principal amount: $1,000 - $999,999.99
- APR: 0.01% - 19.99%
- Term: 1 - 360 months
- Unique application ID

**TDD Steps**:
1. Write failing test for Application creation
2. Implement basic Application class
3. Write failing tests for business rule validation
4. Implement validation logic
5. Refactor for clean code

## 💡 Key Concepts to Practice

### Domain-Driven Design
- Rich domain objects with behavior, not just data
- Business rules enforced within entities
- Clear separation between entities

### Test-Driven Development
- Red: Write failing test first
- Green: Implement minimal code to pass
- Refactor: Improve code while keeping tests green

### Business Rule Validation
- Age calculation and validation
- Monetary range validation
- Required field validation

## ✅ Success Criteria

By the end of this lesson, you should have:

- [ ] Working project structure with proper Python packages
- [ ] pytest configured and running
- [ ] Individual entity with age validation
- [ ] Student entity inheriting from Individual
- [ ] Application entity with business rule validation
- [ ] 100% test coverage for all entities
- [ ] All tests passing
- [ ] Clean, readable code following Python conventions

## 🔗 Next Lesson Preview

**Lesson 02** will focus on the Financial Engine:
- Loan calculation algorithms
- Monthly payment computation
- APR to monthly rate conversion
- Interest calculation logic

## 💡 Tips for Success

1. **Start Small**: Implement one test and one method at a time
2. **Read the Docs**: Reference `docs/PRD.md` for exact business requirements
3. **TDD Discipline**: Always write the test first
4. **Refactor Frequently**: Clean up code after tests pass
5. **Ask Questions**: Use the documentation to understand business context

## 🚀 Ready to Start?

Begin by setting up the project structure, then start with your first failing test for the Individual entity!