#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    # Retrieving MySQL credentials from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connecting to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Creating a cursor object using cursor() method
    cursor = db.cursor()

    # Executing SQL query to select all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id")

    # Fetching all rows from the result set
    rows = cursor.fetchall()

    # Displaying results
    for row in rows:
        print(row)

    # Closing cursor and database connection
    cursor.close()
    db.close()
