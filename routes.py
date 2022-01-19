from flask import Flask
from flask import render_template
from flask_mail import Mail
from flask_mail import Message
from flask import request

import os

app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ['EMAIL_USER'],
    "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD']
}

app.config.update(mail_settings)
mail = Mail(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sendEmail", methods=['POST'])
def sendEmail():
    msg = Message(request.form['Assunto'],
                  body=request.form['Content'],
                  sender=request.form['Email'],
                  recipients=[os.environ['EMAIL_USER']]);

    mail.send(msg);
    return index();
