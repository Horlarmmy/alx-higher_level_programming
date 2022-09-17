#!/usr/bin/python3
"""
List all states from the db hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states;")
    states = cur.fetchall()
    for row in states:
        print(row)
    cur.close()
    conn.close()
