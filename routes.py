from flask_mail import Message
from flask import render_template
from flask import request
from app import app
from flask_mail import Mail

from controllers.crudController import crudPage
from controllers.projectController import getProjectContent, createProject, readProject, updateProject, deleteProject

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projects/calorie")
def calorie():
    return render_template("wip.html")


@app.route("/projects/pageguild")
def pageguild():
    return getProjectContent("PageGuild")

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
def admin():
    return crudPage()

@app.route("/admin/project/create", methods=['POST'])
def createProjectRoute():
    return createProject(request)

@app.route("/admin/project/delete/<project_id>")
def deleteProjectRoute(project_id):
    return deleteProject(project_id)
