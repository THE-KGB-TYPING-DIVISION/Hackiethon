from flask import Flask, render_template, url_for, Response, request, redirect

import time
import random
from os import path

app = Flask(__name__)


@app.route('/home/')
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
    return render_template('homepage.html', joke=joke)

@app.route('/profile/<name>')
def profile(name):
    joke = 'maybe'
    return render_template("profile.html", name=name, joke=joke)

@app.route('/homepage/')
def homepage():
    return render_template("homepagePractice.html")

@app.route('/homepage/sike/')
def sike():
    return render_template("sikeSubpage.html")

@app.route('/homepage/note/')
def note():
    return render_template('notepage.html')### file_path=file_path, files=files)
    file_path = input("\nCreate file")
    
    files = open(file_path, 'a')

    line_count = 1

    while line_count > 0:
        try:
            line = input("\t"+str(line_count)+" ")
            files.write(line)
            files.write('\n')
            line_count += 1
        except KeyboardInterrupt:
            print("\n\n\tClosing...")
            break
"""@app.route('/homepage/note/')
def countdown(t):
    while t:
        mins, secs = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer,end = "\r")
        time.sleep(1)
        t -= 1
    print("end timer")
countdown(10)"""



if __name__ == '__main__':
    app.run(debug=True)