from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

import migrations.project
import migrations.section

db.create_all()

import seeder