import os
from flask import Flask, json, request, abort, jsonify
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
  
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  cors = CORS(app, resources={r"/trivia_api/*": {"origins": "*"}})


  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(reponse):
        reponse.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        reponse.headers.add('Access-Control-Allow-Method' , 'GET,PATCH ,POST, DELETE , OPTIONS')
        return reponse
        
  QUESTION_COUNT = 10

  def paginate(request ,selection):
        
        page = request.args.get('page' , 1 , type=int)
        start = (page - 1) * QUESTION_COUNT
        end = start + QUESTION_COUNT
        
        questions = [question.format() for question in selection]
        
        formatted_questions = questions[start:end]
  
        return formatted_questions
        


  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route("/trivia_api/categories")
  def get_categories():
        
        try:
          categories = Category.query.all()

          formatted_categories = [category.format() for category in categories]
          print(formatted_categories)

          categories_result = {}

          for c in formatted_categories:
              categories_result[c['id']] = c['type']

          return jsonify({
            "success": True,
            "categories": categories_result
          })
        except:
          abort(400)

  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  
  @app.route('/trivia_api/main/questions')
  def index():

      try:

        categories = Category.query.order_by('id').all()
        questions = Question.query.order_by('id').all()
      
        paginated_questions = paginate( request ,questions)

        formatted_categories = [category.format() for category in categories]

        categories_result = {}

        for c in formatted_categories:
              categories_result[c['id']] = c['type']

        return jsonify({
          "questions": paginated_questions,
          "totalQuestions": len(questions),
          "categories":  categories_result
        })

      except:
        abort(404)
        
        
  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''

  @app.route('/trivia_api/<int:question_id>/questions' , methods=['DELETE'])
  def delete_question(question_id):
        print('nothing')
        try:
          
          question = Question.query.get(question_id)

          current_question = question.format()
          question.delete()
        
          return jsonify({
            'success': True,
            'id': current_question['id'],
            'question': current_question['question']
          })
        except:
          abort(404)
  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''


  @app.route("/trivia_api/questions" , methods=['POST'])
  def post_question():
        
        try:
          data = request.get_json()

          question = data.get('question')
          answer = data.get('answer')
          difficulty = data.get('difficulty')
          category = data.get('category')

          question = Question(
              question=question,
              answer=answer,
              category=category,
              difficulty=difficulty
          )

          question.insert()

          return jsonify({
            "success": True
          })

        except:
          abort(400)
  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''

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
      })
    except:
      abort(422)

  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/trivia_api/<int:category_id>/categories')
  def get_questions_by_category(category_id):
        
        try:
  
          category = Category.query.filter_by(id=category_id).first()
          questions = Question.query.filter_by(category=str(category.id)).all()

          formatted_questions = [question.format() for question in questions]
          
          return jsonify({
            "questions": formatted_questions,
            "totalQuestions": len(questions),
            "currentCategory": category.type

          })
          
        except:
          abort(404)

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
  @app.route("/trivia_api/quizzes" , methods=['POST'])
  def get_quizz_questions():
        
        try:
          data = request.get_json()

          quizz_category = data.get('quiz_category')['id']
          previous_questions = data.get('previous_questions')
          questions_tupple = tuple(previous_questions)      
          print(questions_tupple)
          
          current_question = ''
          
          if quizz_category == 0:
              current_question = Question.query.filter(Question.id.notin_(questions_tupple)).first()
          else: 
              current_question = Question.query.filter(Question.category == quizz_category , Question.id.notin_(questions_tupple)).first()


          if current_question is None:
                current_question = ''
                

          return jsonify({
            "success": True,
            "question": current_question.format() 
          })
        except:
          abort(404)

  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  # 400, 404, 422 and 500

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

    