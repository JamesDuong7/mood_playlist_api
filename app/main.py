from fastapi import FastAPI # type: ignore (Pylance unresolved import)
from fastapi.responses import JSONResponse  # type: ignore (Pylance unresolved import)

# Import JSONResponse class to explicitly return JSON responses
app: FastAPI = FastAPI()    # type: ignore (FastAPI type unknown to Pylance)

# Define the root endpoint ("/") for your API
@app.get("/", response_class=JSONResponse)  # type: ignore (decorator type unresolved by Pylance)
async def root() -> dict[str, str]:
    """
    Root endpoint of the API.
    Returns a simple JSON message indicating the API is running.
    """
    return {"message": "Hello, World!"}
