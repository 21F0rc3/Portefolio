from controllers.controllerImports import *

"""
    Redireciona para a pagina de admin onde podemos manipular a base de dados
"""
def crudPage():
    projects = project.query.all()
    sections = section.query.all()
    
    return render_template("crud.html", projects=projects, sections=sections)