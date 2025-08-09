import pytest
from try_test import *

# def test_give_default_raise():
#     employee = Employee('john', '22')
#     assert employee.give_raise() == 5000
#
# def test_give_custom_raise():
#     employee = Employee('john', '22',666)
#     assert employee.give_raise(666) == 666

@pytest.fixture
def employee():
    employee = Employee('john', '22')
    return employee

def test_give_default_raise(employee):
    # employee = Employee('john', '22')
    assert employee.give_raise() == 5000

def test_give_custom_raise(employee):
    # employee = Employee('john', '22',666)
    assert employee.give_raise(666) == 666