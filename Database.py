import sqlite3
import sys

db = sqlite3.connect("mydatabase.db") 
sql = db.cursor()
 
sql.execute ("""CREATE TABLE IF NOT EXISTS  users (
            current score BIGINT, 
            best result BIGINT,
            username TEXT,
            average score BIGINT,
            time best score BIGINT
            )""")


db.commit()

username = input('Username:  ')

sql.execute('SELECT username FROM users')
if sql.fetchone() is None:
    sql.execute (f"INSERT INTO users VALUES (?, ?, ?, ?, ?)", (0, 0, username, 0, 0) )
    db.commit()

    print("Oh, yeah!")
else:
    print('This nickname already exists.')

for value in sql.execute("SELECT * FROM users"):
    print(value)


