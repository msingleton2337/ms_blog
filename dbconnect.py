import motor.motor_asyncio


MONGODB_URL="mongodb://admin:password123@localhost:27017/?authSource=admin"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
userCollection = client.fastapi.users

document = {'username': 'user1','password': 'pass1'}
result = userCollection.insert_one(document)

async def f():
    async for doc in await userCollection.find():
        print(doc)


f()