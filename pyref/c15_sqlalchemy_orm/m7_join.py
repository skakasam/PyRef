"""Join database tables using the SQLAlchemy ORM."""

from sqlalchemy import select

from . import SESSION, Allocations, Employees, Projects


def main():
    with SESSION.begin() as session:
        # Join Employees and Allocations to get employee names and their allocated project IDs
        allocations = session.execute(
            select(
                Employees.name.label("name"),
                Employees.position.label("role"),
                Projects.name.label("project"),
            )
            .join(Allocations, Employees.id == Allocations.employee_id)
            .join(Projects, Allocations.project_id == Projects.id)
            .where(Allocations.project_id.in_([1]))
            .order_by(Employees.id)
        ).all()
        print("Employee Allocations:")
        for name, role, project in allocations:
            print(f"Project: {project}, Employee: {name}, Role: {role}")
    # commits transaction, closes session


if __name__ == "__main__":
    main()
