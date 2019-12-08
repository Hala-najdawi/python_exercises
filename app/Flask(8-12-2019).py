#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 16:00:00 2019

@author: owner
"""
"""
#Exercise 1:
from flask import Flask
app=Flask(__name__)
@app.route('/')
def index():
    return 'This is the Index page'
@app.route('/hello')
def hello():
    return "Hello World!"
    """
#EX2:
"""    
from flask import Flask ,render_template
app=Flask(__name__)
@app.route('/index/<int:score>')
def index(score):
    return render_template('hello.html',marks=score)
if __name__=='__main__':
    app.run()
"""
#EX 3:
from flask import Flask , render_template
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('EX3.html' )
if __name__=='__main__':
    app.run(debug =True)    