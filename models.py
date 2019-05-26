#
# Main APP models
#

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from main import app


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    """User DB model"""
    __tablename__ = 'user'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    posts = db.relationship(
        'Post',
        backref='user',
        lazy='dynamic',
    )
    comments = db.relationship(
        'Comment',
        backref='comment',
        lazy='dynamic',
    )

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return "<user: '{username}'>".format(username=self.username)


class Post(db.Model):
    """Each post has a user"""
    __tablename__ = 'post'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text(), nullable=True)
    publish_date = db.Column(db.DateTime(), default=datetime.now)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    comments = db.relationship(
        'Comment',
        backref='post',
        lazy='dynamic'
    )

    def __repr__(self):
        return "<Post: '{title}'>".format(title=self.title)


class Comment(db.Model):
    """Each post has comments"""
    __tablename__ = 'comment'

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text(), nullable=True)
    date = db.Column(db.DateTime(), default=datetime.now)
    post_id = db.Column(db.Integer(), db.ForeignKey('post.id'))

    def __repr__(self):
        return "<Comment: '{title}'".format(title=self.title)
