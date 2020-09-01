#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
import os


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade='all, delete')
    else:
        name = ""
        @property
        def cities(self):
            """returns city list instead"""
            res = []
            for i in models.storage.all(City).values():
                if i.state_id == self.id:
                    res.append(i)
            return res
