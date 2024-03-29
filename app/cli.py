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
