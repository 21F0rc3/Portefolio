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
    f = open('static/files/'+request.form["Filename"], "w")

    f.write(request.form["Content"])

    f.close()

    return redirect(url_for('admin'))

def updateFile(request):
    return redirect(url_for('admin'))

def deleteFile(request):
    return redirect(url_for('admin'))