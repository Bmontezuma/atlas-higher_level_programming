#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb


def main():
    """
    Main function to retrieve and display states from the database.
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

    # Executing SQL query to select states starting with 'N'
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id"
    cursor.execute(query)

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
