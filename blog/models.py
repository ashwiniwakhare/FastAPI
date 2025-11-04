# Import Base from our database configuration
from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# Blog table model
class Blog(Base):
    __tablename__ = 'blogs'  # DB table name

    # Primary key and indexed for faster queries
    id = Column(Integer, primary_key=True, index=True)
    
    # Title and body fields for blog content
    title = Column(String)
    body = Column(String)

    # Foreign key linking each blog to a user (nullable for now to allow blogs without assigned users)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)

    # Relationship with User model (one user → many blogs)
    creator = relationship("User", back_populates="blogs")


# User table model
class User(Base):
    __tablename__ = 'users'  # DB table name

    # User details
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    # Relationship back reference → A user can have multiple blog posts
    blogs = relationship('Blog', back_populates="creator")
