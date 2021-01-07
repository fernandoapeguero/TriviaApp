# Trivia App

## Starting Guide 
### introduction 

The Trivia app is a interactive trivia game that you can play with friends or by yourself.
There are different categories to play and enjoy with friends.

Categories : 
  
    Science 🧪
    Art 🎨
    Geography 🗺️
    History 🕐
    Entertaiment 📽️
    Sports ⚽
    
### How to play 


You can choose a category from the provided ones and complete the questions and compare scores with you friends at the end 
whoever have more points wins.

#### How to add a question 

To add a question go to the add tab and insert the information require if any of the field are empty it will not be uploaded to the game.

## Game Preview

<img width="960" alt="trivia" src="https://user-images.githubusercontent.com/25759298/103929445-5778c000-50eb-11eb-8d17-46740639c633.PNG">

---

# Getting Setup

APP Structure

Trivia 

1. [`./frontend/`](./frontend)
2. [`./backend/`](./backend)

## Front-End

### Installing Dependencies

#### Installing Node and NPM

This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

#### Installing project dependencies

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

>_tip_: **npm i** is shorthand for **npm install**

## Required Tasks

## Running Your Frontend in Dev Mode

The frontend app was built using create-react-app. In order to run the app in development mode use ```npm start```. You can change the script in the ```package.json``` file. 

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.<br>

```bash
npm start
```

# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:

Unix Base Cmd's
```bash
psql trivia < trivia.psql
```
Windows Cmd

```bash
psql -U (postgres username) trivia < trivia.psql
```


## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

>_tip_: for all test to pass change the id on the delete test in the test_flaskr file for the item you want to test else it will failif the id does not exist.

---

# Trivia Api Endpoints

## Authentication 

There is no authentication needed for this api
  ```
  Authentication is on the road map in future updates of the api
  ```
## Base Url 

the base url returns a list of all the question in the api and the categories in the trivia. Pagination is integrated into the api each page will get 10 questions each.

    https://localhost:5000/trivia_api/questions


###  Sample Response From Base Url
 
 ```bash
 {
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "questions": [
    {
      "answer": "Lake Victoria", 
      "category": "3", 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }
  ], 
  "success": true, 
  "totalQuestions": 21
}
 ```
  
 ## Error Handling 
 
 Type of error the api handles

   * 400 Bad Request
   * 404 Not Found
   * 405 Method Not Allowed
   * 422 Unproccesable Entity
   * 500 Server Error 
   
Error Handling Response 

```bash
{
  'success': False,
  'error':  400,
  'message': 'Bad request'
}

```

responses with come back in a json object format 

<br>

# Endpoint Library 

Here you will find all the endpoint you need to work with the api 

The Structure of the EndPoint library is simple since you will deploy the backend localy for this app we know the domain will be http://localhost:5000
and you will only need the path for example /trivia_api/questions in this library we will prefix the path with the method needed for the call. 

Example: POST/trivia_api/questions 

---

## GET Endpoints

<br>

### GET/trivia_api/questions

returns paginated questions and all categories

Reponse

```bash
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "questions": [
    {
      "answer": "Lake Victoria", 
      "category": "3", 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": "3", 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": "3", 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Escher", 
      "category": "2", 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }
  ], 
  "success": true, 
  "totalQuestions": 21
}
```

<br>

### GET/trivia_api/categories 

returns all categories

Reponse

```bash
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "success": true
}
```

<br>


### GET/trivia_api/<int:category_id>/categories 

return questions base on selected category id

Reponse
```bash


{
  "currentCategory": "Art", 
  "questions": [
    {
      "answer": "Escher", 
      "category": "2", 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": "2", 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "One", 
      "category": "2", 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Jackson Pollock", 
      "category": "2", 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }
  ], 
  "success": true, 
  "totalQuestions": 4
}

```
---

## POST Endpoints

<br>

### POST/trivia_api/questions


To post a question the enpoint expect a you to pass
question, answer, difficulty, category is any is missing it will fail and not post the question to the database 

JSON body 

```bash
{
  "question": "What is the rarest M&M color?",
  "answer": "Brown",
  "difficulty": 3,
  "category": 4
}
```

returns json object 
```bash
Response
{
  'success': True
}
```

<br>

### POST/trivia_api/search_questions - return question base on search term

The api expect for you to pass the search term into the body of the json call

JSON body

```bash
{
  "searchTerm": "which"
}
```


Response
```bash
{
  "questions": [
    {
      "answer": "The Palace of Versailles", 
      "category": "3", 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": "3", 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Escher", 
      "category": "2", 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }, 
    {
      "answer": "Jackson Pollock", 
      "category": "2", 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }, 
    {
      "answer": "Scarab", 
      "category": "4", 
      "difficulty": 4, 
      "id": 23, 
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }
  ], 
  "success": true, 
  "totalQuestions": 5
}

```

<br>

### POST/trivia_api/quizzes

It returns a single question pet call

JSON Body sample 
```bash
{
    "previous_questions": [],
    "quizz_category": {
        "type": "Art",
        "id": "2"
    }
}
```

Response 
```bash
{
  {
  "question": {
    "answer": "Jackson Pollock", 
    "category": "2", 
    "difficulty": 2, 
    "id": 19, 
    "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
  }, 
  "success": true
}
 
}
```

## DELETE Endpoint

<br>

### DELETE/trivia_api/<int:question_id>/questions

this end point will delete a question from the database base on the id given to the endpoint. The endpoint will return a json object with a success boolean and the deleted question if you want to use it that information in a modal and show the user what the erase.

Reponse 

```bash
{
  "deletedQuestion": {
    "answer": "nose ", 
    "category": "1", 
    "difficulty": 3, 
    "id": 25, 
    "question": "de donde centame "
  }, 
  "id": 25, 
  "success": true
}
```
