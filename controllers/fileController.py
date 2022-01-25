from controllers.controllerImports import *

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
        aux.image_file = project_section.image_file
        
        aux.content_file = readFile(project_section.content_file)

        sections.append(aux)

    return sections