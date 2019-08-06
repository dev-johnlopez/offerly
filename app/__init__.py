import logging
import os
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask import Flask, request, redirect
from config import Config
from werkzeug.contrib.fixers import ProxyFix
from flask_admin import Admin
from flask_mail import Mail
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from geopy.geocoders import Nominatim


app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
mail = Mail()
admin = Admin()
security = Security()
geolocator = Nominatim(user_agent='Offerly')


def create_app(config_class=Config):
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    cors.init_app(app)

    from app.auth.models import User, Role

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app=app,
                      datastore=user_datastore)

    from app.admin import create_admin
    admin = create_admin(app, db)

    from app.views.landing import bp as landing_bp
    from app.views.evaluation import bp as evaluation_bp
    app.register_blueprint(landing_bp)
    app.register_blueprint(evaluation_bp, url_prefix="/e")

    from app.models.address import Address
    from app.models.property import Property

    if not app.debug and not app.testing:
        if app.config['LOG_TO_STDOUT']:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            app.logger.addHandler(stream_handler)
        else:
            if not os.path.exists('logs'):
                os.mkdir('logs')
            file_handler = RotatingFileHandler('logs/assignably.log',
                                               maxBytes=10240, backupCount=10)
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s '
                '[in %(pathname)s:%(lineno)d]'))
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Assignably startup')

    return app
