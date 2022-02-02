from controllers.controllerImports import *

"""
    Retorna a pagina do projeto com seu conteudo populado dinamicamente
"""
def getProjectContent(project_name):
    this_project = project.query.filter_by(name=project_name).first()

    project_sections = getProjectSections(this_project.id)

    return render_template("/layouts/project.html", project=readProject(this_project), sections=project_sections)


"""
    Cria um projeto na base de dados
"""
def createProject(request):
    newProject = project(name=request.form['name'],
                         logo_file_id=request.form['logo_file_id'],
                         description=request.form['description'],
                         keywords=request.form['keywords'])
    
    db.session.add(newProject)
    db.session.commit()

    return redirect(url_for('admin'))

"""
    Formata um projeto num objeto que pode ser lido.
    Por exemplo, subsitui os id's de imagens pelos seus ficheiros, para que possam ser apresentados
"""
def readProject(project):
    if(project.logo_file_id != -1):
        logo_file = readImage(project.logo_file_id)
    else:
        logo_file = null
    
    return ReadableProjectObject(project.name,project.description,project.keywords,logo_file)

"""
    Atualiza os dados de um projeto na base de dados
"""
def updateProject(request):
    updateProject = project.query.filter_by(id=request.form['id']).first()

    updateProject.name = request.form['name']
    updateProject.logo_file_id = request.form['logo_file_id']
    updateProject.description = request.form['description']
    updateProject.keywords = request.form['keywords']

    db.session.commit()

    return redirect(url_for('admin'))

"""
    Elimina um projeto na base de dados
"""
def deleteProject(project_id):
    deleteProject = project.query.filter_by(id=project_id).first()

    db.session.delete(deleteProject)
    db.session.commit() 

    return redirect(url_for('admin'))

"""
    Lê todos os projetos da base de dados no formato em que podem ser lidos[readProject()]
    E utilizado pelo index para apresentar todos os projetos
"""
def readProjects():
    projects = []

    projectQuery = project.query.all()

    for row in projectQuery:
        projects.append(readProject(row))

    return projects

class ReadableProjectObject:
    def __init__(self,name,description,keywords,logo_file):
        self.name=name
        self.description=description
        self.keywords=keywords
        self.logo_file=logo_file

