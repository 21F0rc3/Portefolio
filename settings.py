from app import app

################################
#          Email               #
################################

app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '4c68647ed5fca2'
app.config['MAIL_PASSWORD'] = 'e89a598455961d'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False