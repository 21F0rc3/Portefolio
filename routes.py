from flask_mail import Message
from flask import render_template
from flask import request, session
from app import app
from flask_mail import Mail
from flask_security import Security, SQLAlchemyUserDatastore, auth_required, hash_password
from database import db, user_datastore
from models.project import project
from flask_babel import Babel, gettext

from controllers.crudController import *
from controllers.projectController import getProjectContent, createProject, readProject, updateProject, deleteProject
from controllers.sectionController import createSection, updateSection, deleteSection

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







@app.route("/admin/delete/<table>/<id>")
def deleteRoute(table, id):
    return deleteTableRecord(table, id)

@app.route("/admin/create/<table>", methods=['POST'])
def createRoute(table):
    return createTableRecord(table, request)

@app.route("/admin/update/<table>", methods=['POST'])
def updateRoute(table):
    return updateTableRecord(table, request)




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