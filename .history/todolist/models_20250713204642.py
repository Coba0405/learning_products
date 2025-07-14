from datetime import datetime
from db import Base

from sqlalchemy import Coulumn, String, DateTime, ForeignKey
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.dialects.mysql import INTEGER, BOOLEAN

import hashlib

SQLITE3_NAME = "./db.sqlite3"

class User(Base):
id = Column(
    'id',
    INTEGER,
    primary_)
