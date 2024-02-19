#!/usr/bin/python3
"""
List all cities from the hbtn_0e_4_usa database.

Connects to the MySQL server on localhost:3306, executes the query to fetch
cities sorted by cities.id, and prints the results. Requires MySQLdb module.
"""

import MySQLdb
import sys

def main(user, password, db_name):
    """
    Connect to the MySQL server and execute the SQL query to fetch cities.

    Args:
        user (str): The MySQL username.
        password (str): The MySQL password.
        db_name (str): The name of the database.
    """
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=password, db=db_name)
        cursor = db.cursor()
        cursor.execute("""SELECT cities.id, cities.name, states.name
                          FROM cities
                          INNER JOIN states ON cities.state_id = states.id
                          ORDER BY cities.id ASC""")
        results = cursor.fetchall()
        for row in results:
            print(row)
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"Error {e.args[0]}: {e.args[1]}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: script.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2], sys.argv[3])
