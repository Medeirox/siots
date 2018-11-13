from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@main.route('/user/<user>', methods=['GET', 'POST'])
def user(user):
    return '<h1>Hello {0}!</h1>'.format(user)

@main.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html')