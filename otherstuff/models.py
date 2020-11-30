"""Data models."""
from . import db


class User(db.Model):
    """Data model for user accounts."""

    __tablename__ = "flasksqlalchemy-tutorial-users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(80), index=False, unique=False, nullable=False)
    phone = db.Column(db.Integer, index=False, unique=False, nullable=False)
    password = db.Column(db.String(30), index=False, unique=False, nullable=False)

    def __repr__(self):
        return "<User {}>".format(self.username)