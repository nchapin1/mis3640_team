if os.path.exists('static/users.txt'):
    with open('static/users.txt', 'rb') as rfp:
        users = pickle.load(rfp)
    users.append(user)
    with open('static/users.txt', 'wb') as wfp:
        pickle.dump(users, wfp)
    with open('static/users.txt', 'rb') as rfp:
        users = pickle.load(rfp)

 with open('static/users.txt', 'a') as f:
            for key, value in user.items():
                f.write('%s:%s\n' % (key, value))
                
# SCRAP CODE
# with open("users.txt", 'w') as fo:
#     fo.write(username, email, phone, password)
#     fo.close()
# return redirect(url_for('create_user', username = username, email = email, phone = phone, password = password))
# db.insert('username': request.form['uname'], 'email':request.form['email'], 'phone':request.form['pnumber'], 'password':request.form['password'])



# @app.route("/signup/")
# def signup_page():
#     return render_template("signup.html")


# @app.route("/signup", methods=["GET", "POST"])
# def create_user():
#     # ADD TO THE CSV
#     if request.method == "POST":
#         username = request.form["uname"]
#         email = request.form["email"]
#         phone = request.form["pnumber"]
#         password = request.form["password"]
#         user = {
#             "username": username,
#             "email": email,
#             "phone": phone,
#             "password": password,
#         }
#         # with open("users.txt", "w") as fo:
#             # fo.write(json.dumps(user))
#             # fo.write(pickle.dumps(user))
#         f = open('users.txt','wb')
#         pickle.dump(user, f)
#         f.close
    
#     return render_template('home.html', user=user)
#     # return redirect(url_for('home', user=user))
#     # return render_template('no_page_found.html')

#     # return redirect(url_for("created_user", user=user))


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
db.create_all()


result = connection.execute(ins)
        flash("Submitted")

ins = users.insert().values(
            username=request.form["uname"],
            email=request.form["email"],
            phone=request.form["pnumber"],
            password=request.form["password"],
        )



# HOME PAGE
# @app.route("/home/<input_username>/<input_password>/<query_username>/<query_password>")
# def home(input_username,input_password,query_username,query_password):
#     return render_template("home.html", input_username=input_username, input_password=input_password, query_username=query_username, query_password=query_password)
# LOGIN PAGE
    #     Session = sessionmaker(bind=engine)
    #     s = Session()
    #     query = s.query(Users).filter(Users.username==input_username, Users.password==input_password)
    #     result = query.first()
    #     if result:
    #         return redirect(url_for('home'))
    #     else:
    #         flash('wrong password')
    # return render_template("login.html")