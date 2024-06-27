import sqlite3

conn = sqlite3.connect("entrance.db")

cursor = conn.cursor()

cursor.execute("INSERT INTO Seller (login, password, age) VALUES (?,?,?)",("я","12",19))

conn.commit()

cursor.close()
conn.close()