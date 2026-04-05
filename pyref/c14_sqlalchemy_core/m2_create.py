"""Inseting records into the database using SQLAlchemy Core"""

from datetime import date

import sqlalchemy as sa

from . import ENGINE

metadata = sa.MetaData()
projects_table = sa.Table("projects", metadata, autoload_with=ENGINE)
employees_table = sa.Table("employees", metadata, autoload_with=ENGINE)
allocations_table = sa.Table("allocations", metadata, autoload_with=ENGINE)


def insert_projects(connection: sa.Connection):
    """Inserts sample projects into the database."""
    result: sa.CursorResult = connection.execute(
        sa.insert(projects_table),
        [
            {
                "id": 1,
                "name": "Project Alpha",
                "description": "A top-secret project.",
            },
            {
                "id": 2,
                "name": "Project Beta",
                "description": "A public-facing project.",
            },
        ],
    )
    print(f"{result.rowcount} project rows inserted successfully.")


def insert_employees(connection: sa.Connection):
    """Inserts sample employees into the database."""
    result: sa.CursorResult = connection.execute(
        sa.insert(employees_table),
        [
            {
                "id": 1,
                "name": "Alice Smith",
                "dob": date.fromisoformat("1985-06-15"),
                "position": "Manager",
                "salary": 75000.00,
                "email": "alice.smith@example.com",
            },
            {
                "id": 2,
                "name": "Bob Johnson",
                "dob": date.fromisoformat("1990-09-20"),
                "position": "Architect",
                "salary": 60000.00,
                "email": "bob.johnson@example.com",
            },
            {
                "id": 3,
                "name": "Charlie Brown",
                "dob": date.fromisoformat("1988-12-05"),
                "position": "Developer",
                "salary": 55000.00,
                "email": "charlie.brown@example.com",
            },
            {
                "id": 4,
                "name": "Diana Prince",
                "dob": date.fromisoformat("1992-03-10"),
                "position": "Developer",
                "salary": 50000.00,
                "email": "diana.prince@example.com",
            },
            {
                "id": 5,
                "name": "Ethan Hunt",
                "dob": date.fromisoformat("1987-11-25"),
                "position": "Tester",
                "salary": 45000.00,
                "email": "ethan.hunt@example.com",
            },
            {
                "id": 6,
                "name": "Fiona Gallagher",
                "dob": date.fromisoformat("1995-07-30"),
                "position": "Tester",
                "salary": 40000.00,
                "email": "fiona.gallagher@example.com",
            },
            {
                "id": 7,
                "name": "George Martin",
                "dob": date.fromisoformat("1983-04-18"),
                "position": "Support",
                "salary": 35000.00,
                "email": "george.martin@example.com",
            },
            {
                "id": 8,
                "name": "Hannah Lee",
                "dob": date.fromisoformat("1991-01-22"),
                "position": "Support",
                "salary": 32000.00,
                "email": "hannah.lee@example.com",
            },
            {
                "id": 9,
                "name": "Ian Wright",
                "dob": date.fromisoformat("1993-08-14"),
                "position": "Intern",
                "salary": 30000.00,
                "email": "ian.wright@example.com",
            },
            {
                "id": 10,
                "name": "Jane Doe",
                "dob": date.fromisoformat("1994-05-05"),
                "position": "Intern",
                "salary": 30000.00,
                "email": "jane.doe@example.com",
            },
        ],
    )
    print(f"{result.rowcount} employee rows inserted successfully.")


def insert_allocations(connection: sa.Connection):
    """Inserts sample allocations into the database."""
    result: sa.CursorResult = connection.execute(
        sa.insert(allocations_table),
        [
            {"id": 1, "employee_id": 1, "project_id": 1},
            {"id": 2, "employee_id": 1, "project_id": 2},
            {"id": 3, "employee_id": 2, "project_id": 1},
            {"id": 4, "employee_id": 3, "project_id": 1},
            {"id": 5, "employee_id": 4, "project_id": 2},
            {"id": 6, "employee_id": 5, "project_id": 2},
            {"id": 7, "employee_id": 6, "project_id": 1},
            {"id": 8, "employee_id": 7, "project_id": 2},
            {"id": 9, "employee_id": 8, "project_id": 1},
            {"id": 10, "employee_id": 9, "project_id": 2},
        ],
    )
    print(f"{result.rowcount} allocation rows inserted successfully.")


def main():
    """Inserts sample records into the database."""
    with ENGINE.connect() as connection:
        with connection.begin():  # begins a transaction
            insert_projects(connection)
            insert_employees(connection)
            insert_allocations(connection)
        # auto-commits on success, auto-rollbacks on exception
    # no need for explicit connection.commit()


if __name__ == "__main__":
    main()
