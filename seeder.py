from models.project import project
from models.section import section
from models.file import file
from models.image import image

from database import db

#############################################
#   Use this file to execute SQL inserts    #
#############################################

#pageguild = project(name='PageGuild')

#resumo = section(title='Resumo', content_file='pageguild-resumo.txt', project_id='1')

#db.session.add(pageguild)
#db.session.add(resumo)
#db.session.commit()