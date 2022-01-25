from database import db

class section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text(), nullable=False)
    image_file = db.Column(db.Text())
    content_file = db.Column(db.Text(), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)