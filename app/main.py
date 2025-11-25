from fastapi import FastAPI

app = FastAPI()

users = []


@app.get("/")
async def get_root():
    return {
        "status": "API is running",
        "message": "Welcome to the FastAPI application!",
    }


# post api for create user
@app.post("/users")
async def create_user(
    name: str,
    email: str,
    password: str,
):
    users.append(
        {"id": len(users) + 1, "name": name, "email": email, "password": password}
    )
    return {"status": "succes", "data": users[len(users) - 1]}


# get method for get user by id
@app.get("/users/{user_id}")
async def get_user_by_id(user_id: int):
    return {"status": "success", "data": users[user_id - 1]}


# get method for get all users
@app.get("/users")
async def get_all_users():
    return {"status": "success", "data": users}


# put method for update user by id
@app.put("users/{user_id}")
async def update_user(
    user_id: int,
    name: str,
    email: str,
    password: str,
):
    users[user_id - 1]["name"] = name
    users[user_id - 1]["email"] = email
    users[user_id - 1]["password"] = password

    return {
        "status": "success",
        "data": users[user_id - 1],
    }


# patch method for update user
@app.patch("/users/{user_id}")
async def patch_user(
    user_id: int,
    name: str,
    email: str,
):
    users[user_id - 1]["email"] = email
    users[user_id - 1]["name"] = name

    return {
        "status": "success",
        "data": users[user_id - 1],
    }


# delete method for delete user
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):

    users.remove(users[user_id - 1])

    return {"status": "success", "data": None, "message": "user deleted successfully"}
