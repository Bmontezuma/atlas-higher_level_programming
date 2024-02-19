#!/usr/bin/python3
# Lists all states with a name starting with N from the database hbtn_0e_0_usa.
# Usage: ./1-filter_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import sys
import MySQLdb

if __name__ == "__main__":
    # Validate command-line arguments
    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py <username> <password> <db_name>")
        sys.exit(1)

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

    # Execute the query
    cur.execute("SELECT * FROM `states` ORDER BY `id`")

    # Fetch all the rows
    rows = cur.fetchall()

    # Filter and print states starting with 'N'
    [print(state) for state in rows if state[1][0] == "N"]

    # Close cursor and connection
    cur.close()
    db.close()

