from fastapi import FastAPI, Depends # type: ignore (Pylance unresolved import)
from fastapi.responses import JSONResponse  # type: ignore (Pylance unresolved import)
from database.database import database
from database.models import songs
from app.core.mood_detection import detect_mood_from_text

# Import JSONResponse class to explicitly return JSON responses
app: FastAPI = FastAPI()    # type: ignore (FastAPI type unknown to Pylance)

# Connect to database at app startup
@app.on_event("startup")
async def startup():
    await database.connect()

# Disconnect database at app shutdown
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect

# API endpoint clearly defined to get a mood-based playlist
@app.get("/playlist/", response_class=JSONResponse)  # type: ignore (decorator type unresolved by Pylance)
async def get_playlist(user_input: str):
    # Detect user's mood from input text
    mood = detect_mood_from_text(user_input)

    # Query database for songs matching the detected mood
    query = songs.select().where(songs.c.mood == mood).limit(10)
    results = await database.fetch_all(query)

    # Prepare and return playlist response clearly
    playlist = [{"id": result["id"], "title": result["title"], "artist": result["artist"]} for result in results]
    
    return {"mood": mood, "playlist": playlist}
