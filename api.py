from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def root():
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
    
    return "WELCOME TO THE JOBS POSTING API"


if __name__ == "__main__":
    app.run(debug = True, threaded = True)