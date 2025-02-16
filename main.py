"""
Main app file
"""

from fastapi import FastAPI

from src.users.routes import users_router

app = FastAPI()


@app.get("/")
async def root():
    """
    Root route
    """

    return {"message": "Hello World"}


app.include_router(users_router, tags=["users"])
