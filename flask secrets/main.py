from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField


class LoginForm(FlaskForm):
    email = StringField('Email')
    password = StringField("Password")


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-to-keep-it-secret"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)