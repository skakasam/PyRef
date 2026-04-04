"""Intro to DB Access using Python."""

import sqlite3
from contextlib import closing

from . import DATABASE


def main():
    with closing(sqlite3.connect(DATABASE)) as connection:
        with closing(connection.cursor()) as cursor:
            print("Connected to the database and created a cursor")

            print("Dropping and recreating the projects table")
            cursor.execute("DROP TABLE IF EXISTS projects")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS projects (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT
                )
            """)

            print("Dropping and recreating the employees table")
            cursor.execute("DROP TABLE IF EXISTS employees")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    dob TEXT NOT NULL,
                    position TEXT NOT NULL,
                    salary REAL NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    CONSTRAINT salary_positive CHECK (salary > 0),
                    CONSTRAINT email_format CHECK (email LIKE '%_@__%.__%'),
                    CONSTRAINT dob_valid CHECK (dob GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
                    CONSTRAINT position_check CHECK (position IN ('Manager', 'Architect', 'Developer', 'Tester', 'Support', 'Intern'))
                )
            """)

            print("Dropping and recreating the allocations table")
            cursor.execute("DROP TABLE IF EXISTS allocations")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS allocations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    employee_id INTEGER NOT NULL,
                    project_id INTEGER NOT NULL,
                    CONSTRAINT fk_employee FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE,
                    CONSTRAINT fk_project FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
                )
            """)

            print("Committing changes to the database")
            connection.commit()


if __name__ == "__main__":
    main()
