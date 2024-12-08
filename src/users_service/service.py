from fastapi import FastAPI, HTTPException
from typing import List

from .models import User

app = FastAPI()

# Simulated database
users_db = [
    User(id=1, username="john_doe", email="john@example.com", full_name="John Doe"),
    User(id=2, username="jane_doe", email="jane@example.com", full_name="Jane Doe")
]

@app.get("/users/", response_model=List[User])
async def get_users():
    return users_db

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    user = next((user for user in users_db if user.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user 