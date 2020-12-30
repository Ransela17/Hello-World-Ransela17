from flask import Flask
from flask import render_template, url_for


# creates a Flask application, named app
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/8")
def assignment8():
    return render_template('assignment8.html',
                           user={'firstname': "Ran", 'lastname': "Sela"},
                           family=['Itzhak', 'Miryam', 'Mor', 'Kobi', 'Matan'])


@app.route("/userlist")
def userlist():
    return render_template('userlist.html')


@app.route("/blocktry")
def block():
    return render_template('blocktry.html')


# run the application
if __name__ == "__main__":
    app.run(debug=True)
