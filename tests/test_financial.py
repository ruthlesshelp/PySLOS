"""
Test module for financial calculations in PySLOS.

This module contains tests for the FinancialCalculator class which handles
loan payment calculations, interest rate conversions, and other financial
computations according to the business requirements in docs/PRD.md.

Following TDD principles, these tests are written BEFORE the implementation
to drive the design of the financial calculation engine.
"""

import pytest
from decimal import Decimal


class TestFinancialCalculator:
    """Test cases for the FinancialCalculator class."""
    
    def test_calculate_monthly_payment_with_valid_input_expect_correct_amount(self):
        """
        Test that monthly payment calculation returns the correct amount
        for a standard loan scenario.
        
        Business Rule: Use standard amortization formula to calculate
        monthly payments based on principal, APR, and term.
        
        Example from financial calculator:
        - Principal: $10,000
        - APR: 6.0% (0.005 monthly rate)
        - Term: 12 months
        - Expected monthly payment: $860.66
        """
        # Arrange
        from src.financial.calculator import FinancialCalculator
        
        calculator = FinancialCalculator()
        principal = Decimal('10000.00')
        annual_percentage_rate = Decimal('6.0')  # 6.0% APR
        term_months = 12
        
        # Act
        monthly_payment = calculator.calculate_monthly_payment(
            principal=principal,
            apr=annual_percentage_rate,
            term_months=term_months
        )
        
        # Assert
        expected_payment = Decimal('860.66')
        assert monthly_payment == expected_payment, (
            f"Expected monthly payment of {expected_payment}, "
            f"but got {monthly_payment}"
        )


class TestLoanValidation:
    """Test cases for loan parameter validation."""
    
    def test_validate_principal_within_range_expect_no_exception(self):
        """
        Test that principal amounts within business rules are accepted.
        
        Business Rule: Principal must be between $1,000 and $999,999.99
        """
        # Arrange
        from src.financial.calculator import FinancialCalculator
        
        calculator = FinancialCalculator()
        valid_principals = [
            Decimal('1000.00'),    # Minimum allowed
            Decimal('50000.00'),   # Typical amount
            Decimal('999999.99')   # Maximum allowed
        ]
        
        # Act & Assert
        for principal in valid_principals:
            # Should not raise any exception
            calculator.validate_principal(principal)
    
    def test_validate_principal_below_minimum_expect_value_error(self):
        """
        Test that principal amounts below $1,000 raise ValueError.
        
        Business Rule: Principal must be at least $1,000
        """
        # Arrange
        from src.financial.calculator import FinancialCalculator
        
        calculator = FinancialCalculator()
        invalid_principal = Decimal('999.99')  # Below minimum
        
        # Act & Assert
        with pytest.raises(ValueError, match="Principal must be between"):
            calculator.validate_principal(invalid_principal)


class TestAPRConversion:
    """Test cases for APR to monthly rate conversion."""
    
    def test_convert_apr_to_monthly_rate_with_6_percent_expect_half_percent(self):
        """
        Test conversion of 6% APR to monthly rate.
        
        Business Rule: APR converted to monthly rate with 6 decimal precision.
        6% APR = 0.06 / 12 = 0.005000 monthly rate
        """
        # Arrange
        from src.financial.calculator import FinancialCalculator
        
        calculator = FinancialCalculator()
        apr = Decimal('6.0')  # 6% APR
        
        # Act
        monthly_rate = calculator.convert_apr_to_monthly_rate(apr)
        
        # Assert
        expected_rate = Decimal('0.005000')  # 6 decimal precision
        assert monthly_rate == expected_rate, (
            f"Expected monthly rate of {expected_rate}, "
            f"but got {monthly_rate}"
        )