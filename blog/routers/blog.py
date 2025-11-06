from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
from blog import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from blog.repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs'])
get_db = database.get_db

# API endpoint → Get all blogs
@router.get("/", response_model=List[schemas.ShowBlog])
def get_allblogs(db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_allblogs(db)


# API endpoint → Create a new blog entry
@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request,db)        # Return inserted blog


# API endpoint → Get a single blog by ID
@router.get('/{id}', status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog)
def get_show(id:int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
   return blog.get_show(id, db)


# Delete a specific blog by ID
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)


# Update a specific blog by ID
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)
