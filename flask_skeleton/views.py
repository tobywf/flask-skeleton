import flask
import flask_login
from flask_skeleton.forms import UserForm
from flask_skeleton.models import db, User

views = flask.Blueprint(
    'views',
    __name__,
    template_folder='templates',
    static_folder='static')


@views.route('/login/', methods=['GET', 'POST'])
def login():
    form = UserForm(flask.request.form)
    if form.validate_on_submit():
        user = User.query.get(form.email.data)
        if user:
            if user.authenticate(form.password.data):
                db.session.add(user)
                db.session.commit()
                flask_login.login_user(user, remember=True)
                next_url = flask.request.args.get('next')
                # TODO: validate next_url
                return flask.redirect(next_url or flask.url_for('.index'))
            else:
                form.password.errors.append('Invalid password')
        else:
            form.email.errors.append('Unknown email address')
    return flask.render_template('login.html', form=form)


@views.route('/')
@flask_login.login_required
def index():
    return "Hello, world!"
