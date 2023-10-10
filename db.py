from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm import Session

import config

engine = create_engine(config.DB_URL)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, unique=True, primary_key=True)
    department_id = Column(Integer)
    stream_id = Column(Integer)
    group_id = Column(Integer)
