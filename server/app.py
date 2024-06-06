#!/usr/bin/env python3
import os
from flask import Flask, request, render_template
#jsonify, session... maybe in the future
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from models import db # import your models here!

app = Flask(
      __name__,
    static_url_path='',
    static_folder='../client/dist',
    template_folder='../client/dist'
)
app.secret_key=os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('POSGRES_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)

migrate = Migrate(app, db)

db.init_app(app)

@app.errorhandler(404)
def not_found(e):
    return render_template("index.html")


# write your routes here! 
# all routes should start with '/api' to account for the proxy


if __name__ == '__main__':
    app.run(port=5555, debug=True)
