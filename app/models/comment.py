"""
This is the comments file for the application.
"""
from sqlalchemy import Column, String, ForeignKey, Integer
from app.models.base import BaseModel
from app import db
from sqlalchemy.orm import relationship
from app.models.recipe import Recipe
from app.models.user import User


class Comment(BaseModel, db.Model):
    """
    This is the Comment model for storing the comment details.

    Attributes:
        content: The content of the comment.
        user_id: The user id of the user who created the comment.
        recipe_id: The recipe id of the recipe the comment belongs to.
    
    """
    __tablename__ = 'comments'

    content = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    recipe_id = Column(Integer, ForeignKey('recipes.id'), nullable=False)

    def __init__(self, content, user_id, recipe_id):
        """
        The constructor for the Comment class.

        Parameters:
            content: The content of the comment.
            user_id: The user id of the user who created the comment.
            recipe_id: The recipe id of the recipe the comment belongs to.
        """
        self.content = content
        self.user_id = user_id
        self.recipe_id = recipe_id

    def __repr__(self):
        """
        This method returns a string representation of the Comment object.
        """
        return f'<Comment {self.content}>'

    def __str__(self):
        """
        This method returns a string representation of the Comment object.
        """
        return f'{self.content}'
    
    def to_dict(self):
        """This is a dict representation of the comments"""
        return {
            'id': self.id,
            'content': self.content,
            'user_id': self.user_id,
            'recipe_id': self.recipe_id,
            'user': self.user.to_dict() if self.user else None,
            'created_at': self.created_at,
        }
