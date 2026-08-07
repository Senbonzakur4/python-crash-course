# 11.3(b) Employee

import pytest

from employee import Employee


@pytest.fixture
def employee():
    """An employee instance available to each test function."""
    return Employee("Miku", "Hatsune", 10000)


def test_give_default_raise(employee):
    """Gives the default raise '$5,000'."""
    employee.give_raise()
    assert employee.salary == 15000


def test_give_custom_raise(employee):
    """Prompts for a custom raise"""

    employee.give_raise(39)
    assert employee.salary == 10039
