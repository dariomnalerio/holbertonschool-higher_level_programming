#!/usr/bin/python3
""" 2-my_filter_states module"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    """
    takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument
    """

    state_name = argv[4]

    db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    cur = db.cursor()
    cur.execute(f"SELECT * FROM states WHERE name LIKE BINARY '{state_name}' \
                ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
