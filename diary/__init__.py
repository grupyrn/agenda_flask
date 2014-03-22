# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.pymongo import PyMongo

import config
from views import diary


def create_app(cfg):
    app = Flask(__name__)
    app.config.from_object(cfg)
    return app


# Application creation.
app = create_app(config)

# Database configuration.
db = PyMongo()

# Blueprints registration.
app.register_blueprint(diary)


if __name__ == '__main__':
    app.run()
