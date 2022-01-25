from controllers.controllerImports import *

"""
    Retorna a pagina do projeto com seu conteudo populado dinamicamente
"""
def getProjectContent(project_name):
    project_id = project.query.filter_by(name=project_name).first().id

    project_sections_url = section.query.filter_by(project_id=project_id).all() 

    # Substitui todos os ficheiros da tabela da secção pelo o seu respetivo conteudo
    project_sections = replaceFilesURLForContent(project_sections_url)

    return render_template("/layouts/project.html", title=project_name, sections=project_sections)


def createProject(request):
    newProject = project(name=request.form['name'],
                         logo_file=request.form['logo_file'],
                         description=request.form['description'],
                         keywords=request.form['keywords'])
    
    db.session.add(newProject)
    db.session.commit()

    return redirect(url_for('admin'))

def readProject(project_name):
    return getProjectContent(project_name)

def updateProject(request):
    updateProject = project.query.filter_by(id=request.form['project_id']).first()

    updateProject.name = request.form['name']
    updateProject.logo_file = request.form['logo_file']
    updateProject.description = request.form['description']
    updateProject.keywords = request.form['keywords']

    db.session.commit()

    return redirect(url_for('admin'))

def deleteProject(project_id):
    deleteProject = project.query.filter_by(id=project_id).first()

    db.session.delete(deleteProject)
    db.session.commit() 

    return redirect(url_for('admin'))

