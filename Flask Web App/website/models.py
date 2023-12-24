'''
Here we are going to create out database models
A database model is like a layout or a blueprint for an object that is going to be stored in the database. Eg. all the user must conform to the model below
(email - unique and max 150 characters, etc)
'''

# we are going to have a database model for the users and another one for the notes

from . import db    #importing form the current python package (website folder) the db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

