from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Mood Playlist API is running!"}
