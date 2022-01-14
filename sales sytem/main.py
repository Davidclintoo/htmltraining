#print("yes")
from flask import Flask ,render_template 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, clintoo!'

@app.route('/contact')
def nai():
    return 'nai!'

   
@app.route('/inventory')
def inventory():
    return render_template("inventory.html")

@app.route('/home')
def home():
    return  render_template("home.html")   
app.run()
