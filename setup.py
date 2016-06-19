"""Flask skeleton/example application"""
from setuptools import setup

setup(
    name='flask_skeleton',
    version='0.1',
    description=__doc__,
    author='Toby Fleming',
    author_email='tobywf@users.noreply.github.com',
    packages=['flask_skeleton', 'flask_skeleton.scripts'],
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
        'Flask-Login',
        'Flask-WTF',
        'WTForms-Alchemy',
        'passlib'
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'run = flask_skeleton.scripts:run',
            'reset_db = flask_skeleton.scripts:reset_db',
        ]
    },
    package_data={
        'static': 'flask_skeleton/static/*',
        'templates': 'flask_skeleton/templates/*'
    },
)
