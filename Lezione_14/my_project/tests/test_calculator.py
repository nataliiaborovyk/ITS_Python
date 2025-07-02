from my_project.calculator import Calculator
import pytest

@pytest.fixture
def calculation():
    return Calculator(10,5)

def test_addition(calculation):
    #calculation: Calculator = Calculator(10,5)
    assert calculation.addition() == 13, 'The sum is wrong'

def test_subtraction(calculation):
    #calculation: Calculator = Calculator(10, 5)
    assert calculation.subtraction()  == 5, ' The subtraction is wrong'

def test_multiplication(calculation):
    #calculation: Calculator = Calculator(10, 5)
    assert calculation.multiplication()  == 50, ' The moltiplication is wrong'

def test_division(calculation):
    #calculation: Calculator = Calculator(10, 5)
    assert calculation.division()  == 2.00, ' The division is wrong'