"""Reading data from tables"""

import sqlite3
from contextlib import closing

from . import DATABASE


def main():
    with closing(sqlite3.connect(DATABASE)) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute(
                "SELECT id, name, position FROM employees WHERE position = ? AND salary > ?",
                ("Developer", 50000),
            )
            columns = [desc[0] for desc in cursor.description]
            results = cursor.fetchall()

            print("Employees:")
            for row in results:
                employee = dict(zip(columns, row))
                print(employee)


if __name__ == "__main__":
    main()
