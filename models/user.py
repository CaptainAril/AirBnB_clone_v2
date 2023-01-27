#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage_type
from uuid import uuid4


class User(BaseModel, Base):
    ''' defines User class '''
    __tablename__ = 'users'
    if storage_type == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)

        places = relationship('Place', backref='user',
                              cascade='all, delete, delete-orphan')

        reviews = relationship('Review', backref='user',
                               cascade='all, delete, delete-orphan')

        def __init__(self, **kwargs):
            self.id = str(uuid4())
            for key, value in kwargs.items():
                setattr(self, key, value)
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
