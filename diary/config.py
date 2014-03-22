import os

DEBUG = True
MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017')
