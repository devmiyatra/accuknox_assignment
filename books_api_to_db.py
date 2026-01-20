import requests
import sqlite3

# Step 1: Fetch data from API
url = "https://fakerapi.it/api/v1/books?_quantity=10"
response = requests.get(url)
data = response.json()["data"]

# Step 2: Create SQLite database
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

# Step 3: Insert data into database
for book in data:
    cursor.execute(
        "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
        (book["title"], book["author"], book["published"])
    )

conn.commit()

# Step 4: Display stored data
cursor.execute("SELECT title, author, year FROM books")
rows = cursor.fetchall()

print("Books stored in database:\n")
for row in rows:
    print(f"Title: {row[0]}")
    print(f"Author: {row[1]}")
    print(f"Year: {row[2]}")
    print("-" * 30)

conn.close()
