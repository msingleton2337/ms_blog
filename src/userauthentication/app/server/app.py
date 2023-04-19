from fastapi import FastAPI, APIRouter, Body
from app.server.database import add_user, delete_user, retrieve_users
from app.server.models.user import UserSchema, ResponseModel, ErrorResponseModel
from fastapi.encoders import jsonable_encoder


app = FastAPI()


@app.post("/", response_description="User data added into the database")
async def add_user_data(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    return ResponseModel(new_user, "User added successfully.")

# 
@app.get("/", response_description="Users retrieved")
async def get_users():
    users = await retrieve_users()
    if users:
        return ResponseModel(users, "Users data retrieved successfully")
    return ResponseModel(users, "Empty list returned")

@app.delete("/{id}", response_description="User data deleted from the database")
async def delete_user_data(id: str):
    deleted_user = await delete_user(id)
    if deleted_user:
        return ResponseModel(
            "user with ID: {} removed".format(id), "User deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "user with id {0} doesn't exist".format(id)
    )



@app.get("/api/healthchecker")
def root():
    return {"message": ""}