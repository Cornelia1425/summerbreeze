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
    


# write your models here! my models - piece

class Piece (db.Model, SerializerMixin):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    image = db.Column(db.String)
    video = db.Column(db.String)

    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    event= db.relationship('Event', back_populates='pieces')

    serialize_rules = ('-event.pieces',)
