#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.script import Manager
from flask import render_template
from flask.ext.bootstrap import Bootstrap


app = Flask(__name__)
manager = Manager(app)
bootsrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
#    app.run(debug=True)
    manager.run()
