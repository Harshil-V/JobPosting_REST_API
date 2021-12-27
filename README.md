# JobPosting REST API - Pattern
---
## Description Provided for the API
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

The database file 'jobsPosts.db' already exists in this repo, you can delete it and recreate the database file and the a table all the jobs posting using the url below.

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
PUT(Add) Method:

http://127.0.0.1:5000/add?TITLE=___&DESCRIPTION=____&PAY=___&LOCATION=___

The blank spaces are where you input the data 
```

```
UPDATE Method:

http://127.0.0.1:5000/update/id?TITLE=___&DESCRIPTION=___&PAY=___&LOCATION=____

The blank space are where the updated values goes and replace the 'id' with the id value that you would like to update
```

```
DELETE Method:

http://127.0.0.1:5000/delete/id

Replace id with the id num that you would like to delete from the database
```

