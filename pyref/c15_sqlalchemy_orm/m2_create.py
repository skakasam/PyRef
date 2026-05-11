"""Insert data into the database using the SQLAlchemy ORM."""

from datetime import date
from decimal import Decimal

from . import SESSION, Allocations, Employees, Projects

_PROJECTS = [
    {
        "name": "Project Alpha",
        "description": "Alpha project description.",
    },
    {
        "name": "Project Beta",
        "description": "Beta project description.",
    },
]
_EMPLOYEES = [
    {
        "name": "Alice Smith",
        "dob": date(1985, 6, 15),
        "position": "Manager",
        "salary": Decimal(75000.00),
        "email": "alice.smith@example.com",
    },
    {
        "name": "Bob Johnson",
        "dob": date(1990, 9, 20),
        "position": "Architect",
        "salary": Decimal(60000.00),
        "email": "bob.johnson@example.com",
    },
    {
        "name": "Charlie Brown",
        "dob": date(1988, 12, 5),
        "position": "Developer",
        "salary": Decimal(55000.00),
        "email": "charlie.brown@example.com",
    },
    {
        "name": "Diana Prince",
        "dob": date(1992, 3, 10),
        "position": "Developer",
        "salary": Decimal(50000.00),
        "email": "diana.prince@example.com",
    },
    {
        "name": "Ethan Hunt",
        "dob": date(1987, 11, 25),
        "position": "Tester",
        "salary": Decimal(45000.00),
        "email": "ethan.hunt@example.com",
    },
    {
        "name": "Fiona Gallagher",
        "dob": date(1995, 7, 30),
        "position": "Tester",
        "salary": Decimal(40000.00),
        "email": "fiona.gallagher@example.com",
    },
    {
        "name": "George Martin",
        "dob": date(1983, 4, 18),
        "position": "Support",
        "salary": Decimal(35000.00),
        "email": "george.martin@example.com",
    },
    {
        "name": "Hannah Lee",
        "dob": date(1991, 1, 22),
        "position": "Support",
        "salary": Decimal(32000.00),
        "email": "hannah.lee@example.com",
    },
    {
        "name": "Ian Wright",
        "dob": date(1993, 8, 14),
        "position": "Intern",
        "salary": Decimal(30000.00),
        "email": "ian.wright@example.com",
    },
    {
        "name": "Jane Doe",
        "dob": date(1994, 5, 5),
        "position": "Intern",
        "salary": Decimal(30000.00),
        "email": "jane.doe@example.com",
    },
]
_ALLOCATIONS = [
    {"employee_id": 1, "project_id": 1},
    {"employee_id": 1, "project_id": 2},
    {"employee_id": 2, "project_id": 1},
    {"employee_id": 3, "project_id": 1},
    {"employee_id": 4, "project_id": 2},
    {"employee_id": 5, "project_id": 2},
    {"employee_id": 6, "project_id": 1},
    {"employee_id": 7, "project_id": 2},
    {"employee_id": 8, "project_id": 1},
    {"employee_id": 9, "project_id": 2},
]


def main():
    with SESSION.begin() as session:
        session.add_all([Projects(**proj) for proj in _PROJECTS])
        session.add_all([Employees(**emp) for emp in _EMPLOYEES])
        session.add_all([Allocations(**alloc) for alloc in _ALLOCATIONS])
    # commits transaction, closes session

    print("Projects added successfully.")
    print("Employees added successfully.")
    print("Allocations added successfully.")


if __name__ == "__main__":
    main()
