#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    ''' The Amenity class, contains state ID and name '''
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenity = relationship("Place", secondary=place_amenity)
