from fastapi import FastAPI, Response, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, field_validator
from typing import Optional, List, Dict

app = FastAPI()

# Temporary storage for posts until converting to a Postgres database & Global id variable assigned to posts
my_posts = []
post_id: int = 1


# Define Post Model with validation
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

    @field_validator('title')
    def check_title(cls, value):
        if not value or value.strip() == "":
            raise ValueError("title cannot be an empty string or Null")
        return value

    @field_validator('content')
    def check_content(cls, value):
        if not value or value.strip() == "":
            raise ValueError("content cannot be an empty string or Null")
        return value


# Helper function that searches an array of posts dictionaries by id
def get_post_by_id(posts_array: List[Dict], target_id: int):
    """Search for a dictionary by 'id' field in a list of dictionaries."""
    for post in posts_array:
        if post['id'] == target_id:
            return post
    return None


# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to my Social Media API"}


# Create a post
@app.post("/posts")
def create_post(post: Post):
    global post_id
    post_to_dict = post.model_dump()
    post_to_dict = {"id": post_id, **post_to_dict}
    my_posts.append(post_to_dict)
    post_id += 1
    return {"data": f"Successfully added post: {post_to_dict}"}


# Get a post by id
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post: dict = get_post_by_id(my_posts, id)
    if post is None:
        return JSONResponse(content={"message": "Post not found"}, status_code=status.HTTP_404_NOT_FOUND)
    return {f"data": post}


# Get all posts
@app.get("/posts")
def get_all_posts():
    return {f"data": f"{my_posts}"}


# Update post by id
@app.put("/posts/{id}")
def update_post(id: int):
    return {f"data": f"Successfully updated post with id: {id}"}


# Delete post by id
@app.delete("/posts/{id}")
def delete_post(id: int):
    return {f"data": f"Successfully deleted post with id: {id}"}
