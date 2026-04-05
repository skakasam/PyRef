"""Using SQLAlchemy Core to Connect to a Database and Create a Table"""

import sqlalchemy as sa

from . import ENGINE

# Create a metadata object
metadata = sa.MetaData()

# Define tables with columns
projects_table = sa.Table(
    "projects",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("name", sa.String(50), nullable=False),
    sa.Column("description", sa.String(200)),
    sqlite_autoincrement=True,
)

positions = ["Manager", "Architect", "Developer", "Tester", "Support", "Intern"]
PositionType = sa.Enum(*positions, name="position_type")
employees_table = sa.Table(
    "employees",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("name", sa.String(50), nullable=False),
    sa.Column("dob", sa.Date, nullable=False),
    sa.Column("position", PositionType, nullable=False),
    sa.Column("salary", sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column("email", sa.String(100), nullable=False, unique=True),
    sa.CheckConstraint("salary > 0", name="salary_positive"),
    sa.CheckConstraint("email LIKE '%_@__%.__%'", name="email_format"),
    sa.CheckConstraint(f"""position IN ('{"', '".join(positions)}')""", name="valid_position"),
    sa.CheckConstraint("dob GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'", name="dob_valid"),
    sqlite_autoincrement=True,
)

allocations_table = sa.Table(
    "allocations",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("employee_id", sa.Integer, sa.ForeignKey("employees.id", ondelete="CASCADE"), nullable=False),
    sa.Column("project_id", sa.Integer, sa.ForeignKey("projects.id", ondelete="CASCADE"), nullable=False),
    sa.UniqueConstraint("employee_id", "project_id", name="uq_employee_project"),
    sqlite_autoincrement=True,
)


def print_ddls(*tables):
    """Prints the DDL statements for all tables."""
    for table in tables:
        print(f"{table.name} Table DDL:")
        print(str(sa.schema.CreateTable(table).compile(ENGINE)))


def recreate_tables(*tables):
    """Drops and recreates all tables."""
    metadata.drop_all(ENGINE, tables, checkfirst=True)
    metadata.create_all(ENGINE, tables, checkfirst=True)
    print("Tables created successfully.")


def main():
    print_ddls(projects_table, employees_table, allocations_table)
    recreate_tables(projects_table, employees_table, allocations_table)


if __name__ == "__main__":
    main()
