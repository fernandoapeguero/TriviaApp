import os
from flask import Flask, json, request, abort, jsonify
from flask.globals import current_app
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from random import random
import math 

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  cors = CORS(app, resources={r'/trivia_api/*': {'origins': '*'}})

  @app.after_request
  def after_request(reponse):
        reponse.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        reponse.headers.add('Access-Control-Allow-Method' , 'GET,PATCH ,POST, DELETE , OPTIONS')
        return reponse
        
  QUESTION_COUNT = 10
  # ======================= Helper Functions =======================
  def paginate(request ,selection):
        
        page = request.args.get('page' , 1 , type=int)
        start = (page - 1) * QUESTION_COUNT
        end = start + QUESTION_COUNT
        
        questions = [question.format() for question in selection]
        
        formatted_questions = questions[start:end]
  
        return formatted_questions

  # gets a random entry from database results 
  def random_question(questions):
        if len(questions) > 0:
              my_question = questions[math.floor(random() * len(questions))]

              return my_question.format()
        else:
              return ""


  # ===================== End Points ======================

  @app.route('/trivia_api/categories')
  def get_categories():
        
        try:
          categories = Category.query.all()

          formatted_categories = [category.format() for category in categories]
          print(formatted_categories)

          categories_result = {}

          for c in formatted_categories:
              categories_result[c['id']] = c['type']

          return jsonify({
            'success': True,
            'categories': categories_result
          }), 200
        except:
          abort(404)


  @app.route('/trivia_api/questions' , methods=['GET'])
  def get_questions():

      try:

        categories = Category.query.order_by('id').all()
        questions = Question.query.order_by('id').all()
      
        paginated_questions = paginate( request ,questions)

        if len(paginated_questions) == 0:
              abort(404)

        formatted_categories = [category.format() for category in categories]

        categories_result = {}

        for c in formatted_categories:
              categories_result[c['id']] = c['type']

        return jsonify({
          'success': True,
          'questions': paginated_questions,
          'totalQuestions': len(questions),
          'categories':  categories_result
        }) , 200

      except:
        abort(404)


  @app.route('/trivia_api/<int:question_id>/questions' , methods=['DELETE'])
  def delete_question(question_id):
        
        current_question = ''
        try:
          
          question = Question.query.get(question_id)

          current_question = question.format()
          question.delete()
        
          return jsonify({
            'success': True,
            'id': current_question['id'],
            'deletedQuestion': current_question
          }) , 200
        except:
          abort(404)

  @app.route('/trivia_api/questions' , methods=['POST'])
  def post_question():
        
        try:
          data = request.get_json()

          question = data.get('question')
          answer = data.get('answer')
          difficulty = data.get('difficulty')
          category = data.get('category')
          
          print(data)

          if not question  or not answer  or not difficulty or not category:
                abort(422)
          else:

                question = Question(
                    question=question,
                    answer=answer,
                    category=category,
                    difficulty=difficulty
                )

                question.insert()

                return jsonify({
                  'success': True
                }) , 200

        except:
          abort(422)

  @app.route('/trivia_api/search_questions' , methods=['POST'])
  def get_question():
    try:
      data = request.get_json()
      search_term = data['searchTerm']

      questions = Question.query.filter(Question.question.ilike(f'%{search_term}%')).all()

      formatted_questions = paginate(request , questions)

      return jsonify({
        'success': True ,
        'questions': formatted_questions,
        'totalQuestions': len(questions)
      }) , 200
    except:
      abort(422)

  @app.route('/trivia_api/<int:category_id>/categories')
  def get_questions_by_category(category_id):
        
        try:
  
          category = Category.query.filter_by(id=category_id).first()
          questions = Question.query.filter_by(category=str(category.id)).all()

          formatted_questions = [question.format() for question in questions]
          
          return jsonify({
            'success': True,
            'questions': formatted_questions,
            'totalQuestions': len(questions),
            'currentCategory': category.type
          }),200
          
        except:
          abort(404)
        
  @app.route('/trivia_api/quizzes' , methods=['POST'])
  def get_quizz_questions():
        
        try:
          data = request.get_json()
          print(data)
          quizz_category = data.get('quiz_category')['id']
          previous_questions = data.get('previous_questions')
          questions_tupple = tuple(previous_questions)      
          print(quizz_category)
          current_question = ''
          
          if quizz_category == 0:
              print('all')
              questions = Question.query.filter(Question.id.notin_(questions_tupple)).all()
              current_question = random_question(questions)
          else: 
              print('specific')
              questions = Question.query.filter(Question.category == quizz_category , Question.id.notin_(questions_tupple)).all()
              current_question = random_question(questions)


          print(current_question)

          return jsonify({
            'success': True,
            'question': current_question 
          }) ,200
        except:
          abort(404)

  # =========== Error Hanlders ====================

  @app.errorhandler(400)
  def bad_request(error):
        
        return jsonify({
          'success': False,
          'error':  400,
          'message': 'Bad request'
        }), 400

  @app.errorhandler(404)
  def not_found(error):
        
        return jsonify({
          'success': False,
          'error':  404,
          'message': 'Not Found'
        }), 404

  @app.errorhandler(422)
  def unproccesable(error):
        
        return jsonify({
          'success': False,
          'error':  422,
          'message': 'Unprocessable'
        }), 422

  @app.errorhandler(500)
  def server_error(error):
        
        return jsonify({
          'success': False,
          'error':  500,
          'message': 'Server Error'
        }), 500

  return app

    