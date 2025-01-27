import flask
# from flask_cors import CORS
import Events as e

"""
    this file is to communicate with script.js
"""

app = flask.Flask(__name__)
@app.route("/")
def home():
    return flask.render_template('index.html')

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

@app.errorhandler(404)
def not_found(error):
    return {"error": "Invalid route"}, 404


if __name__ == "__main__":
    app.run(debug=True)
