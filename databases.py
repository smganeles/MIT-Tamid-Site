from model import Base, Member

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_Member(name_input,pwd_input):
	member_object = Member(
		Name = name_input,
		Password = pwd_input)
	session.add(member_object)
	session.commit()

def All_Members():
	members = session.query(Member).all()
	return members

def is_Member(name_input,pwd_input):
	member = session.query(Member).filter_by(Name = name_input).first()
	if member:
		if member.Password == pwd_input:
			return True
	return False

def is_Name(name_input):
	members = session.query(Member).all()
	for member in members:
		if member.Name == name_input:
			return True
	return False