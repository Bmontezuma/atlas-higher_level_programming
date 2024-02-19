#!/usr/bin/python3
"""Displays all values in the states table where name matches the argument."""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Create a cursor object
    cur = db.cursor()

    # Create SQL query using format with user input
    sql_query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(sys.argv[4])

    # Execute the query
    cur.execute(sql_query)

    # Fetch all the rows
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
