from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email
from wtforms import ValidationError
from models import User

class RegistrationForm(FlaskForm):
    first_name = StringField('Prénom:', validators=[DataRequired(), Length(1, 64)])
    last_name = StringField('Nom:', validators=[DataRequired(), Length(1, 64)])
    email = StringField('Adresse-email:', validators=[DataRequired(), Length(1, 64), Email()])
    password_confirm = PasswordField('Mot de passe', validators=[DataRequired(), EqualTo('password', message='Les mots de passe doivent correspondre')])
    password = PasswordField('Confirmer Mot de Passe', validators=[DataRequired(), Length(1, 128)])
    submit = SubmitField('connexion')
    register = SubmitField('Créer un nouveau compte', id="submit")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Cette adresse e-mail existe déja!')
        
    def validate_username(self, field):
        if User.query.filter_by(first_name=field.data).first():
            raise ValidationError('Ce nom existe déja !')

class LoginForm(FlaskForm):
   email = StringField('Adresse-email:', validators=[DataRequired(), Length(1, 64), Email()])
   password = PasswordField('Mot de passe:', validators=[DataRequired(), Length(1, 128)])
   remember_me = BooleanField('Se souvenir de moi')
   submit = SubmitField('Se connecter')
