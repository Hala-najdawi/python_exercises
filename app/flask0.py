#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 09:45:43 2019

@author: owner
"""
"""
from flask import Flask ,render_template
app=Flask(__name__)
@app.route('/hello/<int:score>')
def index(score):
    return render_template('hello.html',marks=score)
if __name__=='__main__':
    app.run()
"""
# html
"""
from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World! testing'
@app.route('/index')
def index():
    return '<html><body><h1>Hello, World! testing index page</h1></body></html>'
@app.route('/hello/<name>')
def hello_name(name):
    return'<html><body><h1>Hello %s!</h1></body></html>'%name
if __name__=='__main__':
    app.run(debug=False)
"""

from flask import Flask , render_template
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index4.html")
if __name__ == '__main__':
    app.run(debug =True)
"""
from flask import Flask , render_template
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('home2.html' )
if __name__=='__main__':
    app.run(debug =True)
    """