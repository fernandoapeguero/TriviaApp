import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}@{}/{}".format('postgres:2225' ,'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
            


    def tearDown(self):
        """Executed after reach test"""
        pass
    
    def test_delete_question(self):
            # Change item_id to desire id to be deleted
        item_id  = 25
        res = self.client().delete(f'/trivia_api/{item_id}/questions')
        
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code, 200 )
        self.assertEqual(data['id'] , item_id)
        self.assertTrue(data['deletedQuestion'])

    def test_get_categories(self):
        res = self.client().get("/trivia_api/categories")

        data = json.loads(res.data)

        self.assertEqual(res.status_code , 200)
        self.assertTrue(len(data['categories']))


    def test_404_error_get_categories(self):

        res = self.client().get("/trivia_api/categorie")

        data = json.loads(res.data)

        self.assertEqual(res.status_code , 404)
        self.assertEqual(data['success'] , False)
        self.assertEqual(data['message'] , 'Not Found')


    def test_get_questions(self):

        res = self.client().get('/trivia_api/questions?page=1')
        data = json.loads(res.data)
        # print(data)
        self.assertEqual(res.status_code , 200)
        self.assertEqual(data["success"] , True)
        self.assertTrue(data["totalQuestions"])
        self.assertTrue(len(data["questions"]))


    def test_404_error_get_questions(self):

        res = self.client().get('/trivia_api/questions?page=50')

        data = json.loads(res.data)

        self.assertEqual(res.status_code , 404)
        self.assertEqual(data['success'] , False)
        self.assertEqual(data['message'] , 'Not Found')


    def test_422_unproccesable_post_question(self):
        question = {
            'question': '',
            'answer': "2020",
            'difficulty': 1,
            'category': ''
        }

        res = self.client().post("/trivia_api/questions" , json=question)

        self.assertEqual(res.status_code , 422)


    def test_post_question(self):

        question = {
            "question": "what's the worst year since the 2000",
            "answer": "2020",
            "difficulty": "1",
            "category": "2"
        }

        res = self.client().post("/trivia_api/questions" , json=question)

        data = json.loads(res.data)

        self.assertEqual(res.status_code , 200)
        self.assertEqual(data["success"] , True)


    def test_get_question_by_category(self):
        
        category_id = 2
        res = self.client().get(f'/trivia_api/{category_id}/categories')
        
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code , 200)
        self.assertEqual(data['success'] , True)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['totalQuestions'])


    def test_404_error_get_question_by_category(self):

        category_id = 100000
        res = self.client().get(f'/trivia_api/{category_id}/categories')

        data = json.loads(res.data)

        self.assertEqual(res.status_code , 404)
        self.assertEqual(data['message'] , 'Not Found')


    def test_get_quizz_question(self):

        json_data = {
            'previous_questions': [5],
            'quiz_category': {
                    'type': 'Science', 'id': 0
                }
        }

        res = self.client().post('/trivia_api/quizzes' , json=json_data)

        data = json.loads(res.data)

        self.assertEqual(res.status_code , 200)
        self.assertTrue(data['question'])
        self.assertTrue(len(data['question']))


    def test_404_not_found_get_quizz_question(self):
        
        json_data = {
            'previous_questions': [5],
            'quiz_category': {
                    'type': 'Science'
                }
        }

        res = self.client().post('/trivia_api/quizzes' , json=json_data)

        self.assertEqual(res.status_code , 404)



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()