from controllers.controllerImports import *

def crudPage():
    projects = project.query.all()
    sections = section.query.all()
    
    return render_template("crud.html", projects=projects, sections=sections)