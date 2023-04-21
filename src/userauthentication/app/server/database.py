import motor.motor_asyncio
from bson.objectid import ObjectId

MONGODB_URL="mongodb://admin:password123@localhost:27017/?authSource=admin"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = client.fastapi
user_collection = db.get_collection("users")


def user_helper(user) -> dict:
    '''Helper function for parsing the results from a database query into a Python dict.'''
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "password": user["password"],
        "email": user["email"],
        "role": user["role"],
    }


async def retrieve_users():
    '''Retrieve all users present in the database'''
    users = []
    async for user in user_collection.find():
        users.append(user_helper(user))
    return users


async def add_user(user_data: dict) -> dict:
    '''Add a new user into to the database'''
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)

async def delete_user(id: str):
    '''Delete a user from the database'''
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(id)})
        return True
    
async def retrieve_user(id: str) -> dict:
    '''Retrieve a user with a matching ID'''
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)

async def update_user(id: str, data: dict):
    '''Update a user with a matching ID'''
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await user_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_user:
            return True
        return False


