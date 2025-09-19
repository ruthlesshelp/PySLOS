# Lesson 01: TDD Foundation with Financial Calculator

## 🎯 Learning Objectives

By the end of this lesson, you will:
- **Experience textbook TDD** - tests driving design and existing before implementation
- Understand the **Red-Green-Refactor cycle** through practical application
- Set up professional Python project structure with pytest
- Implement a **FinancialCalculator** class using pure TDD approach
- Learn how business requirements translate directly to test cases

## � **TDD Red Phase: ACCOMPLISHED!**

We've successfully created the perfect TDD starting point:

### ✅ **What We've Built**

```
PySLOS/
├── src/
│   ├── __init__.py
│   └── financial/
│       └── __init__.py              # Ready for calculator.py
├── tests/
│   ├── __init__.py
│   └── test_financial.py           # 🔴 4 FAILING tests
├── lessons/
│   └── LESSON_01.md               # This lesson plan
├── requirements.txt               # pytest, pytest-cov
└── pytest.ini                   # Test configuration
```

### 🎯 **Perfect TDD Example in Action**

Our failing test demonstrates **TDD done right**:

```python
# THIS IS WHAT WE WANT IN TDD! �
def test_calculate_monthly_payment_with_valid_input_expect_correct_amount(self):
    # Arrange
    from src.financial.calculator import FinancialCalculator  # ❌ Module doesn't exist yet!
    
    calculator = FinancialCalculator()  # ❌ Class doesn't exist yet!
    principal = Decimal('10000.00')
    annual_percentage_rate = Decimal('6.0')
    term_months = 12
    
    # Act
    monthly_payment = calculator.calculate_monthly_payment(
        principal=principal,
        apr=annual_percentage_rate,
        term_months=term_months
    )
    
    # Assert
    expected_payment = Decimal('860.66')
    assert monthly_payment == expected_payment
```

**Current Test Output** (exactly what we want!):
```bash
ModuleNotFoundError: No module named 'src.financial.calculator'
```

This is **perfect TDD Red phase** - clean failing test because the module doesn't exist yet! 🔴

## 📋 What We're Building: Financial Calculator

### Business Requirements Embedded in Tests

Our tests contain real financial business rules from `docs/PRD.md`:

1. **Monthly Payment Calculation**
   - Use standard amortization formula
   - Example: $10K loan, 6% APR, 12 months = $860.66/month

2. **Principal Validation** 
   - Must be between $1,000 - $999,999.99
   - Raise `ValueError` for amounts outside range

3. **APR Conversion**
   - Convert annual percentage rate to monthly rate
   - 6 decimal precision: 6% APR = 0.005000 monthly rate

4. **Comprehensive Error Handling**
   - Descriptive error messages
   - Business rule enforcement

## 🟢 **Next: TDD Green Phase Implementation**

Now we implement **minimal code** to make our failing tests pass:

### Step 1: Create the FinancialCalculator Class

Create `src/financial/calculator.py` with:

```python
from decimal import Decimal

class FinancialCalculator:
    """Financial calculations for loan origination."""
    
    def calculate_monthly_payment(self, principal: Decimal, apr: Decimal, term_months: int) -> Decimal:
        """Calculate monthly payment using amortization formula."""
        # TODO: Implement amortization formula
        raise NotImplementedError("Calculate monthly payment not yet implemented")
    
    def validate_principal(self, principal: Decimal) -> None:
        """Validate principal amount within business rules."""
        # TODO: Implement validation logic
        raise NotImplementedError("Principal validation not yet implemented")
    
    def convert_apr_to_monthly_rate(self, apr: Decimal) -> Decimal:
        """Convert APR to monthly rate with 6 decimal precision."""
        # TODO: Implement conversion logic
        raise NotImplementedError("APR conversion not yet implemented")
```

### Step 2: Run Tests and Watch Them Fail Differently

```bash
python3 -m pytest tests/test_financial.py -v
```

Now tests will fail with `NotImplementedError` instead of `ModuleNotFoundError` - progress! 🎉

### Step 3: Implement One Method at a Time

**TDD Green Phase Process**:

1. **Make the first test pass** - implement `calculate_monthly_payment()`
2. **Run tests** - verify the specific test passes
3. **Make the second test pass** - implement `validate_principal()`
4. **Continue until all tests pass**

### 🧮 Financial Formulas to Implement

**Monthly Payment Formula (Amortization)**:
```
M = P × [r(1+r)^n] / [(1+r)^n - 1]

Where:
- M = Monthly payment
- P = Principal (loan amount)
- r = Monthly interest rate (APR/12/100)
- n = Number of payments (term in months)
```

**APR to Monthly Rate**:
```
monthly_rate = (apr / 100) / 12
```

## 🔄 **TDD Refactor Phase**

After all tests pass (Green phase):

1. **Improve code quality** while keeping tests green
2. **Add documentation and type hints**
3. **Extract common validation logic**
4. **Optimize calculations for precision**

## ✅ **Success Criteria - Updated**

By the end of this lesson, you should have:

- [x] Working project structure with proper Python packages
- [x] pytest configured and running
- [x] Comprehensive failing tests (Red phase complete!)
- [ ] FinancialCalculator class with working methods
- [ ] All 4 tests passing (Green phase)
- [ ] Clean, refactored code (Refactor phase)
- [ ] 100% test coverage for financial calculations

## 🔬 **What Makes This Great TDD**

1. **Tests First**: We wrote comprehensive tests before any implementation
2. **Business-Driven**: Tests encode real financial requirements from PRD
3. **Clear Failures**: ModuleNotFoundError → NotImplementedError → Passing tests
4. **Incremental**: One test, one method, one success at a time
5. **Refactor-Safe**: Tests protect against regression during cleanup

## 💡 **Key TDD Insights from This Lesson**

### ✨ **Why This Approach Works**

- **Tests as Specification**: Our tests clearly define what the calculator must do
- **Confidence in Changes**: Tests catch regressions during refactoring  
- **Minimal Implementation**: Only write code needed to pass tests
- **Business Focus**: Financial domain drives technical implementation

### 🎯 **Professional TDD Benefits**

- **Design Emerges**: API design comes from test requirements, not assumptions
- **Quality Built-In**: Code is testable by design (because tests came first!)
- **Documentation**: Tests serve as executable specifications
- **Regression Protection**: Future changes can't break existing functionality

## 🔗 **Next Lesson Preview**

**Lesson 02** will build on this foundation:
- Domain entities (Individual, Student, Application)
- Repository pattern for data access
- Integration tests with SQLAlchemy
- Service layer orchestration

## 🚀 **Ready for Green Phase?**

You now have the perfect TDD foundation. **Your mission**: Make those failing tests pass, one implementation at a time!

```bash
# Start here:
python3 -m pytest tests/test_financial.py::TestFinancialCalculator::test_calculate_monthly_payment_with_valid_input_expect_correct_amount -v
```

Remember: **Write only enough code to make the current test pass!** 🎯