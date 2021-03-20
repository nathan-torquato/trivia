import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def serialise_entity_list(entity_list):
  serialised_list = [entity.serialise() for entity in entity_list]
  return serialised_list

def create_app(test_config=None):
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

  def get_categories_map():
    categories = Category.query.all()
    serialised_list = serialise_entity_list(categories)

    return {
      category['id']: category['type'] for category in serialised_list
    }
  
  @app.route('/categories')
  def get_categories():
    categories = Category.query.all()
    
    return jsonify({
      'success': True,
      'categories': get_categories_map(),
    })

  @app.route('/questions')
  def get_questions():
    page = request.args.get('page', 1, type=int)
    questions = Question.query.order_by(
      Question.id.asc()
    ).paginate(page, max_per_page=QUESTIONS_PER_PAGE)
    
    return jsonify({
      'success': True,
      'questions': serialise_entity_list(questions.items),
      'total_questions': questions.total,
      'categories': get_categories_map(),
      'current_category': None,
    })

  @app.route('/questions', methods=['POST'])
  def create_question():
    try:
      props = request.get_json()
      question = Question(props)
      question.insert()

      return jsonify({
        'success': True,
        'question': question.serialise()
      })
    except:
      abort(422)

  @app.route('/questions/<int:id>', methods=['DELETE'])
  def delete_question(id):
    question = Question.query.get_or_404(id)
    question.delete()

    return jsonify({
      'success': True,
      'id': question.id
    })

  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''

  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''


  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''

  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  
  return app

    