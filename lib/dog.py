from models import Dog
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def create_table(base, engine):
     engine = create_engine('sqlite:///dogs.db')
     Base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def new_from_db(session):
    session.query(Dog)

def get_all(session):
    return session.query(Dog).all()
    

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()
    

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    # return session.query(Dog).filter(Dog.name == name).filter(Dog.breed == breed).first()
    return session.query(Dog).filter(Dog.name == name and Dog.breed == breed).first()
def update_breed(session, dog, breed):
    dog.breed = breed
    session.add(dog)
    session.commit()



