from sqlalchemy import create_engine, Column, Integer, BigInteger
from sqlalchemy.orm import declarative_base

import config

engine = create_engine(config.DB_URL)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, unique=True, primary_key=True)
    department_id = Column(Integer)
    stream_id = Column(Integer)
    group_id = Column(Integer)


def init_db():
    Base.metadata.create_all(engine)
