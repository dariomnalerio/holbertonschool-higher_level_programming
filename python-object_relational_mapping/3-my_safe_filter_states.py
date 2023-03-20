#!/usr/bin/python3
""" 3-my_safe_filter_states """
from sys import argv
import MySQLdb


if __name__ == "__main__":
    """
    takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument
    and is safe from MySQL injections
    """

    state_name = argv[4]

    db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s", (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
