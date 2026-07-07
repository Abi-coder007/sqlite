import sqlite3

conn = sqlite3.connect("student.db")  # sqlite3, not sqlite

cursor = conn.cursor()  # conn, not onn

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER,
    name TEXT,
    mark INTEGER
)
""")

cursor.execute(
    "INSERT INTO students VALUES (?, ?, ?)",
    (1, "Abishek", 90)
)

conn.commit()

cursor.execute("SELECT * FROM students")

print(cursor.fetchall())

conn.close()