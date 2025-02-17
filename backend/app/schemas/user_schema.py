import uuid
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from fastapi_users import schemas
from datetime import datetime

# class UserBase(BaseModel):
    # email: EmailStr
    # username: str = Field(..., min_length=3, max_length=50)

class UserCreate(schemas.BaseUserCreate):
    # pass
    name: str = Field(..., min_length=3, max_length=50)
    #password: str = Field(..., min_length=6)

class UserUpdate(schemas.BaseUserUpdate):
    pass
    #password: Optional[str] = Field(None, min_length=6)

class UserRead(schemas.BaseUser[uuid.UUID]):
    name: str

    # class Config:
      #  orm_mode = True  # Allows the output model to be compatible with ORM objects

class UserSchema(BaseModel):
    name: str
    email: str
    # last_login: datetime

    class Config:
        from_attributes = True