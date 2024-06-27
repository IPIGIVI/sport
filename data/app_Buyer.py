import sqlite3

conn = sqlite3.connect("entrance.db")

cursor = conn.cursor()

cursor.execute("INSERT INTO Buyer (login, password, age,gender) VALUES (?,?,?,?)",("я","12",19,"man"))

conn.commit()

cursor.close()
conn.close()