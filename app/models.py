#This Python module contain  model definitions in other words MySQL tables
#coded Friday May 26th 2023
#Bader Salissou Saadou
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from . import db

#defines the user tables for registration, authentication etc..
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key =True)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    first_name = db.Column(db.String(64), unique=True, index=True, nullable=False)
    last_name = db.Column(db.String(64), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(128), index=True, nullable=False)
    iq = db.Column(db.Integer, index=True)
    eq = db.Column(db.Integer, index=True)
    skills_avg = db.Column(db.Integer, index=True)
    games_avg = db.Column(db.Integer, index=True)
    honors = db.Column(db.Enum('prodige', 'penseur créatif', 'quasi-génie'))
    bank_id = db.Column(db.Integer, db.ForeignKey('bank.id')) 
    courses_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

class Bank(UserMixin, db.Model):
    __tablename__ = 'bank'
    id = db.Column(db.Integer, primary_key=True)
    loans = db.Column(db.Float, index=True, default=0)
    net_worth = db.Column(db.Float(15,9), index=True, default=0)
    money = db.relationship('User', backref='bank_net')
    capital_raised = db.Column(db.Float(15,9), index=True, default=0.00)

#courses definition
class Courses(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text(), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    main_course = db.Column(db.Text(), nullable=False)
    quizz = db.Column(db.Text(),  nullable=False)
    exercises = db.Column(db.Text(),  nullable=False)
    projects = db.Column(db.Text(), nullable=False)
    price = db.Column(db.Float(15,9), index=True, default=2.00)
    author = db.Column(db.String(255), nullable=False)
    specialization = db.Column(db.String(255), nullable=False)
    company = db.Column(db.String(155))
    courses_key = db.relationship('User', backref='purchased_courses')
    intros = db.Column(db.Text())
    videos = db.Column(db.Text())
    pictures = db.Column(db.Text())
    ENG = db.Column(db.Text())
    FR = db.Column(db.Text())


#shop model definition
class Items(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text(), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    price = db.Column(db.Float, nullable=False)
    left = db.Column(db.Integer, nullable=False)
    pictures = db.Column(db.Text(), nullable=False)

#songs model definition
class Songs(db.Model):
    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), index=True, nullable=False)
    singer = db.Column(db.String(62), index=True, nullable=False)
    description = db.Column(db.Text(),  nullable=False)
    song = db.Column(db.Text(), nullable=False)
    biography = db.Column(db.Text(), nullable=False)
    picture = db.Column(db.Text(), nullable=False)
    community = db.Column(db.BigInteger, index=True, nullable=False)

#books model definition
class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text(), nullable=False)
    author = db.Column(db.String(68), index=True, nullable=False)
    description = db.Column(db.Text(), nullable=False)
    biography = db.Column(db.Text(), nullable=False)
    picture = db.Column(db.Text(), nullable=False)

#instructors and  all prospective employees applications
class Applications(db.Model):
    __tablename__ = 'applications'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True, nullable=False)
    last_name = db.Column(db.String(64), index=True, nullable=False)
    email = db.Column(db.String(64), index=True, nullable=False)
    github = db.Column(db.Text())
    essay_one = db.Column(db.Text(), nullable=False)
    essay_two = db.Column(db.Text(),  nullable=False)
    essay_three = db.Column(db.Text(),  nullable=False)
    resume = db.Column(db.Text(), nullable=False)

