from flask import render_template
from . import main

@main.route('/')
def index():
    """
    View root page function that returns the index page
    """
    return render_template('index.html')