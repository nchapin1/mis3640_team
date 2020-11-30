from flask import Flask, render_template, request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from database import db, User, app

# ERROR PAGE
@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404


# INDEX PAGE
@app.route("/")
def index():
    return render_template("index.html")

# HOME
@app.route("/home/")
def home():
    return render_template("home.html")

# LOGIN PAGE
@app.route("/login/", methods=['GET', "POST"])
def login_user():
    # if request.method=="POST":
    input_username = str(request.form['uname']),
    input_password = str(request.form['password'])
    if input_username and input_password:
        existing_user = User.query.filter(
            User.username == input_username and User.email == input_password
        ).first()
        if existing_user:
            return render_template("home.html")
        else:
            flash('not working', "error")


        query_username = User.query.get(input_username)
        # query_username = Users.query.filter_by(username=input_username)
        # query_password = Users.query.filter_by(password=input_password)

        # if input_username == query_username and input_password == query_password:
        #     return redirect(url_for('home'))
        return render_template("home.html", input_username=input_username, input_password=input_password, query_username=query_username)
    return render_template("login.html")


# SIGN UP CREATE USER
@app.route("/signup/", methods=["GET", "POST"])
def create_user():
    
    if request.method == "POST":
        user = User(
        username=request.form["uname"],
        email=request.form["email"],
        phone=request.form["pnumber"],
        password=request.form["password"])
    
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('signup.html')
    # return render_template('signup.html')

    # WORKS return render_template('home.html', user=user)

# if __name__ == '__main__':
#     db.create_all()
#     app.run(debug=True)




# @app.route("/", methods=["GET"])
# def user_records():
#     """Create a user via query string parameters."""
#     username = request.args.get("user")
#     email = request.args.get("email")
#     if username and email:
#         existing_user = User.query.filter(
#             User.username == username or User.email == email
#         ).first()
#         if existing_user:
#             return make_response(f"{username} ({email}) already created!")
#         new_user = User(
#             username=username,
#             email=email,
#             created=dt.now(),
#             bio="In West Philadelphia born and raised, \
#             on the playground is where I spent most of my days",
#             admin=False,
#         )  # Create an instance of the User class
#         db.session.add(new_user)  # Adds new User record to database
#         db.session.commit()  # Commits all changes
#         redirect(url_for("user_records"))
#     return render_template("users.jinja2", users=User.query.all(), title="Show Users")