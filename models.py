from app import db


class Count(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    geo = db.Column(db.String(255))
    agent = db.Column(db.String(255))
