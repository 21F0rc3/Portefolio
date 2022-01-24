from email import charset
from turtle import title
from sqlalchemy import null
from migrations.project import project
from migrations.section import section
from flask import render_template


# Vai buscar o conteudo do projeto a base de dados com um nome especifico
def getProjectContent(project_name):
    project_id = project.query.filter_by(name=project_name).first().id

    # Vai buscar todas as sections do projeto
    project_sections = section.query.filter_by(project_id=project_id).all() 

    # Substitui todos os ficheiros da tabela da secção pelo o seu respetivo conteudo
    sections = replaceFilesURLForContent(project_sections)

    return render_template("/layouts/project.html", title=project_name, sections=sections)

# Vai buscar o conteudo de um ficheiro
def getFileContent(file_url):
    try:
        file = open('files/'+file_url, 'r', encoding='utf-8').read()
    
    except:
        print("Algo deu errado ao tentar acessar o ficheiro: "+file_url)
        file = null

    return file

# Substitui o content_file(url para ficheiro) pelo o seu conteudo
def replaceFilesURLForContent(project_sections):
    sections = []

    for project_section in project_sections:
        aux = section()

        aux.id = project_section.id
        aux.title = project_section.title
        aux.image_url = project_section.image_url
        
        aux.content_file = getFileContent(project_section.content_file)

        sections.append(aux)

    return sections