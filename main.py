from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()



class Post(BaseModel):
   title:str
   content:str
   

my_posts=[{"title":"This is my first post","content":"I am learning fastify","id":1},
          {"title":"This is my second post","content":"This is an example app","id":2}
         ]


def find_post(id):
    for post in my_posts:
      if post['id']==id:
        return post


@app.get("/")
def root():
    return {"message": "Hello World 12345"}

@app.get("/posts")
def get_posts():
    return {"message": my_posts}



@app.post("/posts")
def createpost(post:Post):
    post_dict=post.dict()
    post_dict['id']=randrange(0,100000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


@app.get("/posts/{id}")
def get_post(id:int):

    post=find_post((id))
    print(post)
    return {"post_detail":post}

