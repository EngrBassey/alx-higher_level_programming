#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys
uargs = sys.argv[1]
pargs = sys.argv[2]
dargs = sys.argv[3]

db = MySQLdb.connect(host="localhost", user=uargs,
                     passwd=pargs, db=dargs, port=3306)

cur = db.cursor()
cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
            INNER JOIN states ON states.id=cities.state_id""")
rows = cur.fetchall()
for key in rows:
    print(key)
cur.close()
db.close()
