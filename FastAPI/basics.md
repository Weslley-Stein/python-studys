# Basics of FastAPI
```py
#Importing Required Modules
from fastapi import FastAPI, Body
from pydantic import BaseModel

#Instance the FastAPI
app = FastAPI()

#Creating a Base Model for something
class Post(BaseModel):
	title:str
	content:str

#Creating handle for Post requisitions
@app.post("/create_post"):
def create_post(new_post:Post):
	post = new_post.dict()
	return post


# the method base_model.dict() will return you a python dict
```


