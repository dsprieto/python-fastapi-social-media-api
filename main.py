from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
def root():
    return {"message": "Welcome to my API"}


@app.get("/posts/{post_id}")
def get_post(post_id: int):
    return {f"data": f"This is your post with id: {post_id}"}


@app.get("/posts")
def get_all_posts():
    return {f"data": f"These are all of the posts: "}


@app.put("/posts/{post_id}")
def update_post(post_id: int):
    return {f"data": f"Successfully updated post with id: {post_id}"}


@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    return {f"data": f"Successfully deleted post with id: {post_id}"}


@app.post("/posts")
def create_post(post: Post):
    print(post)
    new_post_to_dict = post.model_dump()
    return {"data": new_post_to_dict}
