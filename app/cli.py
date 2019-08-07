import os
import click
from app import app
from flask.cli import with_appcontext


def register(app):
    @app.cli.group()
    def translate():
        """Translation and localization commands."""
        pass

    @translate.command()
    @click.argument('lang')
    def init(lang):
        """Initialize a new language."""
        pass

    @translate.command()
    def update():
        """Update all languages."""
        pass

    @translate.command()
    def compile():
        """Compile all languages."""
        pass

@click.command("add_user")
@with_appcontext
def add_roles():
    from app import db, security
    from app.auth.models import Role
    db.init_app(app)
    # Setup Flask-Security
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)
    user_datastore.create_user(email='john@johnlopez.org', password=app.config['ADMIN_PASSWORD'])
    db.session.commit()
