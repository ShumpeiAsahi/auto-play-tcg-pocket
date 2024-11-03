from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Battle(Base):
    __tablename__ = "battles"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    start_time = Column(TIMESTAMP, default=datetime.utcnow)
    status = Column(String(20), default="ongoing")