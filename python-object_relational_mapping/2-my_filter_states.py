#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb


def main():
    """
    Main function to retrieve and display states from the database.
    """
    # Retrieving MySQL credentials and search query from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search_query = sys.argv[4]

    # Connecting to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Creating a cursor object using cursor() method
    cursor = db.cursor()

    # Executing SQL query to select states matching the search query
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cursor.execute(query, (search_query,))

    # Fetching all rows from the result set
    rows = cursor.fetchall()

    # Displaying results
    for row in rows:
        print(row)

    # Closing cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
