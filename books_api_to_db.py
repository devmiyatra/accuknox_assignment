import requests
import sqlite3

url = "https://fakerapi.it/api/v1/books?_quantity=10"
response = requests.get(url)
data = response.json()["data"]

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    year INTEGER
)
""")


for book in data:
    cursor.execute(
        "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
        (book["title"], book["author"], book["published"])
    )

conn.commit()


cursor.execute("SELECT title, author, year FROM books")
rows = cursor.fetchall()

print("Books stored in database:\n")
for row in rows:
    print(f"Title: {row[0]}")
    print(f"Author: {row[1]}")
    print(f"Year: {row[2]}")
    print("-" * 30)

conn.close()
