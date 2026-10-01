
from sqlalchemy.orm import Session
from app.repositories.UserRepositary import create_user


def create_user_service(db: Session, name: str, email: str):

    # Logic to create a user in the database
    user=create_user(db, name, email)

    return user