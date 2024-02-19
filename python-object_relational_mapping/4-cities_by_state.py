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
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connecting to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Creating a cursor object using cursor() method
    cursor = db.cursor()

    # Executing SQL query to select all cities with corresponding state names
    query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id
            """
    cursor.execute(query)

    # Fetching all rows from the result set
    rows = cursor.fetchall()

    # Displaying results
    if not rows:
        print("No cities found in the database.")
    else:
        for row in rows:
            print(row)

    # Closing cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
