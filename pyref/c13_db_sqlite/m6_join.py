"""Joining tables"""

import sqlite3
from contextlib import closing

from . import DATABASE


def main():
    with closing(sqlite3.connect(DATABASE)) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute(
                """
                SELECT
                   	e.name AS 'employee',
                   	e.position
                FROM
                   	allocations a
                    INNER JOIN projects p ON a.project_id = p.id
                    INNER JOIN employees e ON a.employee_id = e.id
                WHERE
                   	p.id = ?
                ORDER BY
                   	e.id;
                """,
                (2,),
            )

            columns = [desc[0] for desc in cursor.description]
            results = cursor.fetchall()

            print("Employees allocated to Project Beta:")
            for row in results:
                allocation = dict(zip(columns, row))
                print(allocation)


if __name__ == "__main__":
    main()
