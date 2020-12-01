from flask import Flask, render_template, request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.ext.indexable import index_property
from flask_mail import Mail, Message
import json
from requests import Session
import os
from models import User, Crypto, db, app
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
# https://github.com/mattupstate/flask-security/issues/198
#from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
#from sqlalchemy.engine import create_engine

#engine = create_engine("sqlite:///users.db", echo=True)
#meta = MetaData(engine)

below_threshold_subject = "{symbol} is below the threshold!"
below_threshold_body = "Hello {username},\n\n This is a notification to alert you that {symbol} is below the threshold you have set!\n Please remove it to stop receiving these notifications.\n\nCrypto Team"
above_threshold_subject = "{symbol} is above the threshold!"
above_threshold_body = "Hello {username},\n This is a notification to alert you that {symbol} is above the threshold you have set!\n Please remove it to stop receiving these notifications.\n\nCrypto Team"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SECRET_KEY"] = "asldkf0cm0iasfew"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True


db = SQLAlchemy(app)


app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True  # False
app.config["MAIL_USERNAME"] = "donotreply.cryptosafe@gmail.com"
app.config["MAIL_PASSWORD"] = "mis3640!"
app.config["MAIL_DEFAULT_SENDER"] = "donotreply.cryptosafe@gmail.com"
mail = Mail(app)

def check_prices():
    for crypto_item in db.session.query(Crypto).all():
        current_price = crypto_current(crypto_item.symbol)
        if crypto_item.purchase * ((crypto_item.target / 100) + 1) >= current_price:
            user = User.query.get(crypto_item.username_id)
            print(user)
            # app.app_context()
            with app.app_context():
                msg = Message()
                mail.send_message(subject=above_threshold_subject.format(symbol=crypto_item.symbol),
                        body=above_threshold_body.format(username=user.username,symbol=crypto_item.symbol),
                        recipients=[user.email])
        if crypto_item.purchase * (1-(crypto_item.tolerance / 100)) <= current_price:
            user = User.query.get(crypto_item.username_id)
            # app.app_context()
            with app.app_context():
                msg = Message()
                mail.send_message(subject=below_threshold_subject.format(symbol=crypto_item.symbol),
                        body=below_threshold_body.format(username=user.username,symbol=crypto_item.symbol),
                        recipients=[user.email])
        crypto_item.current = current_price
    db.session.commit()
    for crypto_item in db.session.query(Crypto).all():
        print("THE CURRENT PRICE OF", crypto_item.symbol,"IS",crypto_item.current)

scheduler = BackgroundScheduler()
scheduler.add_job(func=check_prices, trigger="interval", seconds=10)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

def crypto_current(symbol):
    """Uses api to gather latest crypto prices. Symbol allows for desired crypto to be identified. 
    
    Keyword arguments: 
    symbol -- user input for desired crypto asset from homepage. 
    """
    url = "https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    parameters = {
        "start": "1",
        "limit": "5000",
        "convert": "USD",
    }
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": "b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c",
    }

    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    raw = json.loads(response.text)
    data = raw["data"]

    current = 0

    for item in data:
        if item["symbol"] == symbol:
            current = item["quote"]["USD"]["price"]
            break
    return current


@app.errorhandler(404)
def page_not_found(error):
    """404 errors are routed to error page.  
    """
    return render_template("page_not_found.html"), 404


@app.route("/")
def index():
    """Directs user to the general landing page. Equivalent to logging off.  
    """
    return render_template("index.html")


@app.route("/login/")
def login():
    """Directs user to login page.  
    """
    return render_template("login.html")


@app.route("/login_user_request", methods=["GET", "POST"])
def login_request():
    """Collects login form information. If the entry matches the database query, redirects to the homepage.
    """
    if request.method == "POST":
        input_username = str(request.form["uname"])
        input_password = str(request.form["password"])
        user = User.query.get(input_username)
        username = str(user.username)
        password = str(user.password)
        if input_username == username and input_password == password:
            return redirect(url_for("home", username=username))
        else:
            flash("Incorrect Username or Password", "error")


@app.route("/registration")
def register():
    """Directs user to registration page.  
    """
    return render_template("register.html")


@app.route("/registration_user_request", methods=["GET", "POST"])
def register_request():
    """Collects registration form information and creates new user object. Redirects to homepage. 
    """
    if request.method == "POST":
        username = str(request.form["uname"])
        email = str(request.form["email"])
        phone = str(request.form["pnumber"])
        password = str(request.form["password"])
        print()

        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists','error')
            return redirect(url_for('register'))

        new_user = User(username, email, phone, password)
        db.session.add(new_user)
        db.session.commit()
    return redirect(url_for("home", username=username))


@app.route("/home_page/<username>")
def home(username):
    """Uses the User object's username property to display all child Crypto objects. Users can add or remove assets within the data table.  
    
    Keyword arguments:
    username -- User object's primary key.
    """
    rows = Crypto.query.filter_by(username_id=username).all()
    return render_template(
        "home.html", username=username, title="Investments", rows=rows
    )


@app.route("/home_page_add/<username>", methods=["GET", "POST"])
def add_crypto(username):
    """Uses the User object's username property as a foreign key to create a child Crypto object. 

    Keyword arguments:
    username -- User object's primary key.
    """
    if request.method == "POST":
        symbol = str(request.form["symbol"])
        purchase = int(request.form["purchase"])
        current = int(crypto_current(symbol))
        target = int(request.form["target"])
        tolerance = int(request.form["tolerance"])
        username_id = str(username)

        new_crypto = Crypto(symbol, purchase, current, target, tolerance, username_id)
        print(new_crypto)
        db.session.add(new_crypto)
        db.session.commit()
        flash("Good")
    return redirect(url_for("home", username=username))

@app.route("/home_page_remove/<username>", methods=["GET", "POST"])
def remove_crypto(username):
    """Uses the User object's username property as a foreign key to delete a child Crypto object. 

    Keyword arguments:
    username -- User object's primary key.
    """
    if request.method == "POST":
        username = str(username)
        symbol = request.form["symbol"]
        crypto_val = Crypto.query.filter_by(username_id=str(username),symbol=request.form["symbol"]).first()
        dbsession = db.session.object_session(crypto_val)
        dbsession.delete(crypto_val)
        dbsession.commit()
        flash("Good")
    return redirect(url_for("home", username=username))

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)