from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class UserSchema(BaseModel):
    '''Schema for User data'''
    username: str = Field(...)
    password: str = Field(...)
    email: EmailStr = Field(...)
    role: str = Field(...)


class UpdateUserModel(BaseModel):
    username: Optional[str]
    password: Optional[str]
    email: Optional[EmailStr]
    role: Optional[str]

def ResponseModel(data, message):
    '''Schema for a valid(desired) response'''
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }    


def ErrorResponseModel(error, code, message):
    '''Schema for error response'''
    return {"error": error, "code": code, "message": message}