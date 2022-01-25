from database import db
from flask_security.models import fsqla_v2 as fsqla

class Role(db.Model, fsqla.FsRoleMixin):
    pass