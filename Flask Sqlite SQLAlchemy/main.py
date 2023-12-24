from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
db = SQLAlchemy()
db.init_app(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

# with app.app_context():
#     db.create_all()


@app.route('/')
def home():
    results = db.session.execute(db.select(Books).order_by(Books.title))
    all_results = results.scalars()
    return render_template('index.html', books=all_results)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':

        new_book = Books(title=request.form['bookname'], author=request.form['bookauthor'], rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('add.html')


@app.route("/edit/<int:book_id>", methods=['GET', 'POST'])
def edit_rating(book_id):
    with app.app_context():
        search_book = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()

    book = {
        "book_title": search_book.title,
        "current_rating": search_book.rating
    }

    if request.method == 'POST':

        new_rating = request.form['editrating']
        with app.app_context():
            book_to_update = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
            book_to_update.rating = new_rating
            db.session.commit()

        return redirect(url_for('home'))

    return render_template('edit_rating.html', book=book)


@app.route("/delete")
def delete_book():
    book_id = request.args.get('id')

    with app.app_context():
        search_book = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()


        with app.app_context():
            book_to_del = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
            db.session.delete(book_to_del)
            db.session.commit()


        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

