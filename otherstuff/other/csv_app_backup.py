from flask_sqlalchemy import SQLAlchemy
import _pickle as pickle
import csv
import os
import tablib

app = Flask(__name__)
    
# DATASET PAGE
@app.route('/dataset')
def dataset_page():
    return render_template('dataset.html')

# ERROR PAGE
@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404

# INDEX PAGE
@app.route("/")
def index():
    return render_template("index.html")

# HOME PAGE
@app.route("/home/")
def home():
    return render_template("home.html")

# HOME PAGE CREATED USER
@app.route("/home/<username>")
def created_user(username):
    # with open('users.txt', 'r') as f:
    #     return render_template("home.html", text=f.read())

    with app.open_resource('static/users.csv') as f:
        content = f.read()
    return render_template("home.html", username=username)

# LOGIN PAGE
@app.route("/login/")
def login_page():    
    return render_template("login.html")

# SIGN UP PAGE
@app.route("/signup/")
def signup_page():
    return render_template("signup.html")

# SIGN UP CREATE USER 
@app.route("/signup/", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        username = request.form["uname"]
        email = request.form["email"]
        phone = request.form["pnumber"]
        password = request.form["password"]
        fieldnames = ['username', 'email', 'phone', 'password']

        with open('static/users.csv', 'a') as inFile:
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)
            writer.writerow({'username':username, 'email':email, 'phone':phone, 'password':password})
        
    return redirect(url_for("created_user", username=username))

    # WORKS return render_template('home.html', user=user)
    