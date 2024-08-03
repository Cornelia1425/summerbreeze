from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

# write your models here! my models - users (role - audience, and performer)piece are for performers only, events are for both performers and audience


class User (db.Model, SerializerMixin):
    __tablename__="users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    role = db.Column(db.String, default='audience')
    profile_img = db.Column(db.String, nullable=False)

    _hashed_password = db.Column(db.String, nullable=False)

    piece_enrolls = db.relationship('Piece_enroll', back_populates='user') #performer-only

    serialize_rules = ('-piece_enrolls.user',)

    


# write your models here! my models - piece_enroll
class Piece_enroll (db.Model, SerializerMixin):
    __tablename__="piece_enrolls"
    id = db.Column(db.String, primary_key=True)

    piece_id = db.Column(db.Integer, db.ForeignKey('pieces.id'))
    piece = db.relationship('Piece', back_populates='piece_enrolls')

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='piece_enrolls')

    serialize_rules = ('-piece.piece_enrolls', '-user.piece_enrolls',)


# write your models here! my models - piece

class Piece (db.Model, SerializerMixin):
    __tablename__ = "pieces"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    image = db.Column(db.String)
    video = db.Column(db.String)

    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    event= db.relationship('Event', back_populates='pieces')

    piece_enrolls = db.relationship('Piece_enroll', back_populates = 'piece')

    serialize_rules = ('-event.pieces', '-piece_enrolls.piece',)


# write your models here! my models - event
class Event (db.Model, SerializerMixin):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String)
    time = db.Column(db.String)

    pieces = db.relationship('Piece', back_populates='event')

    serialize_rules = ('-pieces.event',)

