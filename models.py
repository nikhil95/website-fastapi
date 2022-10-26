from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey,Boolean,Numeric

# Define To Do class inheriting from Base
class Contact(Base):
                __tablename__='contact'
                id=Column(Integer,primary_key=True)
                name=Column(String(255))
                email=Column(String(255))
                message=Column(String(255))
               
                



class Demo(Base):
                __tablename__='demo'
                id=Column(Integer,primary_key=True)
                name=Column(String(255))
                company_name=Column(String(255))
                email=Column(String(255))
                position=Column(String(255))
                phone_no=Column(Numeric)
                services=Column(String(255))
               
                

class Subscription(Base):
                __tablename__='subscription'
                id=Column(Integer,primary_key=True)
                email=Column(String(255))
                active=Column(Boolean)