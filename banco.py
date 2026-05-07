import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS licencas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    serial TEXT UNIQUE,
    hwid TEXT,
    ativado INTEGER DEFAULT 0,
    expiracao TEXT
)
""")

conn.commit()

print("Banco criado com sucesso")