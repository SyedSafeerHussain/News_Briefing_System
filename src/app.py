from flask import Flask, render_template
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

app = Flask(__name__, template_folder=TEMPLATE_DIR)

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'news.db')

@app.route("/")
def index():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT title, summary, source, url, published_at, fetched_at
        FROM headlines
        ORDER BY fetched_at DESC
        LIMIT 20
    """)
    rows = cursor.fetchall()

    # Prepare data cleanly
    headlines = []
    for row in rows:
        headlines.append({
            "title": row[0],
            "summary": row[1],
            "source": row[2] if row[2] else None,
            "url": row[3],
            "published_at": row[4] if row[4] else None,
            "fetched_at": row[5]
        })

    conn.close()
    return render_template("index.html", headlines=headlines)

if __name__ == "__main__":
    app.run(debug=True)
