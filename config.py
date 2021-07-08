import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost:5432/fyyur'
SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_ENGINE_OPTIONS = {
#   "pool_pre_ping": True,
#   "pool_recycle": 300,
#   'pool_timeout': 900,
#   'pool_size': 10,
#   'max_overflow': 5,
# }
# SQLALCHEMY_ECHO = True