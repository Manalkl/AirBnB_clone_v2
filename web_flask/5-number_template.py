#!/usr/bin/python3
"""this is the flask number"""
from flask import Flask, render_template


AirBnB = Flask(__name__)
AirBnB.url_map.strict_slashes = False


@AirBnB.route("/")
def homepage():
    """home function"""
    return "Hello HBNB!"


@AirBnB.route("/hbnb")
def HBNBpage():
    """HBNH function"""
    return "HBNB"


@AirBnB.route("/c/<text>")
def Cpage(text):
    """home c function"""
    text = text.replace("_", " ")
    return f"C {text}"


@AirBnB.route("/python")
@AirBnB.route("/python/<text>")
def pythonpage(text="is cool"):
    """home python function"""
    text = text.replace("_", " ")
    return f"Python {text}"


@AirBnB.route("/number/<int:n>")
def numperpage(n):
    """home number function"""
    return f"{n} is a number"


@AirBnB.route("/number_template/<int:n>")
def NumperHtmlpage(n):
    """home number html function"""
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    AirBnB.run(host="0.0.0.0", port=5000)
