from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    """
    Function that queries the database and gets a user with the id

    Args:
        UserId:The id of the specific user
    """
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    """
    User model class

    Args:
        DbModel:Connects our class to our database and allow communication
    """
    __tablename__ = 'users'
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship('Pitch',backref = 'user',lazy = "dynamic")

    @property
    def password(self):
        """
        Method to create a write only class property
        """
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        """
        Method to set the password
        """
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        """
        Method that takes in a password,hashes it and compares it to the hashed password for verification
        """
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        """
        Function that makes debugging easier
        """
        return f'User {self.username}'

class Role(db.Model):
    """
    Class that will define all different roles

    Args:
        DbModel:Connects our class to our database and allow communication
    """
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        """
        Function that makes debugging easier
        """
        return f'User {self.name}'

class Pitch(db.Model):
    """
    Class that handles pitch post requests

    Args:
        DbModel:Connects our class to our database and allow communication
    """
    __tablename__ = 'pitch'

    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer)
    pitch_title = db.Column(db.String)
    pitch_subject = db.Column(db.String)
    posted = db.Column(db.DateTime,default = datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_pitch(self):
        """
        Method to save the pitch
        """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,id):
        """
        Method to get the pitches
        """
        pitches = Pitch.query.filter_by(pitch_id=id).all()

        return pitches


    