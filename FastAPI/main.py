from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title:str
    content:str 

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Hello World"}
 
@app.get("/posts")
def get_posts():
    return {"Data": "Post"}

@app.post("/createpost")
def create_post(new_post: Post):
    print(new_post)
    return {"message":"sucessfully created posts"}
