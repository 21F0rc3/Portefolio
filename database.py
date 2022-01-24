from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

# Import DB Tables
import migrations.project
import migrations.section

# Create Tables
#db.create_all()

# Import seeder
import seeder