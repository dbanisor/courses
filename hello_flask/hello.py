from flask import Flask
import requests

app = Flask(__name__)

# Here we created custom decorators that we could use: making the text bold, underlined or italic.
def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
           "<p style='text-align: center'>This is a paragraph.</p>" \
           "<img src='https://media.giphy.com/media/l4KhNBgG8RaItFkDS/giphy.gif'>"

# Different routes using the app. route decorator
@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"

# Creating variable paths and converting the path to a specified data type
@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)


