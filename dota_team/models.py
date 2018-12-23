from dota_team import db, login_manager
from flask_login import UserMixin

# for errors with pylint use pylint-flask
# source: https://github.com/PyCQA/pylint/issues/1973
# of just change linter to flake8 :\

# from documentation
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(35), unique=True, nullable=False)
    steam_login = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    profile_img = db.Column(db.String, nullable=False, default="default_profile_logo.jpg")
    mmr = db.Column(db.String(5), nullable=False)
    aim = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)
    # in the future - many-to-many relation - separate db
    server = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return f"User('{self.id}', '{self.login}', '{self.server}', '{self.profile_img}')"


# class Requests(db.Model):
#     pass
