from migrations.project import project

def getProjectContent(project_name):
    pro = project.query.first()

    return pro.name