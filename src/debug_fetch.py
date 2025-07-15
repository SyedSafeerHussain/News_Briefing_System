import sqlite3
import os

# ✅ Path to your DB
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'news.db')

# ✅ Connect and read
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("SELECT title, summary, source, url, published_at, fetched_at FROM headlines ORDER BY published_at DESC")
rows = cursor.fetchall()

for row in rows:
    print("📰 Title:", row[0])
    print("🧠 Summary:", row[1])
    print("📡 Source:", row[2])
    print("🔗 URL:", row[3])
    print("🕒 Published:", row[4])
    print("📥 Fetched:", row[5])
    print("="*50)

conn.close()
