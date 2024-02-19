#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb


def main():
    """
    Main function to retrieve and display cities from the database.
    """
    # Retrieving MySQL credentials from command line arguments
    username, password, database = sys.argv[1:4]

    # Connecting to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Creating a cursor object using cursor() method
    cursor = db.cursor()

    # Executing SQL query to select all cities
    query = """
            SELECT id, name,
                   (SELECT name
                    FROM states
                    WHERE cities.state_id = states.id) AS state_name
            FROM cities
            ORDER BY id
            """
    cursor.execute(query)

    # Fetching all rows from the result set
    rows = cursor.fetchall()

    # Displaying results
    if rows:
        for row in rows:
            print(row)
    else:
        print("No cities found.")

    # Closing cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
