"""
This is the category file for the application.
"""
from sqlalchemy import Column, String
from app.models.base import BaseModel
from sqlalchemy.orm import relationship
from app import db


class Category(BaseModel, db.Model):
    """
    This is the RecipeCategory model for storing the recipe category details.

    Attributes:
        name: The name of the category.
        description: The description of the category.
    
    """
    __tablename__ = 'recipecategories'

    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255), nullable=True)

    recipes = relationship('Recipe', backref='category', lazy=True)

    def __init__(self, name, description=None):
        """
        The constructor for the RecipeCategory class.

        Parameters:
            name: The name of the category.
            description: The description of the category.
        """
        self.name = name
        self.description = description
