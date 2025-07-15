import sqlite3
from sqlite3 import Connection
from datetime import datetime
from typing import List,Dict
import os
DB_PATH="data/news.db"

def get_connection()->Connection:
    """Connects to the SQLite database (and creates the file if needed)."""
    conn=sqlite3.connect(DB_PATH)
    return conn
def init_db():
    DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'news.db')
    conn = sqlite3.connect(DB_PATH)
    """Creates the headlines table if it doesn’t already exist."""
    cursor=conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS headlines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            summary TEXT,
            source TEXT,
            url TEXT,
            published_at TEXT,
            fetched_at TEXT
        )
    ''')
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
                "INSERT INTO headlines (title, url, source, published_at, fetched_at) VALUES (?,?,?,?,?)",
                (
                    item["title"],
                    item["url"],
                    item.get("source", "Unknown"),
                    item.get("publishedAt", "Unknown"),
                    now
                )
                
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