from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from ..models import User,Pitch
from .forms import PitchForm,UpdateProfile
from .. import db,photos
import markdown2

@main.route('/')
def index():
    """
    View root page function that returns the index page
    """
    return render_template('index.html')
    

@main.route('/user/<uname>')
def profile(uname):
    """
    Function to render the profile page
    """
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    """
    View function to handle update profile request

    Args:
        Uname:The users username
    """
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname = user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    """
    Function to allow update of profile photo
    """
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/pitch/<int:id>')
def single_pitch(id):
    pitch = Pitch.query.get(id)
    if pitch is None:
        abort(404)

    format_review = markdown2.markdown(review.movie_review,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('review.html',review = review,format_review=format_review)

@main.route('/')
def pitch(id):
    """
    Function to find pitch
    """
    pitches = Pitch.query.filter_by(id)

    return render_template('index.html', pitches = pitches)



@main.route('/pitch/new',methods = ['GET','POST'])
def new_pitch():
    new = PitchForm()

    if new.validate_on_submit():

        brand = Pitch(pitch_title = new.title.data,pitch_subject = new.pitch.data)
        view = []
        view.append(brand)
        db.session.add(brand)
        db.session.commit()

        return redirect(url_for('.pitch'))

    title = 'New Pitch'
    return render_template('pitch.html',title = title,new = new)