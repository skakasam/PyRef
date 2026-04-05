"""Inserting data into tables"""

import sqlite3
from contextlib import closing
from datetime import date

from . import DATABASE


def insert_project(cursor, id, name, description):
    """Inserts a project record."""
    cursor.execute(
        "INSERT INTO projects (id, name, description) VALUES (?, ?, ?)",
        (id, name, description),
    )


def insert_employee(cursor, id, name, dob, position, salary, email):
    """Inserts an employee record, validating dob is in the past."""

    if date.fromisoformat(dob) >= date.today():
        raise ValueError(f"Date of birth must be in the past, got: {dob}")

    cursor.execute(
        "INSERT INTO employees (id, name, dob, position, salary, email) VALUES (?, ?, ?, ?, ?, ?)",
        (id, name, dob, position, salary, email),
    )


def insert_allocation(cursor, id, employee_id, project_id):
    """Inserts an allocation record."""
    cursor.execute(
        "INSERT INTO allocations (id, employee_id, project_id) VALUES (?, ?, ?)",
        (id, employee_id, project_id),
    )


def main():
    projects_data = [
        (1, "Project Alpha", "A top-secret project to develop a new product."),
        (2, "Project Beta", "A project to improve our existing product line."),
    ]

    employees_data = [
        (1, "Alice Smith", "1985-06-15", "Manager", 75000.00, "alice.smith@example.com"),
        (2, "Bob Johnson", "1990-09-20", "Architect", 60000.00, "bob.johnson@example.com"),
        (3, "Charlie Brown", "1988-12-05", "Developer", 55000.00, "charlie.brown@example.com"),
        (4, "Diana Prince", "1992-03-10", "Developer", 50000.00, "diana.prince@example.com"),
        (5, "Ethan Hunt", "1987-11-25", "Tester", 45000.00, "ethan.hunt@example.com"),
        (6, "Fiona Gallagher", "1995-07-30", "Tester", 40000.00, "fiona.gallagher@example.com"),
        (7, "George Martin", "1983-04-18", "Support", 35000.00, "george.martin@example.com"),
        (8, "Hannah Lee", "1991-01-22", "Support", 32000.00, "hannah.lee@example.com"),
        (9, "Ian Wright", "1993-08-14", "Intern", 30000.00, "ian.wright@example.com"),
        (10, "Jane Doe", "1994-05-05", "Intern", 30000.00, "jane.doe@example.com"),
    ]

    allocations_data = [
        (1, 1, 1),  # Alice Smith allocated to Project Alpha
        (2, 1, 2),  # Alice Smith allocated to Project Beta
        (3, 2, 1),  # Bob Johnson allocated to Project Alpha
        (4, 3, 1),  # Charlie Brown allocated to Project Alpha
        (5, 4, 2),  # Diana Prince allocated to Project Beta
        (6, 5, 2),  # Ethan Hunt allocated to Project Beta
        (7, 6, 1),  # Fiona Gallagher allocated to Project Alpha
        (8, 7, 2),  # George Martin allocated to Project Beta
        (9, 8, 1),  # Hannah Lee allocated to Project Alpha
        (10, 9, 2),  # Ian Wright allocated to Project Beta
    ]

    with closing(sqlite3.connect(DATABASE)) as connection:
        with closing(connection.cursor()) as cursor:
            print("Inserting rows into the projects table")
            for project in projects_data:
                insert_project(cursor, *project)

            print("Inserting rows into the employees table")
            for employee in employees_data:
                insert_employee(cursor, *employee)

            print("Inserting rows into the allocations table")
            for allocation in allocations_data:
                insert_allocation(cursor, *allocation)

            connection.commit()
            print("Committing changes to the database")


if __name__ == "__main__":
    main()
