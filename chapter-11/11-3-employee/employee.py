# 11.3(a) Employee


class Employee:
    """A simple attempt to represent an employee."""

    def __init__(self, first_name, last_name, salary):
        """Initialize first name, last name, and salary attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, amount=5000):
        """Add the given amount to the employee's salary."""
        self.salary += amount
