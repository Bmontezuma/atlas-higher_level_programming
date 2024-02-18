#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb


def main():
    """
    Main function to retrieve and display cities from the database for a given state.
    """
    # Retrieving MySQL credentials and state name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connecting to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Creating a cursor object using cursor() method
    cursor = db.cursor()

    # Executing SQL query to select cities of the given state
    query = """
            SELECT GROUP_CONCAT(cities.name ORDER BY cities.id SEPARATOR ', ')
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            """
    cursor.execute(query, (state_name,))

    # Fetching the result
    result = cursor.fetchone()[0]

    # Displaying results
    if result:
        print(result)
    else:
        print("No cities found for the given state.")

    # Closing cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
