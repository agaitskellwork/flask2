from datetime import datetime
from flask import Flask, render_template
#from . import app
from . import server

@server.route("/")
def home():
    return render_template("home.html")

@server.route("/about/")
def about():
    return render_template("about.html")

@server.route("/contact/")
def contact():
    return render_template("contact.html")

@server.route("/hello/")
@server.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@server.route("/api/data")
def get_data():
    return server.send_static_file("data.json")
