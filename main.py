from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return {"data": "Blog List"}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)

    
    
class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]
        
@app.post('/blog')
def create_blog(request:Blog):
    # return request
    return{'data':f'blog is created as title with {request.title}'}




@app.get('/about')
def about():
    return {"data":"this is the about page"}

@app.get('/blog/{id}')
def show(id: int ):
    return {'data':id}    

@app.get('/blog/{id}/comments')
def comments(id):
    #fetch comments of blog with id =id
    return {'data':{'1','2'}}

@app.get('/blog')
def index(limit=10,published:bool=True, sort:Optional[str]=None):
    if published:
        return{'data':f'{limit} published blogs are from database'}
    else:
        return{'data':f'{limit} all blogs are from database'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':"this is unpublished blog"}

