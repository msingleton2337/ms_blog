from fastapi import FastAPI
from app.server.routes.users import router as UserRouter

app = FastAPI()

app.include_router(UserRouter, tags=["Users"], prefix="/users")

@app.get("/api/healthchecker")
def root():
    return {"message": ""}