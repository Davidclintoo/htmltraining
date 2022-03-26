#from crypt import methods
from cProfile import label
from enum import unique
from unicodedata import name
from flask import Flask, flash ,render_template, request ,redirect, url_for ,session, flash

import psycopg2
import psycopg2.extras
import os
import secrets
import re


app=Flask(__name__)

app.config['SECRET_KEY'] = 'clintoo333david0000'
conn=psycopg2.connect("dbname='duka' user='postgres' host='localhost' password='5132'")




@app.route("/")
def home():
    return  render_template("index.html") 



@app.route("/achievements")
def achievement():
    return render_template("achievements.html")

@app.route("/about")
def about():
    return render_template("about.html") 

@app.route("/contact")
def contact():
    return render_template("contact.html")     

@app.route("/signup" ,methods=["GET", "POST"])
def sinup():
    msg=''
    if request.method=="POST" and 'first_name' in request.form and 'second_name' in request.form and 'password' in request.form and 'email' in request.form:
        cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        first_name=request.form["first_name"]
        second_name=request.form["second_name"],
        email=request.form["email"],
        password=request.form["password"]
        cur.execute("SELECT  * from users  where first_name =first_name , second_name=second_name , email=email , password=password  ;" )
        account = cur.fetchone()

        
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', first_name):
            msg = 'Username must contain only characters and numbers !'
        elif not first_name or  not second_name or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cur.execute("INSERT INTO public.users(id, first_name, second_name, email, password)VALUES (null, %s, %s, %s, %s);")
            conn.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('contact.html', msg = msg)
        
       



@app.route("/login" ,methods=["GET", "POST"])
def login():
    msg = ''
    if request.method=="POST" and 'email' in request.form and 'password' in request.form:
        cur=conn.cursor()

        
        email=request.form["email"],
        password=request.form["password"]
        query=("SELECT * from users where 'email'=%s and 'password'=%s ")
        row= (email ,password)
        cur.execute(query,row)
        users=cur.fetchone()
        conn.commit

        if  users:
            session['loggedin'] = True
            session['id'] =  users['id']
            session['email'] =  users['email']
            return 'Logged in successfully!'
        else:
            msg = 'Incorrect email/password!'

    return redirect(url_for("home" ,msg=msg)) 
    
@app.route('/login/logout')
def logout():
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('email', None)
   return redirect(url_for('contact'))


app.run(debug=True)    