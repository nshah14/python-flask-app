from app import app
from flask import render_template, request
from app.forms import LoginForm, RegisterForm
from flask_mysqldb import MySQL

mysql = MySQL(app)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Naved'}
    posts = [
        {
            'author' : {'username' : 'Nargiza'},
            'body'   : 'Beautiful Day in Reading'
        },
        {
            'author' : {'username' : 'Aleyah'},
            'body'   : 'Beautiful day in the world'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    
    form = LoginForm()
    print ("iam in login")
    print("form %s", form)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register' , methods=['GET', 'POST'])
def register():
    
    form = RegisterForm()
    if request.method == "POST":
        print ("iam in post of registers")
        details = request.form
        firstName = details['name']
        lastName = details['lastname']
        username = details['username']
        password = details['password']
        # print("Name is :%s " % (str(firstName)))
        # print("Last name is  :%s " % (str(lastName)))
        # print("usernanme is :%s " % (str(username)))
        # print("password is : %s " % (str(password)))
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers(firstName, lastName, username, password ) VALUES (%s, %s, %s, %s)", (firstName, lastName, username,  password))
        mysql.connection.commit()
        cur.close()
        return render_template('login.html', title='Sign In', form=LoginForm())
    print ("iam in get register")
    return render_template('register.html', title='Register', form=form)

