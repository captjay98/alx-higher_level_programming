#!/usr/bin/python3


import MySQLdb
from sys import argv

'''
lists all states with starting name with N
from the database hbtn_0e_0_usa
'''
if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    cur = db.cursor()
    cur.execute(
            "SELECT * FROM states WHERE name LIKE\
                BINARY 'N%'ORDER BY id ASC")
    for item in cur.fetchall():
        print(item)
