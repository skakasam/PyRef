"""Updating records in the database using SQLAlchemy Core"""

from sqlalchemy import Connection, CursorResult, MetaData, Table, update

from pyref.common import blue, green

from . import ENGINE

metadata = MetaData()
employees_table = Table("employees", metadata, autoload_with=ENGINE)
allocations_table = Table("allocations", metadata, autoload_with=ENGINE)


def update_employees(connection: Connection):
    """Updates employee salaries based on position."""
    print(blue.bold("Commencing employee updates."))

    updt1: CursorResult = connection.execute(
        update(employees_table).where(employees_table.c.id == 3).values(position="Architect", salary=65000.00)
    )
    print(f"{updt1.rowcount} employee rows updated successfully.")
    print("Employee with ID 3 promoted to Architect with a salary of $65,000.00.")

    updt2: CursorResult = connection.execute(
        update(employees_table).where(employees_table.c.id == 9).values(position="Developer", salary=55000.00)
    )
    print(f"{updt2.rowcount} employee rows updated successfully.")
    print("Employee with ID 9 promoted to Developer with a salary of $55,000.00.")

    updt3: CursorResult = connection.execute(
        update(allocations_table).where(allocations_table.c.employee_id == 3).values(project_id=2)
    )
    print(f"{updt3.rowcount} allocation rows updated successfully.")
    print("Allocation for employee with ID 3 updated to project ID 2.")

    updt4: CursorResult = connection.execute(
        update(allocations_table).where(allocations_table.c.employee_id == 9).values(project_id=1)
    )
    print(f"{updt4.rowcount} allocation rows updated successfully.")
    print("Allocation for employee with ID 9 updated to project ID 1.")

    print(green.bold("Completed employee updates."))


def main():
    """Main function to update employee records in the database."""
    with ENGINE.connect() as connection:
        with connection.begin():
            update_employees(connection)


if __name__ == "__main__":
    main()
