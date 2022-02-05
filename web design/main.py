#from crypt import methods
from cProfile import label
from enum import unique
from unicodedata import name
from flask import Flask, flash ,render_template, request ,redirect, url_for ,session 

import psycopg2
import os
import secrets
import re


app=Flask(__name__)

app.config['SECRET_KEY'] = 'clintoo333david0000'
conn=psycopg2.connect("dbname='duka' user='postgres' host='localhost' password='5132'")




@app.route('/')
def home():
    return  render_template("index.html") 

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/achievements")
def achievement():
    return render_template("achievements.html")

@app.route("/about")
def about():
    return render_template("about.html")      

@app.route("/signup" ,methods=["GET", "POST"])
def sinup():
    msg=''
    if request.method=="POST" and 'first_name' in request.form and 'second_name' in request.form and 'password' in request.form and 'email' in request.form:
        cur=conn.cursor()

        first_name=request.form["first_name"]
        second_name=request.form["second_name"],
        email=request.form["email"],
        password=request.form["password"]

        
        if "@" in email and "." in email :
          msg="welcome"
        else:
          msg="invalid email try again "
       
        
      
        query="INSERT INTO users( first_name, second_name, email, password )VALUES ( %s, %s, %s,%s )"
        rows=(first_name,second_name ,email,password)
        cur.execute=(query ,rows)
        
        conn.commit()
        
        cur.fetchall()
        msg = 'You have successfully registered!'
    


    return redirect(url_for("home" ,msg=msg)) 



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