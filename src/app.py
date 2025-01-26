from flask import Flask, render_template
import Events as e

"""
    this file is to communicate with script.js
"""

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start_game", methods=['POST'])
def start_game():
    return e.start()

@app.route("/choice_1", methods=['POST'])
def choice_1():
    return e.choice_made(1)

@app.route("/choice_2", methods=['POST'])
def choice_2():
    return e.choice_made(2)

@app.route("/new_event", methods=['POST'])
def new_event():
    return e.get_event()
