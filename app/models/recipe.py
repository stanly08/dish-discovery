"""
This is the recipe model for storing the recipe details
"""
from sqlalchemy import Column, String, Integer, ForeignKey, Text
from app.models.base import BaseModel
from app import db
from sqlalchemy.orm import relationship


class Recipe(BaseModel, db.Model):
    """
    This is the Recipe model for storing the recipe details.

    Attributes:
        title: The title of the recipe.
        description: The description of the recipe.
        ingredients: The ingredients of the recipe.
        instructions: The instructions for preparing the recipe.
        user_id: The user id of the user who created the recipe.
    
    """
    __tablename__ = 'recipes'

    title = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    ingredients = Column(Text, nullable=False)
    instructions = Column(Text, nullable=False)
    image_url = Column(String(255), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('recipecategories.id'), nullable=True)


    comments = relationship('Comment', backref='recipe', lazy=True)
    savedrecipes = relationship('SavedRecipe', backref='recipe', lazy=True)

    def __init__(self, title, ingredients, instructions, image_url, user_id, category_id=None):
        """
        The constructor for the Recipe class.

        Parameters:
            title: The title of the recipe.
            ingredients: The ingredients of the recipe.
            instructions: The instructions for preparing the recipe.
            user_id: The user id of the user who created the recipe.
        """
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.image_url = image_url
        self.user_id = user_id
        self.category_id = category_id

    def __repr__(self):
        """
        This method returns a string representation of the Recipe object.
        """
        return f'<Recipe {self.title}>'

    def __str__(self):
        """
        This method returns a string representation of the Recipe object.
        """
        return f'{self.title}'
