import sqlite3

dbfile = 'C:/Users/vivek/PyCharmProjects/migradoc/md_app/site.db'
conn = sqlite3.connect(dbfile)

cur = conn.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(f"Table Name : {cur.fetchall()}")

conn.close()
