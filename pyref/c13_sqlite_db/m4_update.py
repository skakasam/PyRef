"""Updating data in tables"""

import sqlite3
from contextlib import closing

from . import DATABASE


def main():
    with closing(sqlite3.connect(DATABASE)) as connection:
        with closing(connection.cursor()) as cursor:
            # Promote Charlie to Architect and change his assignment to Project Beta
            cursor.execute("UPDATE employees SET position = ?, salary = ? WHERE id = ?", ("Architect", 62000, 3))
            cursor.execute("UPDATE allocations SET project_id = ? WHERE employee_id = ?", (2, 3))
            print("Updated Charlie's position and project assignment")

            # Promote Ian to Developer and change his assignment to Project Alpha
            cursor.execute("UPDATE employees SET position = ?, salary = ? WHERE id = ?", ("Developer", 52000, 9))
            cursor.execute("UPDATE allocations SET project_id = ? WHERE employee_id = ?", (1, 9))
            print("Updated Ian's position and project assignment")

            connection.commit()


if __name__ == "__main__":
    main()
