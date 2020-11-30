from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import Executable, ClauseElement
engine = create_engine('sqlite:///user.db', echo = True)
meta=MetaData(engine)


# APP SETUP
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db" 
app.config['SECRET_KEY'] = 'asldkf0cm0iasfew'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy()

# class CreateView(Executable, ClauseElement):
#     def __init__(self, username, email, phone, password):
#         self.username = username
#         self.email = email
#         self.phone = phone
#         self.password=password

# @compiles(CreateView)
# def visit_create_view(element, compiler, **kw):
#     return "CREATE VIEW %s AS %s" % (
#          element.name,
#          compiler.process(element.select, literal_binds=True)
#          )

# DATABASE TABLE SETUP
user = Table(
    'users', meta,
    Column('id', Integer, primary_key = True), 
    Column('username', String), 
    Column('email', String), 
    Column('phone', Integer),
    Column('password', String),
)
user.create()

# # create view
# createview = CreateView('viewname', users.select().where(users.c.id>5))
# engine.execute(createview)

# # reflect view and print result
# v = Table('viewname', meta, autoload=True)
# for r in engine.execute(v.select()):
#     print (r)

# meta.create_all(engine)

# DATABASE CLASS SETUP
class User(db.Model):
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
