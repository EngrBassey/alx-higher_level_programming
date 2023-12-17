#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys
uargs = sys.argv[1]
pargs = sys.argv[2]
dargs = sys.argv[3]
nargs = sys.argv[4]

db = MySQLdb.connect(host="localhost", user=uargs,
                     passwd=pargs, db=dargs, port=3306)

cur = db.cursor()
query = "SELECT * FROM states  WHERE name = %s"
cur.execute(query, (nargs,))
rows = cur.fetchall()
for key in rows:
    print(key)
cur.close()
db.close()
