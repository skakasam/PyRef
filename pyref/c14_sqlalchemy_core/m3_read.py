"""Reading records from the database using SQLAlchemy Core"""

from sqlalchemy import Connection, CursorResult, MetaData, Table, select

from pyref.common import blue, green, red

from . import ENGINE

metadata = MetaData()
projects_table = Table("projects", metadata, autoload_with=ENGINE)
employees_table = Table("employees", metadata, autoload_with=ENGINE)
allocations_table = Table("allocations", metadata, autoload_with=ENGINE)


def read_projects(connection: Connection):
    """Reads and prints all projects from the database."""
    result: CursorResult = connection.execute(select(projects_table))
    print(red.head("Projects:"))
    for row in result.mappings():
        print(f"ID: {row['id']}, Name: {row['name']}, Description: {row['description']}")
    print()


def read_employees(connection: Connection):
    """Reads and prints all employees from the database."""
    result: CursorResult = connection.execute(
        select(
            employees_table.c.id,
            employees_table.c.name,
            employees_table.c.position,
            employees_table.c.salary,
        ).where((employees_table.c.salary > 50000) & (employees_table.c.position != "Intern"))
    )
    print(blue.head("Employees:"))
    for row in result.mappings():
        print(f"ID: {row['id']}, Name: {row['name']}, Position: {row['position']}, Salary: ${row['salary']:,.2f}")
    print()


def read_allocations(connection: Connection):
    """Reads and prints all allocations from the database."""
    result: CursorResult = connection.execute(
        select(allocations_table).where(allocations_table.c.employee_id.in_([1, 2, 3]))
    )
    print(green.head("Allocations:"))
    for row in result.mappings():
        print(f"ID: {row['id']}, Employee ID: {row['employee_id']}, Project ID: {row['project_id']}")
    print()


def main():
    """Main function to read and print all data from the database."""
    with ENGINE.connect() as connection:
        read_projects(connection)
        read_employees(connection)
        read_allocations(connection)


if __name__ == "__main__":
    main()
