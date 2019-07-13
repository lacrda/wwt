from app import db
from sqlalchemy.dialects.postgresql import JSON
import os


class Terr(db.Model):
    __tablename__ = 'terr'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    owner = db.Column(db.String())
    position = db.Column(db.String())
    color = db.Column(db.String())
    # result_all = db.Column(JSON)


    def __init__(self, name, owner, position, color):
        self.name = name
        self.owner = owner
        self.position = position
        self.color = color

    def __repr__(self):
        return '<id {}>'.format(self.name)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'owner': self.owner,
            'position':self.position,
            'color': self.color
        }

class Owners(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String())
    color = db.Column(db.String())
    quant = db.Column(db.Integer())
    # result_all = db.Column(JSON)


    def __init__(self, owner, color, quant):
        self.owner = owner
        self.color = color
        self.quant = quant

    def __repr__(self):
        return '<id {}>'.format(self.owner)
    
    def serialize(self):
        return {
            'id': self.id, 
            'owner': self.owner,
            'color': self.color,
            'quant':self.quant
        }    