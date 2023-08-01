#!/usr/bin/env python3
"""
A Basic flask application
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict


class Config(object):
    """
    Application configuration class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Instantiate the application object
app = Flask(__name__)
app.config.from_object(Config)

# Wrap the application with Babel
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(id) -> Union[Dict[str, Union[str, None]], None]:
    """
    Validate user login details
    Args:
        id (str): user id
    Returns:
        (Dict): user dictionary if id is valid else None
    """
    return users.get(int(id), 0)


@babel.localeselector
def get_locale() -> str:
    """
    Get locale from request
    """
    locale = request.args.get('locale', '').strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    elif g.user and g.user.get('locale'):
        if g.user.get('locale') in Config.LANGUAGES:
            return g.user.get('locale')
    elif request.headers.get('locale'):
        if request.headers.get('locale') in Config.LANGUAGES:
            return request.headers.get('locale')
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request():
    """
    Adds valid user to the global session object `g`
    """
    setattr(g, 'user', get_user(request.args.get('login_as', 0)))


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders a basic html template
    """
    return render_template('6-index.html', user=g.user)


if __name__ == '__main__':
    app.run()
