"""
This is the User model for storing the user details
"""
from sqlalchemy import Column, String, Integer, ForeignKey
from app.models.base import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db
from app.models.role import Role
from app.models.recipe import Recipe
from sqlalchemy.orm import relationship


class User(BaseModel, UserMixin, db.Model):
    """
    This is the User model for storing the user details.

    Attributes:
        username: The username of the user.
        email: The email address of the user.
        password: The hashed password of the user.
        role_id: The role id of the user.
    
    Methods:
        set_password: This method is used to hash the password before storing it.
        check_password: This method is used to check if the password is correct.

    """
    __tablename__ = 'users'

    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False, default=1)

    recipes = relationship('Recipe', backref='user', lazy=True)
    comments = relationship('Comment', backref='user', lazy=True)
    saved = relationship('Saved', backref='user', lazy=True)

    def __init__(self, username, email, password, role_id=1):
        """
        The constructor for the User class.

        Parameters:
            username: The username of the user.
            email: The email address of the user.
            password: The hashed password of the user.
            role_id: The role id of the user.
        """
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.role_id = role_id

    def set_password(self, password):
        """
        This method is used to hash the password before storing it.
        """
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """
        This method is used to check if the password is correct.
        """
        return check_password_hash(self.password, password)
