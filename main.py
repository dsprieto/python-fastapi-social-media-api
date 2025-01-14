from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List, Dict

app = FastAPI()


post_id: int = 1


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = []


def search_by_id(posts_array: List[Dict], target_id: int):
    """Search for a dictionary by 'id' field in a list of dictionaries."""
    for post in posts_array:
        if post['id'] == target_id:
            return post
    return None


@app.get("/")
def root():
    return {"message": "Welcome to my API"}


@app.post("/posts")
def create_post(post: Post):
    global post_id
    post_to_dict = post.model_dump()
    post_to_dict = {"id": post_id, **post_to_dict}
    my_posts.append(post_to_dict)
    post_id += 1
    return {"data": f"successfully added post: {post_to_dict}"}


@app.get("/posts/{id}")
def get_post(id: int):
    post: dict = search_by_id(my_posts, id)
    return {f"data": post}


@app.get("/posts")
def get_all_posts():
    return {f"data": f"{my_posts}"}


@app.put("/posts/{id}")
def update_post(id: int):
    return {f"data": f"Successfully updated post with id: {id}"}


@app.delete("/posts/{id}")
def delete_post(id: int):
    return {f"data": f"Successfully deleted post with id: {id}"}
