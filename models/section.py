from database import db

class section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text(), nullable=False)
    image_file_id = db.Column(db.Integer, db.ForeignKey('image.id'))
    content_file_id = db.Column(db.Integer, db.ForeignKey('file.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

    """
        Utilizada para preencher os tabel_headers da classe table. E chamada por tipo de model.
    """
    def getAttributes():
        return ["id","title","image_file_id","content_file_id","project_id"]