from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

# Import DB Tables
import models.project
import models.section

# Create Tables
#db.create_all()

# Import seeder
import seeder