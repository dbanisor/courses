from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


    def to_dict(self):
        dictionary = {}

        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def get_random_cafe():
    cafes = Cafe.query.all()
    random_cafe = random.choice(cafes)

    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def get_all_cafes():
    all_cafes = Cafe.query.order_by(Cafe.name).all()
    dict_list = []
    for i in all_cafes:
        dict_list.append(i.to_dict())
    return jsonify(cafes=dict_list)

@app.route("/search")
def search_cafe():
    query_location = request.args.get("loc")
    cafes_found = Cafe.query.filter_by(location=query_location).all()
    if cafes_found:
        return jsonify(cafe=[cafe.to_dict() for cafe in cafes_found])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})

@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
