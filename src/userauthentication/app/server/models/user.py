from pydantic import BaseModel, EmailStr, Field

# Schema for how User datat will be stored in the MongoDB database.
class UserSchema(BaseModel):
    username: str = Field(...)
    password: str = Field(...)
    email: EmailStr = Field(...)

# Schema for a valid(desired) response
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }    

# Schema for error response 
def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}