from fastapi import FastAPI
import uvicorn
from config import config

from routers import user

app = FastAPI()

app.include_router(user.router, prefix="/users", tags=["users"])

if __name__ == "__main__" :
    uvicorn.run(app, host=config.SV_HOST, port=config.SV_PORT)