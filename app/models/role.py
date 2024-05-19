"""
This is the roles files for the application.
"""
from sqlalchemy import Column, String
from app.models.base import BaseModel
from sqlalchemy.orm import relationship
from app import db

class Role(BaseModel, db.Model):
    """
    This is the Role model for storing the role details.

    Attributes:
        name: The name of the role.
        description: The description of the role.

    """
    __tablename__ = 'roles'

    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255), nullable=True)

    users = relationship('User', backref='role', lazy=True)

    def __init__(self, name, description=None):
        """
        The constructor for the Role class.

        Parameters:
            name: The name of the role.
            description: The description of the role.
        """
        self.name = name
        self.description = description
