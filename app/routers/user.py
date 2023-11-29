
from sqlalchemy.orm import Session
from fastapi import status, HTTPException, Depends, APIRouter

from app import models, Utils
from app.database import get_db
import app.schemas.user as userschemas

router = APIRouter(
    prefix='/user',
    tags= ['User']
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=userschemas.ResponseUser)
def create_user(user: userschemas.UserBase, db: Session = Depends(get_db)):
    try:
        if user:
            user.password = Utils.get_password_hash(user.password)
            new_user = models.User(**user.model_dump())
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            return user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@router.get('/{id}', response_model=userschemas.ResponseUser)
def get_user_id(id: int, db: Session = Depends(get_db)):
    try:
        user = db.query(models.User).filter(models.User.id == id).first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"no user with id {id}"
            )
        return user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
