from enum import unique
from database import db

class image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_file = db.Column(db.Text(), nullable=False, unique=True)

    """
        Utilizada para preencher os tabel_headers da classe table. E chamada por tipo de model.
    """
    def getAttributes():
        return ["id","image_file"]