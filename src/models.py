import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)


class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    planets = Column(Integer, ForeignKey('planets.id'), primary_key=True)
    characters = Column(Integer, ForeignKey('characters.id'), primary_key=True)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    diameter = Column(Integer)
    rotation_period = Column(Integer, nullable=False)
    oribital_period = Column(Integer)
    gravity = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(256), nullable=False)
    terrain = Column(String(256), nullable=False)
    surface_water = Column(String(256), nullable=False)
    url = Column(String(256), nullable=False)


class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    birth_year = Column(Integer)
    eye_color = Column(String(256), nullable=False)
    gender = Column(String(256), nullable=False)
    hair_color = Column(String(256), nullable=False)
    height = Column(String(256), nullable=False)
    weight = Column(String(256), nullable=False)
    complexion = Column(String(256), nullable=False)
    url = Column(String(256), nullable=False)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')