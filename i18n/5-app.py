#!/usr/bin/env python3
"""
Mock login system with Flask-Babel for Task 5.

- Users table
- login_as URL parameter
- before_request sets g.user
- Localized messages
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

# Users table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__, template_folder="templates")
app.config.from_object(Config)


def get_locale():
    """
    Determine the locale from URL parameter or Accept-Language.
    """
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel = Babel(app, locale_selector=get_locale)
app.jinja_env.globals['get_locale'] = get_locale  # Template access


def get_user():
    """
    Retrieve user dict based on login_as parameter.

    Returns:
        dict or None
    """
    try:
        user_id = int(request.args.get("login_as"))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """Set g.user for the request"""
    g.user = get_user()


@app.route("/", strict_slashes=False)
def home():
    """Render home page with localized messages"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)