#!/usr/bin/env python3

from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# 1 contains model "Dog" with name and breed attributes.
class Dog(Base):
    __tablename__ = 'dog'

    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer, primary_key=True)
    name = Column(String)
    breed = Column(String)