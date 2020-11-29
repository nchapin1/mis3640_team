# TODO:
# 1. can regular app route pages be added into the functional app route pages? HTML header links refer to "url_for"
from flask import Flask, render_template, request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from database import db, Users, app
db.create_all()

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


# LOGIN PAGE
@app.route("/login/", methods=['GET','POST'])
def login_user():
    if request.method=="POST":
        input_username = request.form['uname'],
        input_password = request.form['password']
    #     query_username = Users.query.filter_by(username=input_username).first()
    #     query_password = Users.query.filter_by(password=input_password).first()

    #     if input_username == query_username and input_password == query_password:
    #         return redirect(url_for('home'))
    # return render_template("login.html")

    #     Session = sessionmaker(bind=engine)
    #     s = Session()
    #     query = s.query(Users).filter(Users.username==input_username, Users.password==input_password)
    #     result = query.first()
    #     if result:
    #         return redirect(url_for('home'))
    #     else:
    #         flash('wrong password')
    # return render_template("login.html")
    


# SIGN UP CREATE USER
@app.route("/signup/", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        user = Users(
        username=request.form["uname"],
        email=request.form["email"],
        phone=request.form["pnumber"],
        password=request.form["password"])
    
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('signup.html')

    # WORKS return render_template('home.html', user=user)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)