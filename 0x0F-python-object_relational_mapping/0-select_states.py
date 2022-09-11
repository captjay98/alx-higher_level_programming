#!/usr/bin/python3

import MySQLdb
from sys import argv

user = argv[1]
password = argv[2]
database = argv[3]

connection = MySQLdb.connect(
    host='localhost',
    port=3306,
    user=user,
    password=password,
    database=database)

cursor = connection.cursor()

cursor.execute("SELECT * FROM states")

db = cursor.fetchall()

for item in db:
    print(item)
