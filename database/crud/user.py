from sqlmodel import Session
from database.models import User

# Create a user
def create_user(session: Session, name: str, email: str) -> User:
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

# Get a user by ID
def get_user_by_id(session: Session, user_id: int) -> User:
    return session.get(User, user_id)

# Get all users
def get_all_users(session: Session) -> list[User]:
    return session.query(User).all()

# Update a user
def update_user(session: Session, user_id: int, name: str, email: str) -> User:
    user = session.get(User, user_id)
    if user:
        user.name = name
        user.email = email
        session.commit()
        session.refresh(user)
    return user

# Delete a user
def delete_user(session: Session, user_id: int) -> bool:
    user = session.get(User, user_id)
    if user:
        session.delete(user)
        session.commit()
        return True
    return False