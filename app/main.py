from fastapi import FastAPI

from app import models
from app.routers import post, user
from app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)


@app.get('/')
def root():
    return "hello this is the root"



# @app.get('/sqlalchemy')
# def test(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     print(type(posts))
#     return {"data": f"{posts}"}

# @app.get('/post')
# def get_posts(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return {'data': f"{posts}"}

# try:
#     conn = psycopg2.connect(host='localhost', database='fastapi',
#                             user='postgres', password=12345678, cursor_factory=RealDictCursor)
#     cursor = conn.cursor()
#     print("connection to DB succesfull")
# except Exception as e:
#     time.sleep(5)
#     print("connection to DB failed")
#     print(e)


# def get_all_post():
#     cursor.execute("""
#                 SELECT * FROM post;
#                 """)
#     posts = cursor.fetchall()
#     if posts:
#         return posts
#     return None


# def find_post(id):
#     if id:
#         cursor.execute("""
#                     select * from post where id = %s
#                     """, (id,))
#         post = cursor.fetchone()
#         if post:
#             return post
#     return None


# def find_post_index(id: int):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i
#     return None


# def delete_post_with_id(id):
#     try:
#         cursor.execute("""
#                     DELETE FROM post WHERE id = %s
#                     """, (str(id)))
#         conn.commit()
#         return True
#     except Exception as e:
#         return False


# def update_post_with_id(id, post):
#     print(type(post))
#     print(post)
#     # post = post.model_dump()
#     try:
#         cursor.execute(""" UPDATE post SET title = %s, content = %s, published = %s where id = %s RETURNING * """,
#                        (post['title'], post['content'], post['published'], str(id),))
#         updated_post = cursor.fetchone()
#         print(updated_post)
#         if updated_post:
#             conn.commit()
#             return updated_post
#     except Exception as e:
#         print(f"error while updating")
#         print(e)
    # return None
