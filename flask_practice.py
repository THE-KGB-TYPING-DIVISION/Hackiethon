from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home()
    return render_template('homepage.html')
    

@app.route('/joke/<int:numb>')
def random_joke(numb):
    if numb == 1:
        return "Why did Steve fall off the tractor ............ because Steve was a strawberry"
    elif numb == 2:
        print("My wife told me to stop acting like a flamingo")
        print("So I had to put my foot down")
    elif numb == 3:
        print("Did you hear about the mathematician")
        print("He’ll stop at nothing to avoid them.")
    elif numb == 4:
        print("Did you hear about the restaurant called Karma?")
        print("There is no menu, you get what you deserve")
    elif numb == 5:
        print("Did you hear about the actor who fell through the floorboards?")
        print("He was probably just going through a stage.")
    return 'hi'

@app.route("/profile/<name>")
def profile(name):
    return render_template("profile.html", name=name)


if __name__ == '__main__':
    app.run(debug=True)