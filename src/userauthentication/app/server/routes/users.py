from app.server.database import add_user, delete_user, retrieve_users, retrieve_user, update_user, user_helper
from app.server.models.user import UserSchema, ResponseModel, ErrorResponseModel, UpdateUserModel
from fastapi import APIRouter, Body


router = APIRouter()

@router.post("/", response_description="User data added into the database")
async def add_user_data(user: UserSchema = Body(...)):
    new_user = await add_user(dict(user))
    return ResponseModel(new_user, "User added successfully.")

@router.get("/", response_description="Users retrieved")
async def get_users():
    users = await retrieve_users()
    if users:
        return ResponseModel(users, "Users data retrieved successfully")
    return ResponseModel(users, "Empty list returned")

@router.get("/{userId}", response_description="User data retrieved")
async def get_user_data(id):
    user = await retrieve_user(id)
    if user:
        return ResponseModel(user, "User data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "User doesn't exist.")

@router.put("/{userId}")
async def update_user_data(id: str, req: UpdateUserModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await update_user(id, req)
    if updated_user:
        return ResponseModel(
            "User with ID: {} Update is successful".format(id),
            "User updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the user data.",
    )

@router.delete("/{userId}", response_description="User data deleted from the database")
async def delete_user_data(id: str):
    deleted_user = await delete_user(id)
    if deleted_user:
        return ResponseModel(
            "user with ID: {} removed".format(id), "User deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "user with id {0} doesn't exist".format(id)
    )