from datetime import datetime
from db import Base

from sqlalchemy import Coulumn, String, DateTime, ForeignKey
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.dialects.mysql import INTEGER, BOOLEAN

import hashlib

SQLITE3_NAME = "./db.sqlite3"

class User(Base):
    __tablename__ = 'user'
    id = Column(
        'id',
        INTEGER,
        primary_key=True,
        autoincrement=True,
    )
    username = Column('username', String(256))
    password = Column('password', String(256))
    mail = Column('mail', String(256))

    def __init__(self, username, password, mail):
        self.username = username
        self.password = hashlib.md5(password.encode()).hexdigest
        self.mail = mail

    def __str__(self):
        return str(self.id) + ':' + self.username

class Task(Base):
    __tablename__ = 'task'
    id = Column
