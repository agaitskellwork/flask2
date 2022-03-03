#from flask import Flask  # Import the Flask class
#app = Flask(__name__)    # Create an instance of the class for our use

import flask
import dash
server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server,  url_base_pathname='/dash')

app.layout = html.Div(id='dash-container')

@server.route("/dash")
def my_dash_app():
    return app.index()
