import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


        # Creating a database

# db = sqlite3.connect("books-collection.db")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float, nullable=False)

# with app.app_context():
#     db.create_all()

new_book = Book(title="a title", author="an author", rating=8)
db.session.add(new_book)
db.session.commit()

        # Creating the cursor (mouse)

# cursor = db.cursor()


        # Creating table in a database

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")


        # Adding data in the table

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
