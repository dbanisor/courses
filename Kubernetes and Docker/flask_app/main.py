from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f'<h1>Hello Docker, hi!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0')