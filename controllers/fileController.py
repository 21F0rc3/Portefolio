from controllers.controllerImports import *

"""
    Retorna o conteudo de um ficheiro
"""
def readFile(file_id):
    file_url = file.query.filter_by(id=file_id).first().filename

    try:
        f = open('static/files/'+file_url, 'r', encoding='utf-8').readlines()
    
    except:
        print("Algo deu errado ao tentar acessar o ficheiro: "+file_url)
        f = null

    return f

def createFile(request):
    f = request.files['file']
    f.save(os.path.join(app.config['FILES_FOLDER'], f.filename))
    
    newFile = file(filename=f.filename)

    db.session.add(newFile)
    db.session.commit()

    return redirect(url_for('admin'))


def updateFile(file_id):
    """
        @TODO

        Basicamente elimina um ficheiro e insere outro
    """

    return redirect(url_for('admin'))
    

def deleteFile(request):
    deleteFile = image.query.filter_by(id=file_id).first()

    try:
        os.remove(os.path.join(app.config['FILES_FOLDER'], deleteFile.filename))
    except:
        print("Não foi possivel eliminar o ficheiro. O ficheiro não existe. Contudo, foi corrigido na base de dados")

    db.session.delete(deleteFile)
    db.session.commit() 

    return redirect(url_for('admin'))