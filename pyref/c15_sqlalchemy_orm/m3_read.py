"""Read data from the database using the SQLAlchemy ORM."""

from sqlalchemy import and_, or_, select

from pyref.common import blue, green, red

from . import SESSION, Allocations, Employees, Projects


def main():
    with SESSION() as session:
        # ######################################
        # Query projects
        # ######################################
        projects = session.execute(select(Projects)).scalars().all()
        print(red.head("Projects:"))
        for proj in projects:
            print(f"ID: {proj.id}, Name: {proj.name}, Description: {proj.description}")

        # ######################################
        # Query employees
        # ######################################
        employees = (
            session.execute(
                select(Employees).where(
                    or_(
                        and_(
                            Employees.position.in_(["Developer", "Tester"]),
                            Employees.salary.between(45000, 50000),
                        ),
                        and_(
                            Employees.position == "Architect",
                            Employees.salary >= 60000,
                        ),
                    )
                )
            )
            .scalars()
            .all()
        )
        print(blue.head("Employees:"))
        for emp in employees:
            print(f"ID: {emp.id}, Name: {emp.name}, Position: {emp.position}, Salary: {emp.salary}")

        # ######################################
        # Query allocations
        # ######################################
        allocations = session.execute(
            select(Allocations.project_id, Allocations.employee_id)
            .where(Allocations.project_id.in_([1]))
            .order_by(Allocations.project_id)
        ).all()
        print(green.head("Allocations:"))
        for alloc in allocations:
            print(f"Project ID: {alloc.project_id}, Employee ID: {alloc.employee_id}")
    # commits transaction, closes session


if __name__ == "__main__":
    main()
