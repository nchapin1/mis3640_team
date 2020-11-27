from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404

@app.route("/login/", methods=["GET", "POST"])
def login_page():
    # CHECK THE CSV FILE FOR KEYS
    # return redirect(url_for('login_page'))
    return render_template("login.html")

@app.route("/signup/", methods=["GET", "POST"])
def signup_page():
    # ADD TO THE CSV
    if request.method == "POST":
        username = request.form['uname']
        email = request.form['email']
        phone = request.form['pnumber']
        password = request.form['password']
    return redirect(url_for('create_user', username = username, email = email, phone = phone, password = password))


@app.route('/home/')
def home():
    return render_template('home.html')



# @app.route("/nearest/", methods=["GET", "POST"])
# def search():
#     if request.method == "POST":
#         location = request.form["location"]
#         rad = request.form["rad"]
#     return redirect(url_for("result", location=location, rad=rad))


# @app.route("/nearest_mbta/<location>/<rad>")
# def result(location, rad):
#     map_url = userlocation(location)
#     response_data = fetchmap(map_url)
#     # if len(response_data['data']) == 1:
#     #     # flash(u'There are no MBTA stops within {rad} miles of your location.', 'error')
#     #     return redirect(url_for('/'))
#     latlng = fetchlatlng(response_data)
#     stop_name, stop_accessible = fetchmbta(latlng, rad)
#     return render_template(
#         "mbta_station.html", stop_name=stop_name, stop_accessible=stop_accessible
#     )



