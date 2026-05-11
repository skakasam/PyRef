"""Update data in the database using the SQLAlchemy ORM."""

from decimal import Decimal

from sqlalchemy import select

from . import SESSION, Allocations, Employees


def main():
    with SESSION.begin() as session:
        # 1. Promote employee with ID 3 to Architect and update salary to $65,000.00.
        emp3 = session.get(Employees, 3)
        if emp3 is None:
            raise ValueError("Employee with ID 3 not found.")
        emp3.position = "Architect"
        emp3.salary = Decimal("65000.00")

        # 2. Promote employee with ID 9 to Developer and update salary to $55,000.00.
        emp9 = session.get(Employees, 9)
        if emp9 is None:
            raise ValueError("Employee with ID 9 not found.")
        emp9.position = "Developer"
        emp9.salary = Decimal("55000.00")

        # 3. Update allocation for employee with ID 3 to project ID 2.
        alloc3 = session.scalars(
            select(Allocations).where((Allocations.employee_id == 3) & (Allocations.project_id == 1))
        ).first()
        if alloc3 is None:
            raise ValueError("Allocation for employee with ID 3 and project ID 1 not found.")
        alloc3.project_id = 2

        # 4. Update allocation for employee with ID 9 to project ID 1.
        alloc9 = session.scalars(
            select(Allocations).where((Allocations.employee_id == 9) & (Allocations.project_id == 2))
        ).first()
        if alloc9 is None:
            raise ValueError("Allocation for employee with ID 9 and project ID 2 not found.")
        alloc9.project_id = 1
    # commits transaction, closes session

    print("Employee with ID 3 promoted to Architect with a salary of $65,000.00.")
    print("Employee with ID 9 promoted to Developer with a salary of $55,000.00.")
    print("Allocation for employee with ID 3 updated to project ID 2.")
    print("Allocation for employee with ID 9 updated to project ID 1.")


if __name__ == "__main__":
    main()
