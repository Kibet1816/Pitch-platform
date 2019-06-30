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

    def __repr__(self):
        """
        Function that makes debugging easier
        """
        return f'User {self.username}'