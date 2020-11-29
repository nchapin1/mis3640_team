from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# APP SETUP
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db" 
app.config['SECRET_KEY'] = 'asldkf0cm0iasfew'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# DATABASE TABLE SETUP
class Users(db.Model):
    id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    email = db.Column(db.String(50))
    phone = db.Column(db.Integer)
    password = db.Column(db.String(30))

    def __init__(self, username, email, phone, password):
        self.username = username
        self.email = email
        self.phone = phone
        self.password = password
    
    def __str__(self):
        return self.username

