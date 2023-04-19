import motor.motor_asyncio
from bson.objectid import ObjectId

MONGODB_URL="mongodb://admin:password123@localhost:27017/?authSource=admin"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = client.fastapi
user_collection = db.get_collection("users")

# helper function for parsing the results from a database query into a Python dict.
def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "password": user["password"],
         "email": user["email"],
    }

# Retrieve all users present in the database
async def retrieve_users():
    users = []
    async for user in user_collection.find():
        users.append(user_helper(user))
    return users

# Add a new user into to the database
async def add_user(user_data: dict) -> dict:
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)

# Delete a user from the database
async def delete_user(id: str):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(id)})
        return True

