from flask import render_template
from . import auth

@auth.route('/login')
def login():
    """
    View function that renders the login page
    """
    return render_template('auth/login.html')