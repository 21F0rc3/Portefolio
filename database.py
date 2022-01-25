from app import app
from flask_security.models import fsqla_v2 as fsqla
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, auth_required, hash_password

db = SQLAlchemy(app)

# Define models
fsqla.FsModels.set_db_info(db)

# Import DB Tables
import models.project
import models.section
from models.user import User
from models.role import Role

# Create Tables
db.create_all()

# Import seeder
import seeder

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)