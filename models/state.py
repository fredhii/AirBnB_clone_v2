#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    ''' sql '''
    cities = relationship("City", backref="state", cascade='all, delete')
    
    # ''' file storage '''
    # cities = []
    # instance = models.storage.all(City)
    # for i in instance:
    #     if i.state_id = self.id:
    #         cities.append(i)
