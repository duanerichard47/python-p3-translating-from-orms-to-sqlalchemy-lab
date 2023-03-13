#!/usr/bin/env python3

from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer, create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'

    id =Column(Integer(),primary_key=True)
    name = Column(String())
    breed = Column(String())

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, breed={self.name!r})"

if __name__ == '__main__':
    engine = create_engine('sqlite:///dogs.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

