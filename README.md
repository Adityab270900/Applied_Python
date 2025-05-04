# Applied_Python
# Implementing Object_oriented_programming >> School_Catalogue

# School Catalogue

This project demonstrates the use of Object-Oriented Programming (OOP) in Python to model a school system.

## Modules

### School_Catalogue.py
This module contains the following classes:

- **School**: A base class representing a generic school with attributes for name, level, and number of students.
- **PrimarySchool**: A subclass of `School` that adds a `pickupPolicy` attribute specific to primary schools.
- **MiddleSchool**: A subclass of `School` that adds a `clubs` attribute specific to middle schools.
- **HighSchool**: A subclass of `School` that adds a `sportsTeams` attribute specific to high schools.

Each class includes methods to access and modify their attributes, as well as a string representation for easy display.

### School_Catalogue_Property.py
This module contains the following classes implemented using the `@property` decorator:

- **School**: A base class representing a generic school with attributes for name, level, and number of students.
- **PrimarySchool**: A subclass of `School` that adds a `pickup_policy` attribute specific to primary schools.
- **HighSchool**: A subclass of `School` that adds a `sports_teams` attribute specific to high schools.

Each class uses the `@property` decorator for attribute access and modification, providing a more Pythonic way to handle getters and setters.

## How to Use

1. Import the `School`, `PrimarySchool`, and `HighSchool` classes from `School_Catalogue.py`.
2. Create instances of these classes to represent different schools.
3. Use the provided methods to interact with the school objects.

