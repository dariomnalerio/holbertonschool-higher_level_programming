#!/usr/bin/python3
"""5-filter_cities"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    """
    takes in the name of a state as an argument
    and lists all cities of that state
    """

    state_name = argv[4]

    db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    cur = db.cursor()
    cur.execute("""
        SELECT DISTINCT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
    """, (state_name,))
    results = cur.fetchall()

    print(', '.join(row[0] for row in results))
