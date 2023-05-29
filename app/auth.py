from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from .forms import LoginForm, RegistrationForm, EmailForm, PasswordResetForm
from flask_login import login_user, login_required, logout_user

auth = Blueprint('auth', __name__)

@auth.route('/Se_connecter')
def connexion():
    form = LoginForm()
    return render_template('Se_connecter.html', form=form)

@auth.route('/Se_connecter', methods=['POST'])
def login_post():
    form = LoginForm()
    email = request.form.get('email')
    password_hash = request.form.get('password')
    remember = True if request.form.get('remember_me') else False

    user = User.query.filter_by(email=email).first()
    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password_hash, password_hash):
        flash('Mot de passe ou adresse e-mail incorrect, Veuillez réessayer...')
        return redirect(url_for('auth.connexion')) # if the user doesn't exist or password is wrong, reload the page
    login_user(user, remember=remember)
    return redirect(url_for('main.dashboard'))

@auth.route('/Créer_un_nouveau_compte')
def nouvel_utilisateur():
    form = RegistrationForm()
    return render_template('nouvel_utilisateur_un.html', form=form)

@auth.route('/déconnexion')
@login_required
def logout():
    logout_user()
    flash("Veuillez vous connecter afin d'accéder à la page")
    return redirect(url_for('auth.connexion'))

@auth.route('/Créer_un_nouveau_compte', methods=['POST'])
def nouvel_utilisateur_post():
    # code to validate and add user to database goes here
    form = RegistrationForm()
    email = request.form.get('email')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    password_hash = request.form.get('password_confirm')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database
    # Assuming you have the user object, you can access their bank account balance


    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Ce compte existe déja, Veuillez vous connecter directement')
        return redirect(url_for('auth.nouvel_utilisateur'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, first_name=first_name, last_name=last_name, password_hash=generate_password_hash(password_hash, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    flash('Votre compte a été créee avec succès, vous pouvez vous connecter maintenant!')
    return redirect(url_for('auth.connexion'))

@auth.route('/réinitialisation_mot_de_passe/')
def reset_password():
    form = EmailForm()
    return render_template('mot_de_passe_oublié.html', form=form)

@auth.route('/vérification_code_de_confirmation/')
def checkup():
    form = PasswordResetForm()
    return render_template('réinitialisation_mot_de_passe.html', form=form)
