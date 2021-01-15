from flask import Flask, render_template, url_for, redirect, blueprints, session, request, Blueprint
import mysql.connector

Users = Blueprint('users', __name__, static_folder='static', static_url_path='/users', template_folder='templates')

#intataction with Data Base Function
def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost', user='root', passwd='root', database='newdb', auth_plugin='mysql_native_password')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statement
        # returns: the number of rows affected by query
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement
        # return: False if the query failed, or the result of the query if it succeeded
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value

# insert User to Data Base route and funcation
@Users.route('/insert_user', methods=['GET','POST'])
def insert_user():
    if request.method == 'POST':
        num_id = request.form['id']
        first_name = request.form['fname']
        last_name = request.form['lname']
        email = request.form['email']
        query = "INSERT into users (id, first_name, last_name, email) VALUES ('%s', '%s', '%s', '%s')" % (num_id, first_name, last_name, email)
        interact_db(query, 'commit')

    return redirect('/assignment10')

# Delete User to Data Base route and funcation
@Users.route('/delete_user', methods=['GET','POST'])
def delete_user():
    if request.method == 'POST':
        user_id = request.form['id']
        query = "DELETE FROM users WHERE id='%s';" % user_id
        interact_db(query, 'commit')

    return redirect('/assignment10')

# Update User Email by id route and function
@Users.route('/update_user')
def update_user():
    id_num = request.args['id']
    email = request.args['email']
    query = "UPDATE users SET email = '%s' WHERE id = '%s' " % (email, id_num)
    interact_db(query, query_type='commit')

    return redirect('/assignment10')

@Users.route('/')
@Users.route('/assignment10')
def users():
    query = "select * from users;"
    query_result = interact_db(query, query_type='fetch')
    return render_template('Assignment10.html', users=query_result)

