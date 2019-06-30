from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

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
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))

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


    def __repr__(self):
        """
        Function that makes debugging easier
        """
        return f'User {self.username}'