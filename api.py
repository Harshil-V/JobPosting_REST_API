from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return "WELCOME TO THE JOBS POSTING API"

if __name__ == "__main__":
    app.run(debug = True, threaded = True)