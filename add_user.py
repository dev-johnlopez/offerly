from app import db
from flask import current_app
from flask_security import Security, SQLAlchemyUserDatastore, current_user
from flask_security.utils import encrypt_password
from app.auth.models import Role, User
# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
user_datastore.create_user(email='john@johnlopez.org', password=encrypt_password(''))
db.session.commit()
