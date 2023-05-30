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

    bank_account = db.relationship('BankAccount', backref='user', uselist=False)
    courses = db.relationship('Courses', secondary='enrollments', backref='users')

class BankAccount(db.Model):
    __tablename__ = 'bank_accounts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    balance = db.Column(db.Float, default=0.0)
    transactions = db.relationship('Transaction', backref='bank_account')

class Courses(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text(), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    main_course = db.Column(db.Text(), nullable=False)
    quizz = db.Column(db.Text(), nullable=False)
    exercises = db.Column(db.Text(), nullable=False)
    projects = db.Column(db.Text(), nullable=False)
    price = db.Column(db.Float(15, 9), index=True, default=2.0)
    author = db.Column(db.String(255), nullable=False)
    specialization = db.Column(db.String(255), nullable=False)
    company = db.Column(db.String(155))
    intros = db.Column(db.String(255))
    videos = db.Column(db.String(255))
    pictures = db.Column(db.String(255))
    ENG = db.Column(db.String(255))
    FR = db.Column(db.String(255))
