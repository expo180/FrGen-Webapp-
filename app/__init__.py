import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import json

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
     # Get the SSL certificate information from the environment variable
    ssl_cert = os.getenv("SSL_CERT")
     # Parse the SSL certificate information as a dictionary
    ssl_cert_dict = json.loads(ssl_cert)

     # Configure the database URI with the SSL certificate information
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{username}:{password}@{host}/{database}?ssl={{"ca": "{ssl_cert}"}}'.format(
    host=os.environ.get('HOST'),
    username=os.environ.get('USERNAME'),
    password=os.environ.get('PASSWORD'),
    database=os.environ.get('DATABASE'),
    ssl_cert=ssl_cert_dict
    )

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'Frame_genesis_entreprises74418917$*!'

    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.connexion'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
