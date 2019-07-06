from app import db
from sqlalchemy.dialects.postgresql import JSON
import os

class Terr(db.Model):
    __tablename__ = 'terr'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    owner = db.Column(db.String())
    position = db.Column(db.String())
    # result_all = db.Column(JSON)


    def __init__(self, name, owner, position):
        self.name = name
        self.owner = owner
        self.position = position

    def __repr__(self):
        return '<id {}>'.format(self.name)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'owner': self.owner,
            'position':self.position
        }