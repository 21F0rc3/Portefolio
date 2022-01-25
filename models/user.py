from database import db
from flask_security.models import fsqla_v2 as fsqla

class User(db.Model, fsqla.FsUserMixin):
    pass