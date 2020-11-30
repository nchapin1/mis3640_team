from flask import Flask, render_template, request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.indexable import index_property
from flask_mail import Mail
import json
from requests import Session
import os
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.engine import create_engine


# engine = create_engine("sqlite:///users.db", echo=True)
# meta = MetaData(engine)


app = Flask(__name__)
db = SQLAlchemy(app)


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SECRET_KEY"] = "asldkf0cm0iasfew"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)


app.config["MAIL_SERVER"] = "smtp.mail.yahoo.com"
app.config["MAIL_PORT"] = 587
# app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = True #False
app.config["MAIL_USERNAME"] = os.environ.get("EMAIL_USER")
app.config["MAIL_PASSWORD"] = os.environ.get("EMAIL_PASS")
mail = Mail(app)


def crypto_current(symbol):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    parameters = {
        "start": "1",
        "limit": "5000",
        "convert": "USD",
    }
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": "ce4157ad-edeb-4e93-83f0-bb977f31d3e3",
    }

    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    raw = json.loads(response.text)
    data = raw['data']

    for item in data:
        if item["symbol"] == symbol:
            current = item["quote"]["USD"]["price"]
            break
    return current


# USER CLASS SETUP
class User(db.Model):
    def __init__(self, username, email, phone, password):
        self.username = username
        self.email = email
        self.phone = phone
        self.password = password

    def __str__(self):
        return self.username

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    email = db.Column(db.String(50))
    password = db.Column(db.String(30))
    crypto = db.relationship(
        "Crypto", backref="user", lazy=True)
    
# CRYPTO CLASS SETUP
class Crypto(db.Model):
    def __init__(self, symbol, purchase, current, target, tolerance, username_id):
        self.symbol = symbol
        self.purchase = purchase
        self.current = current
        self.target = target
        self.tolerance = tolerance
        self.username_id = username_id

    symbol = db.Column(db.String(30), primary_key=True)
    purchase = db.Column(db.Numeric(10))
    current = db.Column(db.Numeric(10))
    target = db.Column(db.Numeric(10))
    tolerance = db.Column(db.Numeric(10))
    username_id = db.Column(db.String, db.ForeignKey("user.username"), nullable=False)

db.create_all()

# ERROR PAGE
@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404

# INDEX PAGE
@app.route("/")
def index():
    return render_template("index.html")

# @app.route('/login/')
# def login():
#     return render_template('login.html')

# LOGIN PAGE
@app.route("/login_user_request", methods=["GET", "POST"])
def login_request():
    if request.method == "POST":
        input_username = str(request.form["uname"])
        input_password = str(request.form["password"])
        username = str(User.query.get(input_username))
        password = str(User.query.filter_by(password=input_password).first())
        if input_username == username and input_password == password:
            # return render_template('home.html', username = username)
            return redirect(url_for('homepage', username=username))
        else:
            flash('Incorrect Username or Password', 'error')
    return render_template('login.html')
# https://github.com/mattupstate/flask-security/issues/198

# @app.route('/registration/')
# def register():
#     return render_template("register.html")

# SIGN UP CREATE USER
@app.route("/registration_user_request", methods=["GET", "POST"])
def register_request():
    if request.method == "POST":
        username = str(request.form["uname"])
        email = str(request.form["email"])
        phone = str(request.form["pnumber"])
        password = str(request.form["password"])

        new_user = User(username, email, phone, password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('homepage', username=username))  
    return render_template('register.html') 

# HOME
@app.route("/home_page/<username>")
def homepage(username):
    rows = Crypto.query.all()
    return render_template("home.html", title="Investments", rows=rows)
    

       
