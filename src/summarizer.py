from transformers import pipeline
import sqlite3
import time
import os

# 📌 Connect to your existing DB
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'news.db')
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# 🔁 Load the summarization pipeline
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def generate_summary(text):
    try:
        result = summarizer(text, max_length=50, min_length=15, do_sample=False)
        return result[0]['summary_text'].strip()
    except Exception as e:
        print(f"❌ Error generating summary: {e}")
        return None

def summarize_all():
    # ✅ Ensure "summary" column exists
    cursor.execute("PRAGMA table_info(headlines)")
    columns = [col[1] for col in cursor.fetchall()]
    if "summary" not in columns:
        cursor.execute("ALTER TABLE headlines ADD COLUMN summary TEXT")  # Fixed typo: ALERT → ALTER

    # 🔍 Select headlines without summary
    cursor.execute("SELECT id, title FROM headlines WHERE summary IS NULL")
    rows = cursor.fetchall()

    for id, title in rows:
        print(f"🧠 Summarizing: {title}")
        summary = generate_summary(title)
        if summary:
            cursor.execute("UPDATE headlines SET summary = ? WHERE id = ?", (summary, id))
            conn.commit()
            print(f"✅ Summary stored for ID {id}")
        time.sleep(1)

    conn.close()

# Optional direct run
if __name__ == "__main__":
    summarize_all()
