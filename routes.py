from flask_mail import Message
from flask import render_template
from flask import request, session
from app import app
from flask_mail import Mail
from flask_security import Security, SQLAlchemyUserDatastore, auth_required, hash_password
from database import db, user_datastore
from models.project import project
from flask_babel import Babel, gettext

from controllers.crudController import crudPage
from controllers.projectController import getProjectContent, createProject, readProject, updateProject, deleteProject
from controllers.sectionController import createSection, updateSection, deleteSection

babel = Babel(app)
@babel.localeselector
def get_locale():
    # if the user has set up the language manually it will be stored in the session,
    # so we use the locale from the user settings
    try:
        language = session['language']
    except KeyError:
        language = None
    if language is not None:
        return language
    return request.accept_languages.best_match(app.config['LANGUAGES'].keys())

@app.route('/language/<language>')
def set_language(language=None):
    session['language'] = language
    return index()

@app.context_processor
def inject_conf_var():
    return dict(
                AVAILABLE_LANGUAGES=app.config['LANGUAGES'],
                CURRENT_LANGUAGE=session.get('language',request.accept_languages.best_match(app.config['LANGUAGES'].keys())))


@app.route("/")
def index():
    projects = project.query.all()

    return render_template("index.html", projects=projects)

@app.route("/projects/<project_name>")
def seeProjectDetails(project_name):
    return readProject(project_name)

@app.route("/sendEmail", methods=['POST'])
def sendEmail():
    mail = Mail(app)

    msg = Message(request.form['Assunto'],
                  body=request.form['Content'],
                  sender=request.form['Email'],
                  recipients=['gabrielforce21@gmail.com'])

    mail.send(msg)
    return index()


#############################
#       Admin / CRUD        #
#############################

@app.route("/admin")
@auth_required()
def admin():
    return crudPage()

@app.route("/admin/project/create", methods=['POST'])
@auth_required()
def createProjectRoute():
    return createProject(request)

@app.route("/admin/project/update", methods=['POST'])
@auth_required()
def updateProjectRoute():
    return updateProject(request)

@app.route("/admin/project/delete/<project_id>")
@auth_required()
def deleteProjectRoute(project_id):
    return deleteProject(project_id)


@app.route("/admin/section/create", methods=['POST'])
@auth_required()
def createSectionRoute():
    return createSection(request)

@app.route("/admin/section/update", methods=['POST'])
@auth_required()
def updateSectionRoute():
    return updateSection(request)

@app.route("/admin/section/delete/<section_id>")
@auth_required()
def deleteSectionRoute(section_id):
    return deleteSection(section_id)