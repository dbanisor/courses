from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    blog_data = blog_response.json()
    return render_template("index.html", blog_posts=blog_data)


if __name__ == "__main__":
    app.run(debug=True)
