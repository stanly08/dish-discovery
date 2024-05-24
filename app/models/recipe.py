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
    views = Column(Integer, default=0)

    comments = relationship('Comment', backref='recipe', lazy=True)
    savedrecipes = relationship('SavedRecipe', backref='recipe', lazy=True)

    def __init__(self,
                 title,
                 ingredients,
                 instructions,
                 user_id,
                 image_url=None,
                 description=None,
                 category_id=None):
        """
        The constructor for the Recipe class.

        Parameters:
            title: The title of the recipe.
            ingredients: The ingredients of the recipe.
            instructions: The instructions for preparing the recipe.
            user_id: The user id of the user who created the recipe.
        """
        self.title = title
        self.description = description
        self.ingredients = ingredients
        self.instructions = instructions
        self.image_url = image_url
        self.user_id = user_id
        self.category_id = category_id
        self.views = 0

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
    
    def to_dict(self):
        """
        This method returns a dict representation of the recipe
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'ingredients': self.ingredients,
            'instructions': self.instructions,
            'image_url': self.image_url,
            'user_id': self.user_id,
            'category_id': self.category_id,
            'views': self.views,
            'comments': [comment.to_dict() for comment in self.comments],
            'savedrecipes': [savedrecipe.to_dict() for savedrecipe in self.savedrecipes]
        }
