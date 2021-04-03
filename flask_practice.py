from flask import Flask, render_template, url_for, Response, request, redirect

import random

app = Flask(__name__)

@app.route('/homepage/')
def home():
    joke = 'rand'
    numb = random.randint(1,5)
    if numb == 1:
        joke = "Why did Steve fall off the tractor? Because Steve was a strawberry"
    elif numb == 2:
        joke = "My wife told me to stop acting like a flamingo. So I had to put my foot down"
    elif numb == 3:
        joke = "Did you hear about the mathematician who was afraid of negative numbers? He’ll stop at nothing to avoid them."
    elif numb == 4:
        joke = "Did you hear about the restaurant called Karma? There is no menu, you get what you deserve"
    elif numb == 5:
        joke = "Did you hear about the actor who fell through the floorboards? He was probably just going through a stage."
    return render_template('homepagePractice.html', joke=joke)


@app.route("/profile/<name>")
def profile(name):
    joke = 'maybe'
    return render_template("profile.html", name=name, joke=joke)

@app.route("/homepage/")
def homepage():
    return render_template("homepagePractice.html")

@app.route("/homepage/sike/")
def sike():
    return render_template("sikeSubpage.html")


if __name__ == '__main__':
    app.run(debug=True)