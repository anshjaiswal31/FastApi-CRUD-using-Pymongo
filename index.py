from fastapi import FastAPI
from routes.user import user
import uvicorn
app=FastAPI()
app.include_router(user)

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

if __name__ == "__main__":
   uvicorn.run("index:app", host="127.0.0.1", port=9000, reload=True)