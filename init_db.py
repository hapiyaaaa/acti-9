import sqlite3

conn = sqlite3.connect("students.db")

conn.execute("DROP TABLE IF EXISTS students")
conn.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT NOT NULL,
    name TEXT NOT NULL,
    program TEXT NOT NULL,
    year INTEGER NOT NULL,
    section TEXT NOT NULL,
    source TEXT DEFAULT 'Local'
)
""")

students = [
    ("2026-0001", "Sharmaine Joyce Palencia", "BSIT", 3, "B", "Local"),
    ("2026-0002", "Jero Paca-oncis", "BSIT", 3, "B", "Local"),
    ("2026-0003", "Missy Miranda", "BSIT", 3, "B", "Local"),
    ("2026-0004", "Ana Garcia", "BSIT", 3, "A", "Local"),
    ("2026-0005", "Mark Lopez", "BSIT", 3, "A", "Local"),
]

conn.executemany(
    """INSERT INTO students (student_id, name, program, year, section, source)
    VALUES (?, ?, ?, ?, ?, ?)""",
    students,
)

conn.commit()
conn.close()

print("Database initialized successfully!")
print(f"{len(students)} Local student records inserted.")
