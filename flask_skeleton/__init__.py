import flask
import werkzeug.local

# pylint: disable=invalid-name
logger = werkzeug.local.LocalProxy(lambda: flask.current_app.logger)


def create_app(settings):
    app = flask.Flask(__name__)
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True
    app.config.from_object('flask_skeleton.config')
    app.config.update(settings)

    import flask_skeleton.models
    flask_skeleton.models.db.init_app(app)
    flask_skeleton.models.lm.login_view = "views.login"
    flask_skeleton.models.lm.init_app(app)

    import flask_skeleton.views
    app.register_blueprint(flask_skeleton.views.views)

    return app
