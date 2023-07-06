from flask import Flask, render_template, request, redirect
from werkzeug.exceptions import abort
from flask_mysqldb import MySQL

application = Flask(__name__)
application.config['PROPAGATE_EXCEPTIONS'] = True
application.config['MYSQL_HOST']='localhost'
application.config['MYSQL_USER']='u1172195'
application.config['MYSQL_PASSWORD']='root'
application.config['MYSQL_DB']='u1172195_tg'

# все ломает
# сделал вручную
# db = MySQL.connect('localhost', 'u1172195', 'root', 'u1172195_tg')


mysql=MySQL(application)

@application.route("/")
def hello():
   return "<h1 style='color:blue'>Hello There!</h1>"

# пока нах не нужен
@application.route("/about")
def about():
    return "/about is working"


@application.route('/secret', methods=['POST'])
def secret():
    if request.method=='POST':
        userDetails=request.form
        name=userDetails['name']
        email=userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name,email)  VALUES(%s,%s)",(name, email))
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    return render_template('site.html')

@application.route('/', methods=['DELETE'])
def delete():
    if request.method=='DELETE':
        userDetails=request.form
        email=userDetails['email']
        name=userDetails['name']
        cur = mysql.connection.cursor()
        mysql.connection.delete("DELETE FROM users(name,email)  VALUES(%s,%s)",(name, email))
        mysql.connection.commit()
        cur.close()
        return redirect('/users.html')
    return render_template('site.html')


@application.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue=cur.execute("SELECT * FROM users")
    if resultValue>0:
        userDetails=cur.fetchall()
        return render_template('users.html', userDetails=userDetails)

# @application.route('/delete', method= ['POST', 'GET'])
# def delete():
#     cur = mysql.connection.cursor()
#     deleted=cur.execute("SELECT * FROM users")
#     if deleted>0:
#         userDeleted=cur.fetchall()
#         return render_template('delete.html', userDeleted=userDeleted)


if __name__ == "__main__":
   application.run(debug=True)