# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the `/backend` directory and running:

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
```bash
psql trivia < trivia.psql
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

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

## API doc

> Every response has a "success" field with a boolean value (not represented in the sample responses bellow for the sake of brevity).

> Error responses will include the "status_code" in the body as well.

> Unless otherwise indicated, listed *Request Query Params* are required

### Routes

> GET `/categories`
- *Description:*: Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- *Response:* 
```json
{
  "categories": {
    "1" : "Science",
    "2" : "Art",
    "3" : "Geography",
    "4" : "History",
    "5" : "Entertainment",
    "6" : "Sports"
  }
}
```

> GET `/categories/<int:category_id>/questions`
- *Description:*: Fetches the questions for the specified category if it exists, throws 404 if it doesn't
- *Response:*
```
{
  "current_category": 1,
  "questions": [
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    ...
  ],
  "total_questions": 3
}
```

> POST `/quizzes`
- *Description:* Fetches not previously asked questions randomizing either all questions or within a specific category.
- *Request.body:*
```
{
  "previous_questions": int[],
  "category_id": int
}
```
- *Response:*
```
{
  "question": {
    "answer": "The Liver", 
    "category": 1, 
    "difficulty": 4, 
    "id": 20, 
    "question": "What is the heaviest organ in the human body?"
  },
  "previous_questions": int[], # same as requested
  "category_id": int, # same as requested
}
```

> GET `/questions?page=<page_number>`

- *Description:* Fetches a paginated list of questions
- *Request Params:* page:int (value 1 is used as default)
- *Response:*  
```
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    ...
  }, 
  "current_category": null, 
  "questions": [
    {
      "answer": "name", 
      "category": 1, 
      "difficulty": 5, 
      "id": 5, 
      "question": "What's your name"
    },
    ... 
  ], 
  "total_questions": 19
}
```

> POST `/questions`
- *Description:* Creates a new question
- *Request.body:*
```
{
  question:string,
  answer:string,
  difficulty:int,
  category:string
}
```
- *Response:* 
```
{
  "question": {
    "answer": "The Liver",
    "category": 1,
    "difficulty": 4,
    "id": 20,
    "question": "What is the heaviest organ in the human body?"
  },
}
```

> POST `/questions/search`
*Description:* Fetches all questions matching the search term (case-insensitive)
- *Request.body:*
```
{
  searchTerm:string
}
```
- *Response:*
```
{
  "current_category": null, 
  "questions": [
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    ...
  ], 
  "total_questions": 10
}
```

> DELETE `/questions/<question_id>`
*Description:* Deletes an existing question
- *Response:* 
```
{
  "id": "28"
}
```

## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```