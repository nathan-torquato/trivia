import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "trivia"
database_path = f"postgresql://postgres:postgres@localhost:5432/{database_name}"

db = SQLAlchemy()

'''
setup_db(app)
  binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
  app.config["SQLALCHEMY_DATABASE_URI"] = database_path
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  db.app = app
  db.init_app(app)
  db.create_all()

'''
Question

'''
class Question(db.Model):  
  __tablename__ = 'questions'

  id = Column(Integer, primary_key=True)
  question = Column(String, nullable=False)
  answer = Column(String, nullable=False)
  category = Column(String, db.ForeignKey('categories.id'), nullable=False)
  difficulty = Column(Integer, nullable=False)

  def __init__(self, props):
    self.question = props['question']
    self.answer = props['answer']
    self.category = props['category']
    self.difficulty = props['difficulty']

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def serialise(self):
    return {
      'id': self.id,
      'question': self.question,
      'answer': self.answer,
      'category': self.category,
      'difficulty': self.difficulty
    }

'''
Category

'''
class Category(db.Model):  
  __tablename__ = 'categories'

  id = Column(Integer, primary_key=True)
  type = Column(String, nullable=False)
  questions = db.relationship(
    'Question',
    backref='categories',
    lazy=True
  )

  def __init__(self, type):
    self.type = type

  def serialise(self):
    return {
      'id': self.id,
      'type': self.type
    }
  
  def get_serialised_questions(self):
    return [q.serialise() for q in self.questions]