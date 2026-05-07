import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS licencas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    serial TEXT,
    hwid TEXT,
    ativo INTEGER DEFAULT 0,
    expiracao TEXT
)
""")

serial = "TELTEC-2026-RESET-9X2A"

cursor.execute("""
INSERT INTO licencas (
    serial,
    expiracao
)
VALUES (?, ?)
""", (serial, "2026-12-31"))

conn.commit()

print("BANCO TELTEC OK")
print("Licença adicionada")