from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/Se_connecter')
def connexion():
    return render_template('Se_connecter.html')

@auth.route('/Se_connecter', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()
    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Mot de passe ou Adresse e-mail incorrecte, Veuillez réessayer...')
        return redirect(url_for('auth.connexion')) # if the user doesn't exist or password is wrong, reload the page

    return redirect(url_for('main.dashboard'))

@auth.route('/Créer_un_nouveau_compte')
def nouvel_utilisateur():
    return render_template('nouvel_utilisateur_un.html')

@auth.route('/déconnexion')
def logout():
    return 'logged Out'

@auth.route('/Créer_un_nouveau_compte', methods=['POST'])
def nouvel_utilisateur_post():
    # code to validate and add user to database goes here
    email = request.form.get('email')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    password = request.form.get('confirm_password')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Cette Adresse-email existe déja')
        return redirect(url_for('auth.nouvel_utilisateur'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('connexion'))
