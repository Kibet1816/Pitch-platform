from flask import render_template,redirect,url_for
from . import auth
from ..models import User
from .forms import RegistratonForm
from .. import db

@auth.route('/login')
def login():
    """
    View function that renders the login page
    """
    return render_template('auth/login.html')

@auth.route('/register',methods = ['GET','POST'])
def register():
    """
    Function to register new users
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.add(user)
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)

