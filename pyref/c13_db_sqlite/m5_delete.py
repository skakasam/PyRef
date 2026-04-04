"""Deleting data from tables"""

import sqlite3
from contextlib import closing

from . import DATABASE


def main():
    with closing(sqlite3.connect(DATABASE)) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("DELETE FROM employees WHERE id = ?", (10,))
            connection.commit()

            print("Deleted employee with ID 10")


if __name__ == "__main__":
    main()
