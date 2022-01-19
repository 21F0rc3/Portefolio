from flask import Flask
from flask import render_template
from flask_mail import Mail
from flask_mail import Message
from flask import request

import os

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '4c68647ed5fca2'
app.config['MAIL_PASSWORD'] = 'e89a598455961d'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sendEmail", methods=['POST'])
def sendEmail():
    msg = Message(request.form['Assunto'],
                  body=request.form['Content'],
                  sender=request.form['Email'],
                  recipients=['gabrielforce21@gmail.com'];

    mail.send(msg);
    return index();
