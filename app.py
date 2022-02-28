from flask import Flask, render_template, request, url_for, redirect, session, jsonify
from flask_mysqldb import MySQL, MySQLdb
import mysql.connector

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'blixentech'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/register',methods=["GET","POST"])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        nameU = request.form['nameU']
        emailU = request.form['emailU']
        numberU = request.form['numberU']
        passwordU = request.form['passwordU'].encode('utf-8')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO usuario(name,email,password, number) VALUES(%s,%s,%s,%s)",(nameU, emailU, passwordU, numberU,))
        mysql.connection.commit()
        data = "Registred sucessfully"
        return render_template('register.html', data= data)

@app.route('/login',methods=["GET","POST"])
def login():
    cur = mysql.connection.cursor()
    if request.method == "POST":
        signup = request.form
        email = signup['email']
        password = signup['password']
        session['email'] = request.form['email']
        if 'email' in session:
            s=session['email']
            cur.execute("SELECT * FROM employee WHERE email='" +email+"' and password='"+password+"'")
            account = cur.fetchone()
            if account:
                username = cur.execute("SELECT username FROM employee WHERE email='" +email+"'")
                data = cur.fetchone()
                return render_template("crud.html", name=data)
            else:
                return render_template("error.html")
    else:
        return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))

@app.route('/loginUser',methods=["GET","POST"])
def loginUser():
    cur = mysql.connection.cursor()
    if request.method == "POST":
        signup = request.form
        email = signup['email']
        password = signup['password']
        session['email'] = request.form['email']
        if 'email' in session:
            s = session['email']
            cur.execute("SELECT * FROM usuario WHERE email='" +email+"' and password='"+ password +"'")
            account = cur.fetchall()
            if account:
                username = cur.execute("SELECT name FROM usuario WHERE email='" + email +"'")
                data = cur.fetchone()
                return render_template("clientData.html", name=data)
            else:
                return render_template("error.html")
    else:
        return render_template("login.html")

@app.route('/store')
def store():
    return render_template('store.html')

@app.route('/crud')
def crud():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM product")
    data = cur.fetchall()
    cur.close()
    return render_template('crud.html',product= data)

@app.route('/employee')
def employee():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM employee")
    data = cur.fetchall()
    cur.close()
    return render_template('employee.html', product=data)

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuario")
    data = cur.fetchall()
    cur.close()
    return render_template('users.html', product=data)

@app.route('/clientData')
def clientData():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuario")
    data = cur.fetchall()
    cur.close()
    return render_template('clientData.html', product=data)

'''filter product'''
@app.route('/fetchrecords',methods=["GET","POST"])
def fetchrecords():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        query = request.form['action']
        minimum_price = request.form['minimum_price']
        maximum_price = request.form['maximum_price']
        if query == '':
            cur.execute("SELECT * FROM product ORDER BY prod_id ASC")
            productlist = cur.fetchall()
            print('all list')
        else:
            cur.execute("SELECT * FROM product WHERE price BETWEEN (%s) AND (%s)", [minimum_price, maximum_price])
            productlist = cur.fetchall()
    return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

@app.route('/insertProd', methods=["POST"])
def insertProd():
    name = request.form['name']
    type = request.form['type']
    price = request.form['price']
    qtd = request.form['qtd']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO product(name,type,price,quantity) VALUES (%s,%s,%s,%s)",(name,type,price,qtd))
    mysql.connection.commit()
    return redirect(url_for('crud'))


@app.route('/insertEmp', methods=["POST"])
def insertEmp():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO employee(username,email,password) VALUES (%s,%s,%s)", (username,email,password))
    mysql.connection.commit()
    return redirect(url_for('employee'))

@app.route('/update', methods=["POST"])
def update():
    id_data = request.form['id']
    name = request.form['name']
    type = request.form['type']
    price = request.form['price']
    qtd = request.form['qtd']
    img = request.form['image']
    cur = mysql.connection.cursor()
                                                    #name, typr, price, quantity vem antes de id_data
    cur.execute("UPDATE product SET  name= %s, type= %s, price = %s, quantity = %s, image = %s WHERE prod_id=%s",(name, type, price, qtd, img, id_data,))
    mysql.connection.commit()
    return redirect(url_for('crud'))

@app.route('/updateEmp', methods=["POST"])
def updateEmp():
    id_data = request.form['id']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE employee SET username= %s, email= %s, password = %s WHERE employee_id =%s",(username, email, password,id_data))
    mysql.connection.commit()
    return redirect(url_for('employee'))

@app.route('/updateUser', methods=["POST"])
def updateUser():
    id_data = request.form['id']
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    number = request.form['number']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE usuario SET name= %s, email= %s, password = %s, number=%s WHERE user_id  =%s", (name, email, password, number,id_data))
    mysql.connection.commit()
    return redirect(url_for('users'))

@app.route('/delete/<string:id_data>', methods=["GET"])
def delete(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM product WHERE prod_id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('crud'))

@app.route('/deleteUser/<string:id_data>', methods=["GET"])
def deleteUser(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM usuario WHERE user_id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('users'))

@app.route('/deletEmp/<string:id_data>', methods=["GET"])
def deleteEmp(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM employee WHERE employee_id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('employee'))


if __name__ == '__main__':
    app.secret_key = "hello"
    app.run(debug=True)
