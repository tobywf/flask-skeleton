import flask_skeleton
from flask_skeleton.models import db, User


# pylint: disable=invalid-name
app = flask_skeleton.create_app({
    'SECRET_KEY': 'completely_unsafe_dev_key',
    'DEBUG': True,
    'TESTING': True
})


def run():
    app.run(host='0.0.0.0', port=5000)


def reset_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
        if app.debug:
            user = User(email='admin@admin.com', password='password')
            db.session.add(user)
            db.session.commit()

    print('Database', app.config['SQLALCHEMY_DATABASE_URI'], 'created')
