from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    """
    Class for users to write their own pitches
    """

    title = StringField('Pitch title',validators=[Required()])
    pitch = TextAreaField('Write a new pitch')
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    """
    Class to update our profile
    """
    bio = TextAreaField('Tell us about you.',validators=[Required()])
    submit = SubmitField('Submit')