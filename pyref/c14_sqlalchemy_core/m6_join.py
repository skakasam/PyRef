"""Joining tables using SQLAlchemy Core"""

from sqlalchemy import Connection, MetaData, Table, join, select

from . import ENGINE

metadata = MetaData()
projects_table = Table("projects", metadata, autoload_with=ENGINE)
employees_table = Table("employees", metadata, autoload_with=ENGINE)
allocations_table = Table("allocations", metadata, autoload_with=ENGINE)


def join_tables(connection: Connection):
    """Performs a join between employees and projects through allocations."""
    results = connection.execute(
        select(
            projects_table.c.name.label("project"),
            employees_table.c.name.label("employee"),
            employees_table.c.position.label("position"),
            employees_table.c.salary.label("salary"),
        )
        .select_from(
            join(
                employees_table,
                allocations_table,
                employees_table.c.id == allocations_table.c.employee_id,
            ).join(
                projects_table,
                allocations_table.c.project_id == projects_table.c.id,
            )
        )
        .where(projects_table.c.id == 1)
        .order_by(employees_table.c.salary.desc())
    )

    print("Employees allocated to Project ID 1:")
    for row in results.mappings():
        print(
            f"Project: {row['project']}, Employee: {row['employee']}, Position: {row['position']}, Salary: ${row['salary']:,.2f}"
        )
    print()


def main():
    """Main function to perform the join and print results."""
    with ENGINE.connect() as connection:
        join_tables(connection)


if __name__ == "__main__":
    main()
