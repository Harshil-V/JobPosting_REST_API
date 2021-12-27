# JobPosting REST API - Pattern

## Description
Design and implement REST endpoints for Job Posting. We are looking for simple CRUD (Create, Read, Update and Delete) endpoints. Each job posting should have integer id, title, description, location, and hourly pay rate among other things. We also want to keep track of when a job posting is created and when it is updated. Please use any relational database and ORM of your choice to model the data. You can choose the framework for implementing API endpoints, but we want to see a well-defined API interface including the request &amp; response. Please also include tests for the endpoints.  We have set up a base repository at https://gitlab.com/patternlabs-public/exercise-backend with some skeleton code. Please use it as your starting point.  Please upload your solution to a public Github/Gitlab/Bitbucket repository (only one). If your solution requires any specific setup like specific node/npm versions, please include those requirements in a `README.md` file. Once you have done so, please send us the link to that public repository. 

## Prerequisite
This project require:
- Python
- pip 
- SQLite / SQLite Studio
- Postman (Optional)

## Requirements 

You will need to install Flask

```bash
$ pip install flask
```

## Run the API 

Start the Server
```bash
$ python api.py
```
You can use Postman or any browser and visit: http://127.0.0.1:5000/

If "http://127.0.0.1:5000/" does not work there will a url available that will work own you start the server. (The post might be different depending on the user computer setup and which post are available)

<br>

**Create database called *jobsPosts.db* with table called *JOBS* is already not present.**
```
http://127.0.0.1:5000/createdb

Creates:
- jobsPosts.db 
- JOBS table in the database
```

### CRUD Methods

```
GET Method:

http://127.0.0.1:5000/
or 
http://127.0.0.1:5000/get
or
http://127.0.0.1:5000/home
```

```

```

