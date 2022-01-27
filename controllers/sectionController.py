from controllers.controllerImports import *

"""
    Cria uma nova secção na base de dados
"""
def createSection(request):
    newSection = section(title=request.form['title'],
                         image_file=request.form['image_file'],
                         content_file=request.form['content_file'],
                         project_id=request.form['project_id'])
    
    db.session.add(newSection)
    db.session.commit()

    return redirect(url_for('admin'))

"""
    Le uma secção da base de dados
"""
def readSection():
    return

"""
    Atualiza os dados de uma secção na base de dados
"""
def updateSection(request):
    updateSection = section.query.filter_by(id=request.form['section_id']).first()

    updateSection.title = request.form['title']
    updateSection.image_file = request.form['image_file']
    updateSection.content_file = request.form['content_file']
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

