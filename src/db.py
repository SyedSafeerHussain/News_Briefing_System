import sqlite3
from sqlite3 import Connection
from datetime import datetime
from typing import List,Dict
DB_PATH="data/news.db"

def get_connection()->Connection:
    """Connects to the SQLite database (and creates the file if needed)."""
    conn=sqlite3.connect(DB_PATH)
    return conn
def init_db():
    """Creates the headlines table if it doesn’t already exist."""
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS headlines (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            title       TEXT NOT NULL,
            url         TEXT NOT NULL UNIQUE,
            fetched_at  TEXT NOT NULL
        );
    """)
    conn.commit()
    conn.close()
def insert_headlines(items: List[Dict[str,str]])->int:
    """
    Inserts a list of headlines into the DB.
    Skips any with duplicate URLs.
    Returns the count of newly inserted rows.
    """
    conn=get_connection()
    cursor=conn.cursor()
    new_count=0
    now=datetime.utcnow().isoformat()
    for item in items:
        try:
            cursor.execute(
                "INSERT INTO headlines (title, url, fetched_at) VALUES (?, ?, ?)",
                (item["title"],item["url"],now)
            )
            new_count+=1
        except sqlite3.IntegrityError:
            # URL already exists, skip
            continue
    conn.commit()
    conn.close()
    return new_count
if __name__=="__main__":
    init_db()
    sample=[
        {"title": "Test Headline 1", "url": "https://example.com/1"},
        {"title": "Test Headline 2", "url": "https://example.com/2"},
    ]
    count=insert_headlines(sample)
    print(f"Inserted {count} new headlines.")