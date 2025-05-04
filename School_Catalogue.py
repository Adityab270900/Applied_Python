"""
This module contains classes to represent a school system using Object-Oriented Programming (OOP).

Classes:
    School: A base class representing a generic school.
    PrimarySchool: A subclass of School representing primary schools.
    HighSchool: A subclass of School representing high schools.

Each class includes methods to access and modify their attributes, as well as a string representation for easy display.
"""

class School:
    """
    Represents a generic school.

    Attributes:
        name (str): The name of the school.
        level (str): The level of the school (e.g., primary, high).
        numberOfStudents (int): The number of students in the school.
    """
    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_numberOfStudents(self):
        return self.numberOfStudents

    def set_numberOfStudents(self, number):
        self.numberOfStudents = number
        return self.numberOfStudents

    def __repr__(self):
        return f"A {self.level} school named {self.name} with {self.numberOfStudents} students"

class PrimarySchool(School):
    """
    Represents a primary school, inheriting from the School class.

    Attributes:
        pickupPolicy (str): The policy for picking up students.
    """
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, "primary", numberOfStudents)
        self.pickupPolicy = pickupPolicy

    def get_pickupPolicy(self):
        return self.pickupPolicy

    def __repr__(self):
        return super().__repr__() + f"\npickupPolicy : {self.pickupPolicy}"

class MiddleSchool(School):
    """
    Represents a middle school, inheriting from the School class.

    Attributes:
        clubs (list): A list of clubs in the school.
    """
    def __init__(self, name, numberOfStudents, clubs):
        super().__init__(name, "middle", numberOfStudents)
        self.clubs = clubs

    def get_clubs(self):
        return self.clubs

    def __repr__(self):
        return super().__repr__() + f"\nclubs: {self.clubs}"


class HighSchool(School):
    """
    Represents a high school, inheriting from the School class.

    Attributes:
        sportsTeams (list): A list of sports teams in the school.
    """
    def __init__(self, name, numberOfStudents, sportsTeams):
        super().__init__(name, "high", numberOfStudents)
        self.sportsTeams = sportsTeams

    def get_sportsTeams(self):
        return self.sportsTeams

    def __repr__(self):
        return super().__repr__() + f"\nsportsTeams: {self.sportsTeams}"