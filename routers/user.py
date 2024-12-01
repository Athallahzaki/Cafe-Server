from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import crud, models, database

router = APIRouter()

# Create a user
@router.get("/")
def get_users(session: Session = Depends(database.get_session)):
    return crud.user.get_all_users(session)

# Create a user
@router.post("/")
def create_user(name: str, email: str, session: Session = Depends(database.get_session)):
    return crud.user.create_user(session, name, email)

# Get a user by ID
@router.get("/{user_id}")
def get_user(user_id: int, session: Session = Depends(database.get_session)):
    user = crud.user.get_user_by_id(session, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user