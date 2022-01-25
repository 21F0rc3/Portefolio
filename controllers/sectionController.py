from controllers.controllerImports import *

def createSection(request):
    newSection = section(title=request.form['title'],
                         image_url=request.form['image_url'],
                         content_file=request.form['content_file'],
                         project_id=request.form['request_form'])
    
    db.session.add(newSection)
    db.session.commit()

    return redirect(url_for('admin'))

def readSection():
    return

def updateSection(section_id):
    return

def deleteSection(section_id):
    deleteSection = section.query.filter_by(id=section_id).first()

    db.session.delete(deleteSection)
    db.session.commit() 

    return redirect(url_for('admin'))

