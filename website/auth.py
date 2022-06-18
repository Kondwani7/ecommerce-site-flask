from flask import Blueprint, render_template,request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
auth = Blueprint('auth', __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

    return render_template("login.html")

@auth.route("/logout")
def logout():
    return "<p>logout</p>"

@auth.route("/signup", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(name) < 2:
            flash("Name must be greater than 1 character", category='error')
        elif password1 != password2:
            flash("password must match to be confirmed", category="error")
        elif (len(password1) < 7):
            flash("password must be atleast 7 characters", category='error')
        
        else:
            flash("Account created", category="success")
    return render_template("sign_up.html")