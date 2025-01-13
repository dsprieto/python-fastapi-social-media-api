from fastapi import FastAPI, Body

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to my API"}


@app.get("/posts/{post_id}")
def get_posts(post_id: int):
    return {f"data": f"This is your post with id: {post_id}"}


@app.post("/post/create")
def create_post(body: dict = Body(...)):
    print(body)
    return {"message": "Post successfully created"}
