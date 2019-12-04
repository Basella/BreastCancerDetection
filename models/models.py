from frontend.__init__ import db
from datetime import datetime


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    date_created = db.Column(db.Integer, default=datetime.utcnow)

    def __repr__(self):
        return '<Entry {}>'.format(self.username)
