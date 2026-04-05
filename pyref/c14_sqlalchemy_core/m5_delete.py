"""Deleting records from the database using SQLAlchemy Core"""

from sqlalchemy import Connection, CursorResult, MetaData, Table, delete

from . import ENGINE

metadata = MetaData()
employees_table = Table("employees", metadata, autoload_with=ENGINE)


def delete_employees(connection: Connection):
    """Deletes employee 10 from the database."""
    result: CursorResult = connection.execute(delete(employees_table).where(employees_table.c.id == 10))
    print(f"{result.rowcount} employee rows deleted successfully.")
    print("Deleted employees with id = 10.")


def main():
    """Main function to delete employee records from the database."""
    with ENGINE.connect() as connection:
        with connection.begin():
            delete_employees(connection)


if __name__ == "__main__":
    main()
