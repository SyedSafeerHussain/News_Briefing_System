from flask import Flask,render_template
import sqlite3
import os
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'))

def get_all_headlines():
    conn=sqlite3.connect("data/news.db")
    cursor=conn.cursor()
    cursor.execute("SELECT title, url, fetched_at FROM headlines ORDER BY id DESC LIMIT 50;")
    rows=cursor.fetchall()
    conn.close()
    return rows
@app.route("/")
def index():
    headlines=get_all_headlines()
    return render_template("index.html", headlines=headlines)
if __name__=="__main__":
    app.run(debug=True)

