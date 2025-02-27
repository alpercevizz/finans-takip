import sqlite3

conn = sqlite3.connect("PYTHON/finans-takip/finans.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS gelir(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               tarih TEXT,
               tutar REAL,
               aciklama TEXT
)
 """)

cursor.execute("""
CREATE TABLE IF NOT EXISTS gider(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               tarih TEXT,
               tutar REAL,
               aciklama TEXT,
               kategori TEXT              
)
 """)

conn.commit()
conn.close()

print("Veritabanı ve tablolar başarıyla oluşturuldu!")