from flask_mail import Message
from flask import render_template
from flask import request
from app import app
from flask_mail import Mail

from controllers.projectController import getProjectContent

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