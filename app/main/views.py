from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import User

@main.route('/')
def index():
    """
    View root page function that returns the index page
    """
    return render_template('index.html')

@main.route('/pitches/review/new/<int:id>',methods = ['GET','POST'])
@login_required
def new_review():
    pass

@main.route('/user/<uname>')
def profile(uname):
    """
    Function to render the profile page
    """
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
