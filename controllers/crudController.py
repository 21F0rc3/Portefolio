from controllers.controllerImports import *

"""
    Redireciona para a pagina de admin onde podemos manipular a base de dados
"""
def crudPage():
    tables = []

    tables.append(Table(project))
    tables.append(Table(section))
    tables.append(Table(file))
    tables.append(Table(image))

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

"""
    Lida com o tipo de model/tabela que pretendemos formatar e chama o formatador correspondente.

    Assim, podemos ter todas as diferentes tabelas com os diferentes dados, todos em arrays de arrays da class Table, na table_content.
    Isto ajuda a iterar sobre os diferentes dados nas templates, assim como deixar tudo dinamico.
"""
def formatQueryRows(model, queryResults):
    if model == project:
        return formatQueryRowsIntoProject(queryResults)
    if model == section:
        return formatQueryRowsIntoSection(queryResults)
    if model == file:
        return formatQueryRowsIntoFile(queryResults)
    if model == image:
        return formatQueryRowsIntoImage(queryResults)
    else:
        print ("ERRO: Não foi reconhecido o model em formatQueryRows()")
        return url_for('index')

"""
    Formata os resultados da tabela de Project para a classe Table

    Isto é importante para depois usarmos a classe Table para percorrer os resultados de todas as tabelas nas templates.
    Ele junta os dados de um project num array com cada uma das colunas e junta numa lista de todas as linhas dos resultados da query
"""
def formatQueryRowsIntoProject(queryResults):
    results = []

    for row in queryResults:
        rowColumns = [row.id,row.name,row.logo_file_id,row.description,row.keywords]
        results.append(rowColumns)

    return results

"""
    Fortmata os resultados da tabela de Section para a classe Table

    Isto é importante para depois usarmos a classe Table para percorrer os resultados de todas as tabelas nas templates.
    Ele junta os dados de uma section num array com cada uma das colunas e junta numa lista de todas as linhas dos resultados da query
"""
def formatQueryRowsIntoSection(queryResults):
    results = []

    for row in queryResults:
        rowColumns = [row.id,row.title,row.image_file_id,row.content_file_id,row.project_id]
        results.append(rowColumns)

    return results

"""
    Fortmata os resultados da tabela de File para a classe Table

    Isto é importante para depois usarmos a classe Table para percorrer os resultados de todas as tabelas nas templates.
    Ele junta os dados de uma section num array com cada uma das colunas e junta numa lista de todas as linhas dos resultados da query
"""
def formatQueryRowsIntoFile(queryResults):
    results = []

    for row in queryResults:
        rowColumns = [row.id,row.filename]
        results.append(rowColumns)

    return results

"""
    Fortmata os resultados da tabela de Image para a classe Table

    Isto é importante para depois usarmos a classe Table para percorrer os resultados de todas as tabelas nas templates.
    Ele junta os dados de uma section num array com cada uma das colunas e junta numa lista de todas as linhas dos resultados da query
"""
def formatQueryRowsIntoImage(queryResults):
    results = []

    for row in queryResults:
        rowColumns = [row.id,row.image_file]
        results.append(rowColumns)

    return results


"""
    Lida com os pedidos para eliminar um item da base de dados.
    Verifica qual o tipo de tabela e chama o controlador correspondente para eliminar a linha especicada com o id

    table - Tabela de onde pretendemos eliminar. Neste caso pode ser interpretado como um dos models
    id - Id do elemento que pretendemos eliminar
"""
def deleteTableRecord(table, id):
    if table == 'project':
        return deleteProject(id)
    if table == 'section':
        return deleteSection(id)
    if table == 'file':
        return deleteFile(id)
    if table == 'image':
        return deleteImage(id)
    else:
        print ("ERROR: Não foi renconhecida a tabela em deleteFromTable()")
        return url_for('index')

"""
    Lida com os pedidos para criar um item na base de dados.
    Verifica qual o tipo de tabela e chama o controlador correspondente para inserir a nova linha

    table - Tabela de onde pretendemos criar. Neste caso pode ser interpretado como um dos models
    request - Form com todos os dados
"""
def createTableRecord(table, request):
    if table == 'project':
        return createProject(request)
    if table == 'section':
        return createSection(request)
    if table == 'file':
        return createFile(request)
    if table == 'image':
        return createImage(request)
    else:
        print ("ERROR: Não foi renconhecida a tabela em insertIntoTable()")
        return url_for('index')

"""
    Lida com os pedidos para atualizar um item na base de dados.
    Verifica qual o tipo de tabela e chama o controlador correspondente para atualizar o item

    table - Tabela de onde pretendemos atualizar. Neste caso pode ser interpretado como um dos models
    request - Form com todos os dados novos(ou antigos)
"""
def updateTableRecord(table, request):
    if table == 'project':
        return updateProject(request)
    if table == 'section':
        return updateSection(request)
    if table == 'file':
        return updateFile(request)
    if table == 'image':
        return updateImage(request)
    else:
        print ("ERROR: Não foi renconhecida a tabela em insertIntoTable()")
        return url_for('index')