from sqlmodel import create_engine, Session
from config import config

DATABASE_URL = f"{config.DB_PROTOCOL}://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"

engine = create_engine(DATABASE_URL, echo=True)

def get_session() :
    if engine is None : 
        raise Exception("Database connection not initialized!")
    
    with Session(engine) as session:
        yield session