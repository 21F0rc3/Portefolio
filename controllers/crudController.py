from controllers.controllerImports import *

"""
    Redireciona para a pagina de admin onde podemos manipular a base de dados
"""
def crudPage():
    tables = []

    tables.append(Table(project))
    tables.append(Table(section))

    """
    @todo Fazer o array de tabelas ser preenchidos por todos os models da db

    for model in db.metadata.tables.items():
         tables.append(Table(model))
    """

    return render_template("crud.html", tables=tables)

class Table:
    def __init__(self, model):
        self.table_headers = model.getAttributes()
        self.table_content = formatQueryRows(model, model.query.all())

def formatQueryRows(model, queryResults):
    if model == project:
        return formatQueryRowsIntoProject(queryResults)
    if model == section:
        return formatQueryRowsIntoSection(queryResults)
    else:
        print ("ERRO: Não foi reconhecido o model em formatQueryRows()")
        return url_for('index')

def formatQueryRowsIntoProject(queryResults):
    results = []

    for row in queryResults:
        rowColumns = [row.id,row.name,row.logo_file,row.description,row.keywords]
        results.append(rowColumns)

    return results

def formatQueryRowsIntoSection(queryResults):
    results = []

    for row in queryResults:
        rowColumns = [row.id,row.title,row.image_file,row.content_file,row.project_id]
        results.append(rowColumns)

    return results


def deleteTableRecord(table, id):
    if table == 'project':
        return deleteProject(id)
    if table == 'section':
        return deleteSection(id)
    else:
        print ("ERROR: Não foi renconhecida a tabela em deleteFromTable()")
        return url_for('index')

def createTableRecord(table, request):
    if table == 'project':
        return createProject(request)
    if table == 'section':
        return createSection(request)
    else:
        print ("ERROR: Não foi renconhecida a tabela em insertIntoTable()")
        return url_for('index')

def updateTableRecord(table, request):
    if table == 'project':
        return updateProject(request)
    if table == 'section':
        return updateSection(request)
    else:
        print ("ERROR: Não foi renconhecida a tabela em insertIntoTable()")
        return url_for('index')