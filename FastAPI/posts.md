```py
from fastapi import FastAPI, Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

posts = [ ] 

def find_post(id):
	for post in posts:
		if post["id"] = id
			return post

class Post(BaseModel):
	title:str
	content:str
	id:int

@app.post("/create-post")
def create_post(post:Post):
	new_post = post.dict()
	return {"Status":"Post Succesful Created"}

@app.get("/posts/{id}")
def posts(id):
	post = find_post(id)
	return post
```
