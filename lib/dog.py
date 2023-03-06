from sqlalchemy import create_engine

from models import Dog

engine = create_engine('sqlite:///:memory:')

# 2 takes a declarative_base, creates table "dogs" if it does not exist, and returns the engine.
def create_table(base):
    base.metadata.create_all(engine)
    return engine

# 3  that takes a Dog instance and session as arguments, 
# saves the dog to the database, and returns the session.
def save(session, dog):
    session.add(dog)
    session.commit()
    return session

# 4 that takes a database row and returns a Dog instance
def new_from_db(session, row):
    return session.query(Dog).filter_by(id = row.id).first()

# 5 that takes a session and 
# returns a list of Dog instances for every record in the database.
def get_all(session):
    return [dog for dog in session.query(Dog)]

# 6 that takes a session and name 
# and returns a Dog instance corresponding to its database record retrieved by name.
def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()

# 7  that takes a session and id and 
# returns a Dog instance corresponding to its database record retrieved by id.
def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()

# 8 that takes a session, a name, and a breed as arguments 
# and returns a Dog instance matching that record.
def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()

# 9 that takes a session instance, and breed as arguments 
# and updates the instance's breed.
def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()
    return session