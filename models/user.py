#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'users'
        first_name = Column(String(128))
        last_name = Column(String(128))
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        places = relationship('Place', backref='user', cascade='all, delete')
        reviews = relationship('Review', backref='user', cascade='all, delete')

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
