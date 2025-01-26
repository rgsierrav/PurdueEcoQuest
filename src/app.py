from flask import Flask, render_template
import Events as e

"""
    this file is to communicate with script.js
"""

app = Flask(__name__)

@app.route("/start_game", methods=['POST'])
def start_game():
    e.PurdueEcoQuest()
