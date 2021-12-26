from flask import Flask
from flask import request
import sqlite3
import json


app = Flask(__name__)

@app.route('/createdb')
def createdb():
    db = sqlite3.connect('jobPosts.db')
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS JOBS (
        Id INTEGER PRIMARY KEY, 
        TITLE text NOT NULL, 
        DESCRIPTION TEXT NOT NULL, 
        PAY INTEGER NOT NULL, 
        LOCATION TEXT NOT NULL,
        CREATED TEXT DEFAULT CURRENT_TIMESTAMP,
        UPDATED TEXT DEFAULT CURRENT_TIMESTAMP
    )''')

    # cursor.execute('''INSERT INTO JOBS (TITLE, DESCRIPTION, PAY, LOCATION) VALUES (
    #     'Tester',
    #     'I am a Tester',
    #     10,
    #     'REMOTE'
    # )''')

    # db.commit()
    # cursor.execute('SELECT * FROM JOBS')
    # data = cursor.fetchall()

    db.close()

    return ("DATABASES CREATED WITH TABLE NAMED: \"JOBS\" ")

"FORMAT : http://127.0.0.1:5000/add?TITLE=___&DESCRIPTION=____&PAY=___&LOCATION=___"
@app.route("/home")
def root():
    db = sqlite3.connect('jobPosts.db')
    cursor = db.cursor()

    cursor.execute('SELECT * FROM JOBS')
    data = cursor.fetchall()

    db.close()

    return str(data)

@app.route("/add")
def add():
    db = sqlite3.connect('jobPosts.db')
    cursor = db.cursor()

    TITLE = request.args.get('TITLE')
    DESCRIPTION = request.args.get('DESCRIPTION')
    PAY = request.args.get('PAY')
    LOCATION = request.args.get('LOCATION')

    cursor.execute('''INSERT INTO JOBS (TITLE, DESCRIPTION, PAY, LOCATION) VALUES (
        '%s',
        '%s',
        %s,
        '%s'
    )''' % (TITLE, DESCRIPTION, PAY, LOCATION))
    db.commit()
    return "TITLE: {} | DESCRIPTION: {} | PAY: {} | LOCATION: {}".format(TITLE, DESCRIPTION, str(PAY), LOCATION)

@app.route('/update/<id>')
def update(id):
    db = sqlite3.connect('jobPosts.db')
    cursor = db.cursor()

    TITLE = request.args.get('TITLE')
    DESCRIPTION = request.args.get('DESCRIPTION')
    PAY = request.args.get('PAY')
    LOCATION = request.args.get('LOCATION')

    cursor.execute('''UPDATE JOBS SET 
        TITLE="%s",
        DESCRIPTION="%s",
        PAY="%s",
        LOCATION="%s",
        UPDATED=CURRENT_TIMESTAMP WHERE Id=%s''' % (TITLE, DESCRIPTION, PAY, LOCATION, id))
    
    db.commit()

    db.close()
    return "Updated ID:{} with --> TITLE: {} | DESCRIPTION: {} | PAY: {} | LOCATION: {}".format(id, TITLE, DESCRIPTION, str(PAY), LOCATION)

@app.route("/delete/<id>")
def delete(id):
    db = sqlite3.connect('jobPosts.db')
    cursor = db.cursor()

    cursor.execute("DELETE FROM JOBS WHERE Id=%s" % id)
    db.commit()

    db.close()
    return "Deleted Entry with ID:{}".format(id)


if __name__ == "__main__":
    app.run(debug = True, threaded = True)