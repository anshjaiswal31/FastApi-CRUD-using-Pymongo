from fastapi import APIRouter, HTTPException, Depends
from typing import List
from models.user import User,UserIn,UserOut
from config.db import conn
from bson import ObjectId
from schemas.user import userEntity,usersEntity
user=APIRouter()


#Dependency to verify db connection
async def get_database():
    if conn is None:
        raise  HTTPException(status_code=404, detail="Database Connection failed")
    elif conn.local.user is None:
        raise  HTTPException(status_code=404, detail="Database Collection doesnot exist")
    return conn.local.user

#get all users
@user.get('/') #response_model=List[UserOut]
async def find_all_users(db = Depends(get_database)):
    return usersEntity(db.find())

@user.get('/{id}', response_model=UserOut)
async def get_one_user(id,db = Depends(get_database)):
    return userEntity(db.find_one({"_id":ObjectId(id)}))

@user.post('/')
async def create_user(user:UserIn,db = Depends(get_database)):
    db.insert_one(dict(user))
    return usersEntity(db.find())

@user.put('/{id}')
async def update_user(id,user:UserIn,db = Depends(get_database)):
    (db.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    }))
    return userEntity(db.find_one({"_id":ObjectId(id)}))

@user.delete('/{id}', response_model=User, response_model_exclude={"passsword"})
async def delete_user(id, db = Depends(get_database)):
    return userEntity(db.find_one_and_delete({"_id":ObjectId(id)}))


