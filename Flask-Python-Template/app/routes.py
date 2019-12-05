from app import server
from flask import render_template


@server.route('/')
@server.route('/index')
def index():
    return render_template('index.html')


def some_true_function():
    return True
