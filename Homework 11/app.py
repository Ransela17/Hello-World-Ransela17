from flask import Flask, render_template, url_for,redirect

app = Flask(__name__)


##Get Blueprint Assignment 10 And Register
from pages.Assignment10.assigment10 import Users
app.register_blueprint(Users)


if __name__ == '__main__':
    app.run(debug=True)
