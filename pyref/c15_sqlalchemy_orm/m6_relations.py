"""Use relationships in SQLAlchemy ORM"""

from datetime import date

from sqlalchemy import select

from . import SESSION, Allocations, Employees, Projects


def main():
    gamma_project: Projects = Projects(
        name="Project Gamma",
        description="Gamma project description",
    )
    gamma_employee_1: Employees = Employees(
        name="Kate Wright",
        dob=date(1985, 6, 15),
        position="HR",
        salary=50000,
        email="kate.wright@example.com",
    )
    gamma_employee_2: Employees = Employees(
        name="Liam Brown",
        dob=date(1990, 9, 20),
        position="HR",
        salary=45000,
        email="liam.brown@example.com",
    )

    with SESSION.begin() as session:
        # Add project and employees to the session
        session.add(gamma_project)
        session.add_all([gamma_employee_1, gamma_employee_2])
        session.flush()  # Ensure IDs are generated

        # Create allocations using relationships
        alloc1 = Allocations(employee_id=gamma_employee_1.id, project_id=gamma_project.id)
        alloc2 = Allocations(employee_id=gamma_employee_2.id, project_id=gamma_project.id)
        session.add_all([alloc1, alloc2])
    # commits transaction, closes session

    with SESSION.begin() as session:
        # Query the project and its employees using relationships
        project = session.execute(select(Projects).where(Projects.name == "Project Gamma")).scalar_one()
        print(f"Project: {project.name}, Description: {project.description}")

        employees: list[Employees] = [alloc.employee for alloc in project.allocations]
        print("Employees allocated to this project:")
        for emp in employees:
            print(f"ID: {emp.id}, Name: {emp.name}, Position: {emp.position}, Salary: {emp.salary}")

        if employees:
            employee_to_delete = employees[0]
            session.delete(employee_to_delete)  # Delete the first employee allocated to the project
            print(f"Deleted employee: {employee_to_delete.name} (ID: {employee_to_delete.id})")
    # commits transaction, closes session

    print("Done!")


if __name__ == "__main__":
    main()
