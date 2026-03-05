from fastapi import Depends
from config.database import get_db

from models.user_models import User
from sqlalchemy.orm import Session
from schemas.user import RegisterUser
from config.hashing import Hashing


class UserService:
    def get_allUser(db: Session):
        return db.query(User).order_by(User.id.asc()).all()

    def get_user(email: str, db: Session = Depends(get_db)):
        return db.query(User).filter(User.email == email).first()

    def create_user(user: RegisterUser, db: Session = Depends(get_db)):
        db_user = User(
            name=user.name,
            email=user.email,
            password=Hashing.bcrypt(user.password),
            role=user.role,
            is_active=user.is_active,
        )

        db.add(db_user)
        db.commit()

        db.refresh(db_user)
        db_user.password = None

        return db_user

    def update_user(userid: int, user: RegisterUser, db: Session):
        db_userid = db.query(User).filter(User.id == userid).first()

        db_userid.name = user.name
        db_userid.email = user.email
        db_userid.password = Hashing.bcrypt(user.password)
        db_userid.role = user.role
        db_userid.is_active = user.is_active

        db.commit()

        return db_userid

    def deleteUser(userid: int, db: Session):
        db_userid = db.query(User).filter(User.id == userid).first()
        db_userid.is_active = False
        # db.delete(db_userid)
        db.commit()
        return db_userid

