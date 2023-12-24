from flask import Flask, render_template
import requests
import random
from datetime import datetime

app = Flask(__name__)
year = datetime.now().year
my_name = "Denise Banisor"

@app.route("/")
def home():
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, current_year=year, name=my_name)


@app.route("/guess/<some_name>")
def extract_name(some_name):
    genderize_link = requests.get(f"https://api.genderize.io?name={some_name}")
    gender = genderize_link.json()["gender"]
    agify_link = requests.get(f"https://api.agify.io?name={some_name}")
    returned_age = agify_link.json()["age"]
    return render_template("guess.html", name=some_name, sex=gender, age=returned_age)


@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)