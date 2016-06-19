import flask_wtf
import wtforms_alchemy
from flask_skeleton.models import db, User


class DeleteForm(flask_wtf.Form):
    """Dummy form to allow CSRF on requests without other fields, e.g. delete."""
    pass

# plumbing to get flask integration between wtforms_alchemy and flask_wtf
# pylint: disable=invalid-name
BaseModelForm = wtforms_alchemy.model_form_factory(flask_wtf.Form)


class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session


class UserForm(ModelForm):
    class Meta:
        model = User
        only = ['email', 'password']
