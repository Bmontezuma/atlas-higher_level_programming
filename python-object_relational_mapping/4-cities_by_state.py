#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state.
"""

import sys
import MySQLdb


def main():
    """
    Main function to retrieve and display cities for a given state.
    """
    # Retrieving MySQL credentials and state name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connecting to MySQL server
    db = MySQLdb.connect(user=username, passwd=password, db=database)

    # Creating a cursor object using cursor() method
    cursor = db.cursor()

    # Executing SQL query to select all cities for the given state
    query = """
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id
            """
    cursor.execute(query, (state_name,))

    # Fetching all rows from the result set
    rows = cursor.fetchall()

    # Extracting city names from the rows
    cities = [row[0] for row in rows]

    # Displaying results
    if cities:
        print(", ".join(cities))
    else:
        print()

    # Closing cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
