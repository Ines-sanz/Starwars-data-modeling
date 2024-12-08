import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable = False)
    last_name = Column(String, nullable = False)
    email = Column(String, nullable = False, unique = True)
  

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.first_name
        }

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user= relationship('Users', backref='posts')

class Medias(Base):
    __tablename__ = 'medias'
    id = Column(Integer, primary_key=True)
    src= Column(String, nullable = False)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post= relationship('Posts', backref='medias')

class Comments(Base):
    __tablename__ = 'Comments'
    id = Column(Integer, primary_key=True)
    comment = Column( Text, nullable= False)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post= relationship('Posts', backref='comments')
    author_id= Column(Integer, ForeignKey('users.id'))
    user= relationship('Users', backref= 'comments')


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
