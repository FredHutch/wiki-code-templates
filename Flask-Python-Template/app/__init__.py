from flask import Flask
# import logging
from app import config as server_config


def get_app():
    tmp = Flask(__name__)
    tmp.config.from_object(server_config)
    return tmp


server = get_app()


from app import routes  # NOQA
