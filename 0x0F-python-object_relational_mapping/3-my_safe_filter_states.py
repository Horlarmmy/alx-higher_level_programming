#!/usr/bin/python3
"""
 write a script that takes in arguments and displays
 all values in the states table of hbtn_0e_0_usa where
 name matches the argument. But this time, write one
 that is safe from MySQL injections!
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name\
                    LIKE %s ORDER BY id ASC", (argv[4], ))
    rows = cursor.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    db.close()
