"""
This is the base model for all the models
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime
from datetime import datetime

Base = declarative_base()

class BaseModel(Base):
    """
    This is the base model for all the models.
    It includes the common attributes and methods that other models can
    inherit from.

    Attributes:
    id: The unique identifier for each model.
    created_at: The timestamp when the record was created.
    updated_at: The timestamp when the record was last updated.

    Methods:
    __abstract__: This attribute is set to True to prevent SQLAlchemy from
    creating a table for this model.
    
    """
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.now(datetime.UTC))
    updated_at = Column(DateTime, default=datetime.now(datetime.UTC),
                        onupdate=datetime.now(datetime.UTC))
