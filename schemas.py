from pydantic import BaseModel, EmailStr
from datetime import date

class UserBase(BaseModel):
    name: str
    email: EmailStr
    date_of_birth: date
    country: str
    favorite_sport: str
    favorite_team: str

class UserCreate(UserBase):
    password: str

class UserSignIn(BaseModel):
    email: EmailStr
    password: str
