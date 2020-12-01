from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.engine import create_engine

app = Flask(__name__)
db = SQLAlchemy(app)

engine = create_engine("sqlite:///users.db", echo=True)
meta = MetaData(engine)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SECRET_KEY"] = "asldkf0cm0iasfew"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


class User(db.Model):
    """User database model."""

    def __init__(self, username, email, phone, password):
        self.username = username
        self.email = email
        self.phone = phone
        self.password = password

    def __str__(self):
        return self.username

    username = db.Column(db.String(30), primary_key=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(30))
    crypto = db.relationship("Crypto", backref="user", lazy=True)


class Crypto(db.Model):
    """Crypto database model."""

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