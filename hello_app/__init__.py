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

from dash import Input, Output, callback

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


index_page = html.Div([
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
])

page_1_layout = html.Div([
    html.H1('Page 1'),
    dcc.Dropdown(['LA', 'NYC', 'MTL'], 'LA', id='page-1-dropdown'),
    html.Div(id='page-1-content'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
    html.Br(),
    dcc.Link('Go back to home', href='/'),
])

@callback(Output('page-1-content', 'children'),
              [Input('page-1-dropdown', 'value')])
def page_1_dropdown(value):
    return f'You have selected {value}'


page_2_layout = html.Div([
    html.H1('Page 2'),
    dcc.RadioItems(['Orange', 'Blue', 'Red'], 'Orange', id='page-2-radios'),
    html.Div(id='page-2-content'),
    html.Br(),
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go back to home', href='/')
])

@callback(Output('page-2-content', 'children'),
              [Input('page-2-radios', 'value')])
def page_2_radios(value):
    return f'You have selected {value}'


# Update the index
@callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    else:
        return index_page
    # You could also return a 404 "URL not found" page here

@server.route("/dash")
def my_dash_app():
    return app.index()
