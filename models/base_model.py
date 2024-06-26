#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

from datetime import datetime
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid
from os import getenv

time_fmt = "%Y-%m-%dT%H:%M:%S.%f"

if getenv("HBNB_TYPE_STORAGE") == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A Base class for all hbnb models"""

    # if getenv("HBNB_TYPE_STORAGE") == 'db':
    #     id = Column(String(60), nullable=False, primary_key=True)
    #     created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    #     updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=False, default=datetime.now())

    # def __init__(self, *args, **kwargs):
    #     """base model initialized"""
    #     self.id = str(uuid.uuid4())
    #     self.created_at = datetime.now()
    #     self.updated_at = self.created_at
    #     for key, value in kwargs.items():
    #         if key == '__class__':
    #             continue
    #         setattr(self, key, value)
    #         if type(self.created_at) is str:
    #             self.created_at = datetime.strptime(self.created_at, time_fmt)
    #         if type(self.updated_at) is str:
    #             self.updated_at = datetime.strptime(self.updated_at, time_fmt)
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            try:
                if getenv('HBNB_TYPE_STORAGE') != 'db':
                    kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                                '%Y-%m-%dT%H:%M:%S.%f')
                    kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                            '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                                '%Y-%m-%d %H:%M:%S.%f')
                    kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                            '%Y-%m-%d %H:%M:%S.%f')
            except KeyError:
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
            if 'id' not in kwargs.keys():
                self.id = str(uuid.uuid4())
            if '__class__' in kwargs.keys():
                del kwargs['__class__']
            for i, j in kwargs.items():
                if i not in ['id', 'created_at', 'updated_at']:
                    self.__setattr__(i, j)
            self.__dict__.update(kwargs)


    def __str__(self):
        """return String representation of the BaseModel class"""
        # return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
        #                                  self.to_dict())
        # return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
        #                                  self.__dict__)
        dict = self.__dict__
        if '_sa_instance_state' in dict.keys():
            del dict['_sa_instance_state']
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, dict)

    def save(self):
        """updates 'updated_at' with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self, save_to_disk=False):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].isoformat()
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        if '_password' in new_dict:
            new_dict['password'] = new_dict['_password']
            new_dict.pop('_password', None)
        if 'amenities' in new_dict:
            new_dict.pop('amenities', None)
        if 'reviews' in new_dict:
            new_dict.pop('reviews', None)
        new_dict["__class__"] = self.__class__.__name__
        # new_dict.pop('_sa_instance_state', None)
        if '_sa_instance_state' in new_dict.keys():
            del new_dict['_sa_instance_state']
        if not save_to_disk:
            new_dict.pop('password', None)
        return new_dict

    def delete(self):
        """Delete current instance from storage by calling its delete method"""
        models.storage.delete(self)
