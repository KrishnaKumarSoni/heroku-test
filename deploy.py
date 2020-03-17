from flask import Flask


# initialize the flask app
app = Flask(__name__)

# default route
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'