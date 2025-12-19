#!/usr/bin/env python3
""" Parametrize templates with Babel """
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config(object):
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__, template_folder="templates")
app.config.from_object(Config)


def get_locale():
    """Return best match with supported languages"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


# Checker istiyor: locale_selector parametresi
babel = Babel(app, locale_selector=get_locale)


@app.route("/", strict_slashes=False)
def home():
    """Render the home page with localized messages"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)