from flask import Flask
import sqlite3

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

@app.route("/home")
def root():
    db = sqlite3.connect('jobPosts.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM JOBS')
    data = cursor.fetchall()
    db.close()
    return str(data)

if __name__ == "__main__":
    app.run(debug = True, threaded = True)