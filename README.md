# Mood-Based Playlist API

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-green?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-orange?logo=streamlit)](https://streamlit.io/)

> A modern, end-to-end music playlist service using FastAPI, AI/ML (HuggingFace Transformers), SQLAlchemy, SQLite, and Streamlit.  
> **Describe your mood in plain English. Instantly get a randomized playlist matching your vibe.**

---

## Features

- NLP-powered mood detection (HuggingFace Transformers)
- Randomized playlist for every request
- Streamlit frontend for easy user interaction
- FastAPI backend for quick, async API responses
- SQLAlchemy + SQLite database for song storage
- Simple setup scripts for database and data import

---

## Tech Stack

- Python 3.9+
- FastAPI
- SQLAlchemy
- HuggingFace Transformers
- Streamlit
- SQLite

---

## Quickstart

1. **Clone the repository and set up the environment**
    ```bash
    git clone https://github.com/JamesDuong7/mood_playlist_api
    cd mood_playlist_api
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    ```

2. **Create and seed the database**
    ```bash
    python scripts/create_tables.py
    python scripts/load_data.py
    ```

3. **Run the FastAPI backend**
    ```bash
    uvicorn app.main:app --reload
    # API docs at http://localhost:8000/docs
    ```

4. **Run the Streamlit frontend (in a new terminal)**
    ```bash
    streamlit run frontend.py
    # App at http://localhost:8501
    ```

---

## API Documentation

**GET /playlist/**  
Generate a randomized playlist based on a user's mood.

**Query Parameters:**
- `user_input` (str): Free text describing mood (e.g. "I feel happy today")
- `limit` (int, optional): Number of songs to return (default: 10, max: 30)

**Example:**
````
GET /playlist/?user\_input=I%20feel%20energetic\&limit=5
````

**Response:**
```json
{
  "mood": "energetic",
  "playlist": [
    { "id": 1, "title": "Blinding Lights", "artist": "The Weeknd" },
    { "id": 4, "title": "Lose Yourself", "artist": "Eminem" }
  ]
}
````

---

## Project Structure

```
mood_playlist_api/
│
├── app/
│   ├── main.py
│   └── core/
│       └── mood_detection.py
├── database/
│   ├── database.py
│   ├── models.py
│   └── database.db
├── scripts/
│   ├── create_tables.py
│   └── load_data.py
├── data/
│   └── music_data.csv
├── frontend.py
├── requirements.txt
├── .gitignore
└── env/
```

---

## Example Usage

1. Start backend and frontend as above.
2. In your browser:

   * Enter your mood in the Streamlit web app
   * Choose how many songs you want
   * Click **Get Playlist**
   * Instantly see a randomized playlist matching your mood

---

## Customization & Extensibility

* Add new moods or an advanced emotion model
* Connect to external music APIs (Spotify, YouTube, etc.)
* Add user authentication and playlist saving
* Deploy to cloud (Render, Railway, Streamlit Cloud)

---

## License

MIT — Free for personal, demo, or educational use.

