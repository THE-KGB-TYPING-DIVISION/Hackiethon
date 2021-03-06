from flask import Flask, render_template, url_for, Response, request, redirect

import time
import random
from os import path

app = Flask(__name__)

@app.route('/homepage/rick_astley')
def ricky():
    return render_template('rick_astley.html')

@app.route('/homepage/')
def homepage():
    return render_template('homepagePractice.html')

@app.route('/homepage/about')
def about():
    return render_template('about.html')

@app.route('/homepage/sike/')
def sike():
    return render_template("sikeSubpage.html")

@app.route('/homepage/note/')
def note():
    return render_template('webnotes.html')
@app.route('/homepage/timer')
def countdown():
    return render_template('timer.html')

@app.route('/homepage/dinogame')
def dino():
    return render_template('dinoGame.html')

if __name__ == '__main__':
    app.run(debug=True)