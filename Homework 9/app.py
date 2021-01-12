from flask import Flask, render_template, url_for, redirect, request, session

app = Flask(__name__)
app.secret_key = '123'

@app.route('/')
def home():
    return redirect(url_for('assignment9'))

@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    search, username, = '',''
    users = ({'first_name':"Michael", 'last_name':"Lawson", 'email':"michael.lawson@reqres.in"},
             {'first_name':"Lindsay", 'last_name':"Ferguson", 'email':"lindsay.ferguson@reqres.in"},
             {'first_name':"Tobias", 'last_name':"Funke", 'email':"tobias.funke@reqres.in"},
             {'first_name':"Byron", 'last_name':"Fields", 'email':"byron.fields@reqres.in"},
             {'first_name':"George", 'last_name':"Edwards", 'email':"george.edwards@reqres.in"},
             {'first_name':"Rachel", 'last_name':"Howell", 'email':"rachel.howell@reqres.in"})

    if request.method == 'POST':
        username = request.form['nickname']
        session['logged_in'] = True
        session['username'] = username

    if request.method == 'GET':
        if 'searchfield' in request.args:
            search = request.args['searchfield']
            return render_template('assignment9.html', search=search, users=users)

    return render_template('assignment9.html', request_method=request.method, username=username)

@app.route('/log_out')
def log_out():
    session['logged_in'] = False
    return redirect(url_for('assignment9'))


if __name__ == '__main__':
    app.run(debug=True)
