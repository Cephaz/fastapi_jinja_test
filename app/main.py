from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """health check endpoint

    Returns:
        str: welcome message
    """
    return {"message": "Welcome to FastAPI!"}
