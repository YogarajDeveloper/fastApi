
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends

from app.database import get_db
from app.services.UserService import create_user_service

router = APIRouter()


@router.post("/users")
def create_user_controller(name: str, email: str, db: Session = Depends(get_db)
):
    user = create_user_service(db,name, email)
    return {
        "message": "User created successfully",
        "user": [
            user
        ]
    }
 