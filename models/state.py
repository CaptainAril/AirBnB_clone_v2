#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if (getenv("HBNB_TYPE_STORAGE") == 'db'):
        # for DBStorage
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        # for FileStorage
        @property
        def cities(self):
            """Returns a list of city objects with state_id = current id."""
            cityList = []
            allCities = models.storage.all(City)
            for city in allCities:
                if allCities[city].state_id == self.id:
                    cityList.append(allCities[city])
            return cityList
