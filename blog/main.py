# FastAPI main application setup
from turtle import title
from urllib import response
from webbrowser import get
from fastapi import FastAPI, Depends, status, Response, HTTPException
from pydantic import BaseModel
from . import schemas
from . import models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

# Initialize FastAPI app
app = FastAPI()

# Create all database tables using SQLAlchemy models
# Using bind=engine ensures correct metadata binding
models.Base.metadata.create_all(bind=engine)

# Dependency to get database session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API endpoint → Create a new blog entry
@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    # Creating a new Blog instance using data received
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)       # Add to DB session
    db.commit()            # Commit to save in DB
    db.refresh(new_blog)   # Refresh instance with DB state
    return new_blog        # Return inserted blog
    
# API endpoint → Get all blogs
@app.get("/blogs")
def get_allblogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()  # Fetch all records
    return blogs

# API endpoint → Get a single blog by ID
@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def get_show(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    
    # If blog not found → return HTTP 404 error
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )
    
    return blog  # Return blog if found

# Delete a specific blog by ID
@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    # Filter the blog record based on the given id
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    # Check if the blog with given id exists
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with ID {id} not found"
        )

    # Delete the blog if exists
    blog.delete(synchronize_session=False)

    # Commit the transaction to apply changes in the database
    db.commit()

    # Ideal response for 204 status is empty, 
    # but returning message for acknowledgment
    return {"message": "Blog deleted successfully"}


# Update a specific blog by ID
@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):

    # Convert Pydantic object to dictionary before update
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)

    # Check whether blog exists before updating
    if not blog_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} does not exist")

    # Perform update with dictionary data
    blog_query.update(request.dict())

    # Save changes to DB
    db.commit()

    return {"message": "Blog updated successfully"}

    