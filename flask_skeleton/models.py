import flask_login
import flask_sqlalchemy
from sqlalchemy_utils import PasswordType

db = flask_sqlalchemy.SQLAlchemy()
lm = flask_login.LoginManager()


class User(db.Model):
    __tablename__ = 'users'

    email = db.Column(db.String, primary_key=True)
    password = db.Column(
        PasswordType(schemes=['pbkdf2_sha512']),
        nullable=False)
    authenticated = db.Column(db.Boolean, nullable=False, default=False)

    def is_active(self):
        return True

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

    def authenticate(self, password):
        # WARNING: this only secure because self.password is `PasswordType`
        compare = self.password == password
        if compare:
            self.authenticated = True
        return compare


@lm.user_loader
def load_user(user_id):
    return User.query.get(user_id)
