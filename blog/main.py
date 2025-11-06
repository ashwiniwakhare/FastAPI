# FastAPI main application setup

from fastapi import FastAPI
from . import models
from .database import engine
from blog.routers import authentication, blog, user


# Initialize FastAPI app
app = FastAPI()

# Using bind=engine ensures correct metadata binding
models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)