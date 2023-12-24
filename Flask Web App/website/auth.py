from flask import Blueprint, render_template, request, flash
from website.models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])  # although we added '<form method="POST">' in the login.html file, we need to add hte HTTP methods in the route too.
def login():
    # to get the information passed by the user, we do this:

    return render_template("login.html")


@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 4:
            flash("Email must be greater than 4 characters.", category="error")
        elif len(firstName) < 2:
            flash("First name must be greater than 1 character.", category="error")
        elif password1 != password2:
            flash("Passwords don't match.", category="error")
        elif len(password1) < 7:
            flash("Passwords must be at least 7 characters.", category="error")
        else:
            #add user to database
            # new_user = User(email=email, first_name=firstName, password=)
            flash("Account created!", category="success")

    return render_template("sign_up.html")