"""Delete data in the database using the SQLAlchemy ORM."""

from sqlalchemy import delete

from . import SESSION, Employees


def main():
    with SESSION.begin() as session:
        deleted_employees = (
            session.execute(delete(Employees).where(Employees.name == "Jane Doe").returning(Employees)).scalars().all()
        )
        deleted_ids = [emp.id for emp in deleted_employees]
    # commits transaction, closes session

    if deleted_employees:
        print(f"Deleted employee(s) with name 'Jane Doe': {deleted_ids}")
    else:
        print("No employee with name 'Jane Doe' found to delete.")


if __name__ == "__main__":
    main()
