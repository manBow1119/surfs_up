#import dependencies
from flask import Flask

#Create new instance of flask app 'name' is a magic method
app = Flask(__name__)

#Create a route
@app.route('/')
def hello_world():
    return "Hello World"

#Trying a new route
@app.route('/')
def other_words():
    return 'which will print?'