from fastapi import FastAPI, HTTPException, Path, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List

app = FastAPI()
templates = Jinja2Templates(directory="./templates")


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


users_db = [User(id=1, name="Ivan", email="ivan@mail.ru", password="qwerty")]


@app.get("/users", response_model=List[User])
async def get_users():
    return users_db


@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int = Path(..., title="The ID of the user")):
    user = next((user for user in users_db if user.id == user_id), None)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


@app.post("/users", response_model=User)
async def create_user(user: User):
    users_db.append(user)
    return user


@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, updated_user: User):
    index = next((i for i, user in enumerate(users_db) if user.id == user_id), None)
    if index is not None:
        users_db[index] = updated_user
        return updated_user
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}", response_model=User)
async def delete_user(user_id: int):
    user = next((user for user in users_db if user.id == user_id), None)
    if user:
        users_db.remove(user)
        return user
    raise HTTPException(status_code=404, detail="User not found")


@app.get("/user_list", response_class=HTMLResponse)
async def get_user_list(request: Request):
    return templates.TemplateResponse("user_list.html", {"request": request, "users": users_db})
