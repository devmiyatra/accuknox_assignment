import csv
import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
""")

with open("users.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (row["name"], row["email"])
        )

conn.commit()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("Users stored in database:\n")
for row in rows:
    print(row)

conn.close()
