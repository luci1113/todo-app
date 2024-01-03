
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from flask_login import UserMixin

Base = declarative_base()

class User(UserMixin, Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    keycloak_id = Column(String)
    pro = Column(Boolean, default=False)
    todos = relationship('Todo', backref='user')

    @classmethod
    def get(cls, id):
        return cls.query.get(id)

class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    time = Column(DateTime, server_default=func.now())
    user_id = Column(Integer, ForeignKey('users.id'))
    image = Column(String)

    @classmethod
    def get(cls, id):
        return cls.query.get(id)

def init_db():
    from sqlalchemy import create_engine
    from sqlalchemy.orm import scoped_session, sessionmaker

    engine = create_engine('sqlite:///database.db', convert_unicode=True)
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))
    Base.query = db_session.query_property()
    Base.metadata.create_all(bind=engine)

    return db_session

