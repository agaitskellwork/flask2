#from flask import Flask  # Import the Flask class
#app = Flask(__name__)    # Create an instance of the class for our use

import flask
import dash
from dash import html
from dash import dcc

from flask import render_template

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server,  url_base_pathname='/dash/')

#app.layout = html.Div(id='dash-container')
app.layout = html.Div([html.H1('Simple Layout',style={'textAlign':'center'})])

@server.route('/hi')
def hello():
    return 'Hi, World!'

@server.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@server.route("/dash")
def my_dash_app():
    return app.index()
