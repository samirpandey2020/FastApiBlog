
from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, status, HTTPException, Depends

from app.database import get_db
from app import schemas, models, Utils
import app.schemas.post as postschema 
router = APIRouter(
    prefix='/post',
    tags=['Post']
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=postschema.ResponsePost)
async def create_post(post: postschema.PostCreate, db: Session = Depends(get_db)):
    try:
        if post:
            new_post = models.Post(
                **post.model_dump())
            db.add(new_post)
            db.commit()
            db.refresh(new_post)
            return new_post
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get("/all_post", status_code=status.HTTP_200_OK, response_model=List[postschema.ResponsePost])
async def get_post(db: Session = Depends(get_db)):
    try:
        posts = db.query(models.Post).all()
        if posts:
            return posts
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No posts found")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=postschema.ResponsePost)
async def get_post(id: int, db: Session = Depends(get_db)):
    try:
        post = db.query(models.Post).filter(models.Post.id == id).first()
        if post:
            return post
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID {id} not found"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int, db: Session = Depends(get_db)):
    try:
        post = db.query(models.Post).filter(models.Post.id == id)
        existing_post = post.first()
        if existing_post is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Post with ID {id} does not exist"
            )

        post.delete(synchronize_session=False)
        db.commit()
        return None

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.put('/update/{id}', status_code=status.HTTP_200_OK, response_model=postschema.ResponsePost)
async def update_post(id: int, updated_post: postschema.UpdatePost, db: Session = Depends(get_db)):
    try:
        post_q = db.query(models.Post).filter(
            models.Post.id == id)
        post = post_q.first()
        if post:
            post_q.update(updated_post.model_dump())
            db.commit()
            return post_q.first()
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID {id} not found"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
