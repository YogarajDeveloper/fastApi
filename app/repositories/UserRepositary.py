from app.models.User import User
import sqlalchemy.orm as orm

def create_user(db: orm.Session, name: str, email: str):
    user = User(name=name, email=email)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user