#!/usr/bin/env python3
""" Infer appropriate time zone with Babel and user locale """
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz

# Mock users table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config(object):
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

# Helpers for templates
def get_user():
    """Return user dict or None if login_as invalid"""
    login_id = request.args.get("login_as", type=int)
    if login_id and login_id in users:
        return users[login_id]
    return None

def get_locale():
    """Determine the locale to use."""
    # URL parameter
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    # User setting
    if g.get("user") and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user["locale"]
    # Request header
    return request.accept_languages.best_match(app.config["LANGUAGES"])

def get_timezone():
    """Determine the timezone to use."""
    tzname = request.args.get("timezone")
    # URL parameter
    if tzname:
        try:
            pytz.timezone(tzname)
            return tzname
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    # User setting
    if g.get("user") and g.user.get("timezone"):
        try:
            pytz.timezone(g.user["timezone"])
            return g.user["timezone"]
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    # Default
    return app.config["BABEL_DEFAULT_TIMEZONE"]

# Initialize Babel
babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)

# Make helpers available in templates
app.jinja_env.globals['get_locale'] = get_locale
app.jinja_env.globals['babel'] = babel

@app.before_request
def before_request():
    """Executed before each request: sets g.user"""
    g.user = get_user()

@app.route("/", strict_slashes=False)
def home():
    """Render home page with localized messages"""
    return render_template("7-index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)