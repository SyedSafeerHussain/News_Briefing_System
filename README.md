## 🧠 AI -Powered News Briefing & Alert System

> Get the world’s top headlines, auto-summarized with AI, stored in a database, and visualized on a sleek dashboard — all in one intelligent pipeline.

---

### 📌 Table of Contents

* [🔍 Project Overview](#-project-overview)
* [🚀 Features](#-features)
* [🧰 Tech Stack](#-tech-stack)
* [🗂️ Folder Structure](#-folder-structure)
* [⚙️ Setup Instructions](#-setup-instructions)
* [💻 How It Works](#-how-it-works)
* [🌐 Live Dashboard Preview](#-live-dashboard-preview)
* [🎯 Future Upgrades](#-future-upgrades)
* [📜 License](#-license)

---

### 🔍 Project Overview

This project is an **AI-powered pipeline** that:

* Fetches **top news headlines** from around the world using **NewsAPI**
* Automatically generates **short summaries** using a transformer-based summarizer
* Stores the data in a **SQLite database**
* Displays everything on a clean **Flask dashboard**

Perfect for:

* Real-time dashboards
* Custom news monitoring
* Resume projects or freelance gigs involving AI, APIs, automation, and dashboards

---

### 🚀 Features

📅 Fetches latest news headlines
🔧 Uses **HuggingFace Transformers** to auto-summarize news
🌐 Smartly handles duplicate entries
📂 Stores data with timestamps (fetched/published)
📄 Simple yet responsive Flask dashboard
📝 Modular Python files for clean architecture

---

### 🧰 Tech Stack

| Layer         | Tools / Libraries                       |
| ------------- | --------------------------------------- |
| Language      | Python 3                                |
| APIs          | [NewsAPI.org](https://newsapi.org/)     |
| AI Model      | `distilbart-cnn-12-6` (via HuggingFace) |
| Web Framework | Flask                                   |
| Database      | SQLite                                  |
| Frontend      | HTML + Bootstrap                        |
| Environment   | `python-dotenv` for secrets             |

---

### 🗂️ Folder Structure

```
news_briefing_system/
│
├── data/               # SQLite DB lives here
│   └── news.db
│
├── src/                # All main source code
│   ├── app.py          # Flask app
│   ├── main.py         # Main pipeline trigger
│   ├── db.py           # DB init & insert logic
│   ├── summarizer.py   # AI summarizer
│   └── fetch_headlines.py  # NewsAPI fetcher
│
├── templates/          # HTML dashboard
│   └── index.html
│
├── .env                # Your NewsAPI key (not pushed to GitHub)
└── README.md           # This file
```

---

### ⚙️ Setup Instructions

1. **Clone the repo**

   ```bash
   git clone https://github.com/your-username/news_briefing_system.git
   cd news_briefing_system
   ```

2. **Set up virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Set your API key in `.env`**

   ```
   NEWS_API_KEY=your_newsapi_key_here
   ```

4. **Run the main pipeline**

   ```bash
   python src/main.py
   ```

5. **Run the Flask dashboard**

   ```bash
   python src/app.py
   ```

---

### 💻 How It Works

1. `main.py` runs the whole flow:

   * Initializes database
   * Fetches headlines from NewsAPI
   * Inserts them into SQLite with timestamp
   * Summarizes them via HuggingFace model
2. `app.py` starts a Flask server and loads data from the DB
3. `index.html` renders it beautifully on a dashboard

---

### 🌐 Live Dashboard Preview

Sample UI:

```text
🧠 AI -Powered News Briefing

Title: Major fire hits downtown factory
Summary: A massive blaze engulfed the industrial zone this morning...
📱 Source: BBC   |   🕒 Published: 2025-07-14
📥 Fetched: 2025-07-15T05:11:03
```

---

### 🎯 Future Upgrades

📧 Add email/Telegram alerts for custom topics
🔄 Add filters by date, keyword, or category
📆 Use PostgreSQL for production-level storage
🔌 Add cron job to schedule fetch+summarize daily
😐 Add sentiment analysis per headline
🚀 Deploy dashboard on Render or Railway

---

### 📜 License

This project is for educational and portfolio purposes. Feel free to use and improve it, but give proper credits when sharing publicly. 🤝
