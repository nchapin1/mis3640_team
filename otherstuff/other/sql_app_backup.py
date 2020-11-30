from flask import Flask, render_template, request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy


# app = Flask(__name__)

# CREATE DATABASE
# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///users.db', echo = True)

# from sqlalchemy import Table, Column, Integer, String, MetaData
# meta = MetaData()
# users = Table(
#    'users', meta,
#    Column('id', Integer, primary_key = True),
#    Column('username', String),
#    Column('email', String),
#    Column('phone', Integer),
#    Column('password', String),
# )
# meta.create_all(engine)

# APP SETUP
app = Flask(__name__)
db_name = "users.db"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_name
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

# DATABASE TABLE SETUP
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.Integer)
    password = db.Column(db.String)

    def __init__(self, username, email, phone, password):
        self.username = username
        self.email = email
        self.phone = phone
        self.password = password


# DATASET PAGE
@app.route("/dataset")
def dataset_page():
    return render_template("dataset.html")


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

    with app.open_resource("static/users.csv") as f:
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
        username=request.form["uname"],
        email=request.form["email"],
        phone=request.form["pnumber"],
        password=request.form["password"]

        record = User(username, email, phone, password)
        
        db.session.add(record)
        db.session.commit()
        return render_template('home.html', username=username)

        # return redirect("/signup")
    # return redirect(url_for("created_user"))

    # WORKS return render_template('home.html', user=user)
