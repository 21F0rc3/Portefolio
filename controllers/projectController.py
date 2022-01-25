from sqlalchemy import null
from models.project import project
from models.section import section
from flask import render_template

"""
    Retorna a pagina do projeto com seu conteudo populado dinamicamente
"""
def getProjectContent(project_name):
    project_id = project.query.filter_by(name=project_name).first().id

    project_sections_url = section.query.filter_by(project_id=project_id).all() 

    # Substitui todos os ficheiros da tabela da secção pelo o seu respetivo conteudo
    project_sections = replaceFilesURLForContent(project_sections_url)

    return render_template("/layouts/project.html", title=project_name, sections=project_sections)



"""
    Le um ficheiro
"""
def readFile(file_url):
    try:
        file = open('files/'+file_url, 'r', encoding='utf-8').readlines()
    
    except:
        print("Algo deu errado ao tentar acessar o ficheiro: "+file_url)
        file = null

    return file



"""
    Substitui o content_file(url para ficheiro) pelo o seu conteudo
"""
def replaceFilesURLForContent(project_sections):
    sections = []

    for project_section in project_sections:
        aux = section()

        aux.id = project_section.id
        aux.title = project_section.title
        aux.image_url = project_section.image_url
        
        aux.content_file = readFile(project_section.content_file)

        sections.append(aux)

    return sections