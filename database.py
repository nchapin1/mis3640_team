from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.engine import create_engine

# from sqlalchemy.ext.compiler import compiles
# from sqlalchemy.sql.expression import Executable, ClauseElement
engine = create_engine("sqlite:///users.db", echo=True)
meta = MetaData(engine)


# SQLALCHEMY
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SECRET_KEY"] = "asldkf0cm0iasfew"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True


db = SQLAlchemy(app)

from flask_security import (
    Security,
    SQLAlchemyUserDatastore,
    UserMixin,
    RoleMixin,
    login_required,
)

roles_users = db.Table(
    "roles_users",
    db.Column("user_id", db.Integer(), db.ForeignKey("user.username")),
    db.Column("role_id", db.Integer(), db.ForeignKey("role.id")),
)


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


from flask_mail import Mail

app.config["MAIL_SERVER"] = "smtp.example.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "username"
app.config["MAIL_PASSWORD"] = "password"
mail = Mail(app)

# USER CLASS SETUP
class User(db.Model, UserMixin):
    def __init__(self, username, email, phone, password):
        self.username = username
        self.email = email
        self.phone = phone
        self.password = password

    def __str__(self):
        return self.username

    __tablename__ = "user"
    username = db.Column(db.String(30), primary_key=True)
    email = db.Column(db.String(50))
    phone = db.Column(db.Integer)
    password = db.Column(db.String(30))
    cryptos = db.relationship(
        "Crypto", lazy="select", backref=db.backref("user", lazy="joined")
    )


# CRYPTO CLASS SETUP
class Crypto(db.Model, UserMixin):
    def __init__(self, symbol, purchase, current, target, tolerance, username_id):
        self.symbol = symbol
        self.purchase = purchase
        self.current = current
        self.target = target
        self.tolerance = tolerance
        self.username_id = username_id

    __tablename__ = "crypto"
    symbol = db.Column(db.String(30), primary_key=True)
    purchase = db.Column(db.Numeric(10))
    current = db.Column(db.Numeric(10))
    target = db.Column(db.Numeric(10))
    tolerance = db.Column(db.Numeric(10))
    username_id = db.Column(db.String, db.ForeignKey("user.username"), nullable=False)

    def __str__(self):
        return self.username


db.create_all()
