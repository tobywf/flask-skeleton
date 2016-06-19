import sys
import flask_skeleton

sys.path.insert(0, '/var/www/flask_skeleton/')

# load virtualenv, etc. not a fully functioning WSGI file!

application = flask_skeleton.create_app({
    'SECRET_KEY': 'completely_unsafe_production_key',
})
