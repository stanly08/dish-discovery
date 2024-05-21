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

    def seed_categories():
        """
        This method is used to seed the recipecategories table with default categories.
        """
        categories = [
            {'name': 'Appetizers', 'description': 'Small dishes served before the main course'},
            {'name': 'Main Course', 'description': 'The main dish of a meal'},
            {'name': 'Desserts', 'description': 'The sweet course eaten at the end of a meal'},
            {'name': 'Drinks', 'description': 'Liquid refreshments'},
            {'name': 'Salads', 'description': 'A cold dish of various mixtures of raw or cooked vegetables'},
            {'name': 'Soups', 'description': 'A liquid dish, typically made by boiling meat, fish, or vegetables in stock or water'},
            {'name': 'Breads', 'description': 'A staple food prepared from a dough of flour and water, usually by baking'},
            {'name': 'Breakfast', 'description': 'The first meal of the day'},
            {'name': 'Lunch', 'description': 'A meal eaten in the middle of the day'},
            {'name': 'Dinner', 'description': 'The main meal of the day, taken either around midday or in the evening'},
            {'name': 'Snacks', 'description': 'A small amount of food eaten between meals'}
        ]
        for item in categories:
            category = Category.query.filter_by(name=item['name']).first()
            if not category:
                category = Category(name=item['name'], description=item['description'])
                db.session.add(category)
                db.session.commit()
        return True
    
    def to_dict(self):
        """This is a dict representation of the category"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
