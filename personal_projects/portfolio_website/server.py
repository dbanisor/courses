from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/elements.html")
def elements_page():
    return render_template("elements.html")

@app.route("/index.html")
def index_page():
    return render_template("index.html")

@app.route("/generic.html")
def generic_page():
    return render_template("generic.html")

@app.route("/morse_code_template.html")
def morse_code_page():
    return render_template("morse_code_template.html")

@app.route("/tic_tac_toe_template.html")
def tic_tac_toe_page():
    return render_template("tic_tac_toe_template.html")

if __name__ == "__main__":
    app.run(debug=True)
