from pydantic import BaseModel,EmailStr,Field

class User(BaseModel):
    name:str
    email:EmailStr
    

class UserIn(User):
    password:str

class UserOut(User):
    id: str
