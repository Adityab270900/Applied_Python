"""
This module contains classes to represent a school system using Object-Oriented Programming (OOP) with the @property decorator.

Classes:
    School: A base class representing a generic school.
    PrimarySchool: A subclass of School representing primary schools.
    HighSchool: A subclass of School representing high schools.

Each class uses the @property decorator for attribute access and modification.
"""

class School:
    """
    Represents a generic school.

    Attributes:
        name (str): The name of the school.
        level (str): The level of the school (e.g., primary, high).
        number_of_students (int): The number of students in the school.
    """
    def __init__(self, name, level, number_of_students):
        self._name = name
        self._level = level
        self._number_of_students = number_of_students

    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level

    @property
    def number_of_students(self):
        return self._number_of_students

    @number_of_students.setter
    def number_of_students(self, number):
        self._number_of_students = number

    def __repr__(self):
        return f"A {self.level} school named {self.name} with {self.number_of_students} students"

class PrimarySchool(School):
    """
    Represents a primary school, inheriting from the School class.

    Attributes:
        pickup_policy (str): The policy for picking up students.
    """
    def __init__(self, name, number_of_students, pickup_policy):
        super().__init__(name, "primary", number_of_students)
        self._pickup_policy = pickup_policy

    @property
    def pickup_policy(self):
        return self._pickup_policy

    def __repr__(self):
        return super().__repr__() + f"\npickup_policy: {self.pickup_policy}"

class HighSchool(School):
    """
    Represents a high school, inheriting from the School class.

    Attributes:
        sports_teams (list): A list of sports teams in the school.
    """
    def __init__(self, name, number_of_students, sports_teams):
        super().__init__(name, "high", number_of_students)
        self._sports_teams = sports_teams

    @property
    def sports_teams(self):
        return self._sports_teams

    def __repr__(self):
        return super().__repr__() + f"\nsports_teams: {self.sports_teams}"