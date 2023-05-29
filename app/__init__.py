import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configure database credentials
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{username}:{password}@{host}/{database}'.format(
        host=os.environ.get('HOST'),
        username=os.environ.get('USERNAME'),
        password=os.environ.get('PASSWORD'),
        database=os.environ.get('DATABASE'),
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

    # SSL configuration
    app.config['SQLALCHEMY_DATABASE_URI'] += "?ssl_mode=VERIFY_IDENTITY&ssl={ca}".format(
        ca=os.environ.get("SSL_CERT")
    )

    return app
