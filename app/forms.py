from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class RegistrationForm(FlaskForm):
    first_name = StringField('Prénom:', validators=[DataRequired(), Length(1, 64)])
    last_name = StringField('Nom:', validators=[DataRequired(), Length(1, 64)])
    email = StringField('Adresse-email:', validators=[DataRequired(), Length(1, 64), Email()])
    password_confirm = PasswordField('Confirmer Mot de Passe', validators=[DataRequired(), EqualTo('password', message='Les mots de passe doivent correspondre')])
    password = PasswordField('Mot de Passe', validators=[DataRequired(), Length(1, 128)])
    submit = SubmitField('connexion')
    register = SubmitField('Créer un nouveau compte', id="submit")

class LoginForm(FlaskForm):
   email = StringField('Adresse-email:', validators=[DataRequired(), Length(1, 64), Email()])
   password = PasswordField('Mot de passe:', validators=[DataRequired(), Length(1, 128)])
   remember_me = BooleanField('Se souvenir de moi')
   submit = SubmitField('Se connecter')

class EmailForm(FlaskForm):
    email = StringField('Entrez votre adresse-email:', validators=[DataRequired(), Length(1, 64), Email()])
    submit = SubmitField('Suivant')

class PasswordResetForm(FlaskForm):
    new_password = PasswordField('Nouveau Mot de Passe', validators=[DataRequired(), Length(1, 128)])
    new_password_confirm = PasswordField('Confirmer Mot de Passe', validators=[DataRequired(), Length(1, 128)])
    reset = SubmitField('Continuer')




