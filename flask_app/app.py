from flask import Flask, jsonify, request, url_for, redirect, session, render_template, g
import sqlite3

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'Thisisasecret!'


# ___________________________BAZA DE DATE________________________________________
            # O FUNCTIE PT CONECTAREA LA BAZA DE DATE

def connect_db():
    sql = sqlite3.connect('/sqlite-tools-win32-x86-3420000/data.db')
    sql.row_factory = sqlite3.Row
    return sql

            # O FUNCTIE PT REDAREA BAZEI DE DATE
def get_db():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

            # O FUNCTIE PT INCHIDEREA BAZEI DE DATE
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
# ___________________________BAZA DE DATE________________________________________


@app.route('/')
def index():
    session.pop('name', None)
    return '<h1>Hello world!</h1>'

# Building URLs

@app.route('/home', methods=['GET', 'POST'], defaults={'name': 'User'})     # ---> aceasta metoda va accepta ca ruta de home sa functioneze fara nicio variabila nume.
@app.route('/home/<string:name>', methods=['GET', 'POST'])                         # Va folosi ca default orice cuvant alegem ex. 'User'
def home(name):
    session['name'] = name
    db = get_db()
    cur = db.execute('select id, name, location from users')
    results = cur.fetchall()

    return render_template('home.html', name=name, display=False,
                           my_list=['one', 'two', 'three', 'four'],
                           list_of_dictionaries=[{'name': 'Zach'}, {'name': 'Zoe'}], results=results)

@app.route('/json')
def json():
    if 'name' in session:
        name = session['name']
    else:
        name = 'Notinsession!'

    return jsonify({'key': 'value', 'key2': [1, 2, 3], 'name': name})

# passing in data using a query string
@app.route('/query')    # to input data in the url it looks like this: http://127.0.0.1:5000/query?name=Denise&location=Florida
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    # this takes data from the url, saves it in variables and does smth with it.
    return '<h1>Hi {}. You are from {}. You are on the query page!</h1>'.format(name, location)

# SENDING AND RETRIEVING FORM DATA

#this route will create the form where the user can pass in data and hit submit
@app.route('/theform', methods=['GET', 'POST'])
def theform():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        name = request.form['name']
        location = request.form['location']

        db = get_db()
        db.execute('insert into users (name, location) values (?, ?)', [name, location])
        db.commit()

        # return '<h1>Hello {}. You are from {}. You have submitted the form successfully!</h1>'.format(name, location)
        return redirect(url_for('home', name=name, location=location))

# process is going to be the url where the user goes after hitting submit#

#this route will retrieve the data from the form
# @app.route('/process', methods=['POST'])
# def process():
    # retrieving data is similar to retrieving data from the url but because we use a form, we will use request.form


@app.route('/processjson', methods=['POST'])
def processjson():

    data = request.get_json()

    name = data['name']
    location = data['location']

    randomlist = data['randomlist']

    return jsonify({'result': 'Success!', 'name': name, 'location': location, 'randomkeyinlist': randomlist[1]})

# _______________________________A FUNCTION THAT SHOWS THE RESULTS IN THE DATABASE___________________

@app.route('/viewresults')
def view_results():
    db = get_db()
    cur = db.execute('select id, name, location from users')
    results = cur.fetchall()
    return '<h1>The ID is {}. The name is {}. The location is {}.</h1>'.format(results[2]['id'], results[2]['name'], results[2]['location'])
#____________________________________________________________________________________________________
if __name__ == "__main__":
    app.run()