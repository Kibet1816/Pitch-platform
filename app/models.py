from . import db

class User(db.Model):
    """
    User model class

    Args:
        DbModel:Connects our class to our database and allow communication
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

class Role(db.Model):
    """
    Class that will define all different roles

    Args:
        DbModel:Connects our class to our database and allow communication
    """
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))

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