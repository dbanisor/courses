'''
In the views.py file we are saving all the standard routes for our website (homepage for ex., except login page which
is going to be in the auth.py file)
'''

from flask import Blueprint, render_template

# Here we are saying that this file is the blueprint of our app.

views = Blueprint('views', __name__)  # the name of the blueprint 'Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")


