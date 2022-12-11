#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from os import environ


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # for DBStorage
    cities = relationship('City', cascade='all, delete', backref='state')
    # for FileStorage

    @property
    def cities(self):
        """Returns a list of city objects with state_id = current id."""
        cityList = []
        allCities = models.storage.all()
        for city in allCities:
            if allCities[city].state_id == self.id:
                cityList.append(allCities[city])
        return allCities
