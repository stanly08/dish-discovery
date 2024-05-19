"""
This file contains the model for the SavedRecipes table.
"""
from sqlalchemy import Column, Integer, ForeignKey
from app.models.base import BaseModel
from app import db
from sqlalchemy.orm import relationship


class SavedRecipe(BaseModel, db.Model):
    """
    This is the Saved model for storing the saved recipes details.

    Attributes:
        user_id: The user id of the user who saved the recipe.
        recipe_id: The recipe id of the saved recipe.
    
    """
    __tablename__ = 'savedrecipes'

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    recipe_id = Column(Integer, ForeignKey('recipes.id'), nullable=False)

    def __init__(self, user_id, recipe_id):
        """
        The constructor for the Saved class.

        Parameters:
            user_id: The user id of the user who saved the recipe.
            recipe_id: The recipe id of the saved recipe.
        """
        self.user_id = user_id
        self.recipe_id = recipe_id
