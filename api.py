from flask import Flask
from flask import request
import sqlite3
import json
import os

app = Flask(__name__)

@app.route('/createdb')
def createdb():
    db = sqlite3.connect('jobPosts.db')
    cursor = db.cursor()
    if os.path.isfile('jobPosts.db'):
        cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='JOBS' ''')
        exists = cursor.fetchone()[0]
        #if the count is 1, then table exists
        
        if exists == 1:          
            db.close()
            return ('Database and Table already exists')
        db.close()
        return "Database already exists"
        


    cursor.execute('''CREATE TABLE IF NOT EXISTS JOBS (
        Id INTEGER PRIMARY KEY, 
        TITLE text NOT NULL, 
        DESCRIPTION TEXT NOT NULL, 
        PAY INTEGER NOT NULL, 
        LOCATION TEXT NOT NULL,
        CREATED TEXT DEFAULT CURRENT_TIMESTAMP,
        UPDATED TEXT DEFAULT CURRENT_TIMESTAMP
    )''')
    db.commit()

    db.close()

    return ("DATABASES CREATED WITH TABLE NAMED: \"JOBS\" ")

@app.route("/")
@app.route("/get")
@app.route("/home")
def root():
    db = sqlite3.connect('jobPosts.db')
    cursor = db.cursor()

    cursor.execute('SELECT * FROM JOBS')
    data = cursor.fetchall()

    db.close()

    return str(data)

"FORMAT : http://127.0.0.1:5000/add?TITLE=___&DESCRIPTION=____&PAY=___&LOCATION=___"
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

"FORMAT: http://127.0.0.1:5000/update/id?TITLE=___&DESCRIPTION=___&PAY=___&LOCATION=____"
@app.route('/update/<id>')
def update(id):
    db = sqlite3.connect('jobPosts.db')
    cursor = db.cursor()

    TITLE = request.args.get('TITLE')
    DESCRIPTION = request.args.get('DESCRIPTION')
    PAY = request.args.get('PAY')
    LOCATION = request.args.get('LOCATION')

    cursor.execute("SELECT EXISTS(SELECT 1 FROM JOBS WHERE Id=%s)" % id)
    exists = cursor.fetchone()[0]

    if exists == 0:
        db.close()
        return "Update Not Possible - There is no entry with ID:{}".format(id)

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

    cursor.execute("SELECT EXISTS(SELECT 1 FROM JOBS WHERE Id=%s)" % id)
    exists = cursor.fetchone()[0]

    if exists == 0:
        db.close()
        return "Delete Not Possible - There is no entry with ID:{}".format(id)
    
    cursor.execute("DELETE FROM JOBS WHERE Id=%s" % id)
    db.commit()

    db.close()
    return "Deleted Entry with ID:{}".format(id)

if __name__ == "__main__":
    app.run(debug = True, threaded = True)