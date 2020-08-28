import sqlite3
import sys


conn = sqlite3.connect('food.sqlite')
curs = conn.cursor()

query = 'SELECT * FROM Food WHERE ' + sys.argv[1]
print(query)
curs.execute(query)
print(curs.description)
names = [f[0] for f in curs.description]
for row in curs.fetchall():
    print(row)
    for pair in zip(names, row):
        print('{}: {}'.format(*pair))
    print()
