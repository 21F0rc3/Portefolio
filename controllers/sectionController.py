from controllers.controllerImports import *

"""
    Cria uma nova secção na base de dados
"""
def createSection(request):
    newSection = section(title=request.form['title'],
                         image_file_id=request.form['image_file_id'],
                         content_file_id=request.form['content_file_id'],
                         project_id=request.form['project_id'])
    
    db.session.add(newSection)
    db.session.commit()

    return redirect(url_for('admin'))

"""
    Le uma secção da base de dados
"""
def readSection(section):
    if(section.image_file_id != -1):
        image_file = readImage(section.image_file_id)
    else:
        image_file = None
    
    if(section.content_file_id != -1):
        content_file = readFile(section.content_file_id)
    else:
        content_file = ""

    return ReadableSectionObject(section.id,section.title,image_file,content_file)
    

"""
    Atualiza os dados de uma secção na base de dados
"""
def updateSection(request):
    updateSection = section.query.filter_by(id=request.form['id']).first()

    updateSection.title = request.form['title']
    updateSection.image_file_id = request.form['image_file_id']
    updateSection.content_file_id = request.form['content_file_id']
    updateSection.project_id = request.form['project_id']

    db.session.commit()

    return redirect(url_for('admin'))


"""
    Elimina uma secção na base de dados
"""
def deleteSection(section_id):
    deleteSection = section.query.filter_by(id=section_id).first()

    db.session.delete(deleteSection)
    db.session.commit() 

    return redirect(url_for('admin'))

"""
    Retorna todas as secoes que pertencem ao projeto indicado.
    Utilizado para formatar todas as secções numa formato legivel[readSection()]
"""
def getProjectSections(project_id):
    sections = []
    
    sectionQuery = section.query.filter_by(project_id=project_id).all()

    for row in sectionQuery:
        sections.append(readSection(row))
    
    return sections

class ReadableSectionObject:
    def __init__(self,id,title,image_file,content_file):
        self.id=id
        self.title=title
        self.image_file=image_file
        self.content_file=content_file