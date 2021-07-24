# FormTable.py
from flask import Flask, render_template, request
import os

from flask import Flask, url_for
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

app = Flask(__name__)
print(os.getenv("BASE_URL"))
app.config['APPLICATION_ROOT'] = os.getenv("BASE_URL")
base_url = app.config['APPLICATION_ROOT']


def simple(env, resp):
    resp(b'200 OK', [(b'Content-Type', b'text/plain')])
    return [b'Invalid url']


@app.route("/")
def home():
    return render_template("home.html")


@app.route('/users')
def users():
    return render_template('users.html')


@app.route('/new')
def new():
    return render_template('new.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form

    return render_template("result.html", result=result)


@app.route('/ping')
def ping():
    return "Service is Up !"


app.wsgi_app = DispatcherMiddleware(simple, {f'{base_url}': app.wsgi_app})


if __name__ == '__main__':
    app.run(debug=True, port="5000", host="0.0.0.0")
