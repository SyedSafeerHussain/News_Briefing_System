import sys
import os
from datetime import datetime

from fetch_headlines import get_top_headlines
from db import init_db, insert_headlines
from summarizer import summarize_all
def main():
    # 1. Initialize database (if not already)
    init_db()

    # 2. Fetch top headlines
    try:
        headlines=get_top_headlines(country='us',page_size=10)
    except Exception as e:
        print(f"[{datetime.utcnow().isoformat()}] ERROR fetching headlines: {e}")
        sys.exit(1)
    # 3. Insert into DB and count new entries
    new_count=insert_headlines(headlines)
    # 4. Log results
    timestamp=datetime.utcnow().isoformat()
    if new_count >0:
        print(f"[{timestamp}] Inserted {new_count} new headline(s).")
    else:
        print(f"[{timestamp}] No new headlines to insert.")


    # 5. Summarize all
    summarize_all()
if __name__=="__main__":
    main()