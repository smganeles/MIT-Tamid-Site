from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Member(Base):
	__tablename__ = "Members"
	id = Column(Integer, primary_key=True)
	Name = Column(String)
	Password = Column(String)