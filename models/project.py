from database import db

class project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(), nullable=False)
    logo_file = db.Column(db.Text())
    description = db.Column(db.Text())
    keywords = db.Column(db.Text())

    """
        Utilizada para preencher os tabel_headers da classe table. E chamada por tipo de model.
    """
    def getAttributes():
        return ["id","name","logo_file","description","keywords"]