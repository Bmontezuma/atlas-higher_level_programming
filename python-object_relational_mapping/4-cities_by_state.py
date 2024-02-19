#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
"""


import sys
import MySQLdb

def main():
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

    # Execute the query to select cities
    cur.execute(
        "SELECT `id`, `name`, (SELECT `name` FROM `states` "
        "WHERE `cities`.`state_id` = `states`.`id`) AS `state_name` "
        "FROM `cities` ORDER BY `id`"
    )

    # Fetch all the rows
    rows = cur.fetchall()

    # Print the results
    if rows:
        [print(city) for city in rows]
    else:
        print("Empty")

    # Close cursor and connection
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
