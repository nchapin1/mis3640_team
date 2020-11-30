from flask import Flask, url_for, render_template, redirect
    
from forms import RegistrationForm

import os
SECRET_KEY = os.urandom(32)


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/', methods=('GET', 'POST'))
def contact():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('index.html',form=form)