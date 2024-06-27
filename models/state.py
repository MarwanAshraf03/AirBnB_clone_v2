#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """state inherits from Bm and Base will be re
    p in column containing a string """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        id = Column(String(60), nullable=False, primary_key=True)
        # cities = relationship("City", cascade="all, delete", backref
        # ="states")
        cities = relationship("City", cascade="all, delete", backref="state")
        # cities = relationship("City", cascade="all, delete-orphan", backref="
        # state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """returns City instances"""
            values_city = models.storage.all(City).values()
            list_city = []
            for city in values_city:
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city
