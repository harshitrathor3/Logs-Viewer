# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo


db = SQLAlchemy()
mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    mongo.init_app(app)

    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app
