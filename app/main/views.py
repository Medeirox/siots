from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    return '<h1>Hello World!</h1>'

@main.route('/user/<user>', methods=['GET', 'POST'])
def user(user):
    return '<h1>Hello {0}!</h1>'.format(user)

@main.route('/template/', methods=['GET', 'POST'])
def template():
    return render_template('base.html')