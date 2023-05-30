from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from . import db
from .bank import generate_bank_id
import datetime

# Defines the enrollments table for the many-to-many relationship between users and courses
enrollments = db.Table('enrollments',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey('courses.id'), primary_key=True)
)

# Defines the courses table
class Course(db.Model):
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

# Rest of the code remains the same

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, nullable=False)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    iq = db.Column(db.Integer)
    eq = db.Column(db.Integer)
    skills_avg = db.Column(db.Integer)
    games_avg = db.Column(db.Integer)
    honors = db.Column(db.Enum('prodige', 'penseur créatif', 'quasi-génie', name='honors_enum'))
    account_number = db.Column(db.String(20), unique=True, nullable=False, default=generate_bank_id)

    bank_account = db.relationship('BankAccount', backref='user', uselist=False)
    courses = db.relationship('Course', secondary='enrollments', backref='users')


class BankAccount(db.Model):
    __tablename__ = 'bank_accounts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    balance = db.Column(db.Float, default=0.0)
    transactions = db.relationship('Transaction', backref='bank_account')

class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now().time())
    bank_account_id = db.Column(db.Integer, db.ForeignKey('bank_accounts.id'), nullable=False)

# Rest of the code remains the same


# Defines the items table for the shop
class Items(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text(), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    price = db.Column(db.Float, nullable=False)
    left = db.Column(db.Integer, nullable=False)
    pictures = db.Column(db.String(255), nullable=False)

# Defines the songs table
class Songs(db.Model):
    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), index=True, nullable=False)
    singer = db.Column(db.String(62), index=True, nullable=False)
    description = db.Column(db.Text(), nullable=False)
    song = db.Column(db.Text(), nullable=False)
    biography = db.Column(db.Text(), nullable=False)
    picture = db.Column(db.String(255), nullable=False)
    community = db.Column(db.BigInteger, index=True, nullable=False)

# Defines the books table
class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text(), nullable=False)
    author = db.Column(db.String(68), index=True, nullable=False)
    description = db.Column(db.Text(), nullable=False)
    biography = db.Column(db.Text(), nullable=False)
    picture = db.Column(db.String(255), nullable=False)

# Defines the applications table for instructors and prospective employees
class Applications(db.Model):
    __tablename__ = 'applications'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True, nullable=False)
    last_name = db.Column(db.String(64), index=True, nullable=False)
    email = db.Column(db.String(64), index=True, nullable=False)
    github = db.Column(db.Text())
    essay_one = db.Column(db.Text(), nullable=False)
    essay_two = db.Column(db.Text(), nullable=False)
    essay_three = db.Column(db.Text(), nullable=False)
    resume = db.Column(db.String(255), nullable=False)

