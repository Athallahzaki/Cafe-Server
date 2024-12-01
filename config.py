from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_PROTOCOL = getenv("DB_PROTOCOL")
    DB_USER = getenv("DB_USER")
    DB_PASSWORD = getenv("DB_PASSWORD")
    DB_HOST = getenv("DB_HOST")
    DB_PORT = getenv("DB_PORT")
    DB_NAME = getenv("DB_NAME")
    
    SV_HOST = getenv("SV_HOST")
    SV_PORT = int(getenv("SV_PORT"))

config = Config()