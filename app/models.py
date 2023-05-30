from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from . import db
from .bank import generate_bank_id
import datetime

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    first_name = db.Column(db.String(64), index=True, nullable=False)
    last_name = db.Column(db.String(64), index=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    iq = db.Column(db.Integer, index=True)
    eq = db.Column(db.Integer, index=True)
    skills_avg = db.Column(db.Integer, index=True)
    games_avg = db.Column(db.Integer, index=True)
    honors = db.Column(db.Enum('prodige', 'penseur créatif', 'quasi-génie'))
    account_number = db.Column(db.String(20), unique=True, nullable=False, default=generate_bank_id)

