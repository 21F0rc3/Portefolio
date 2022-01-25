from app import app
import os

################################
#          Email               #
################################

app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '4c68647ed5fca2'
app.config['MAIL_PASSWORD'] = 'e89a598455961d'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

################################
#           Security           #
################################

# Generate a nice key using secrets.token_urlsafe()
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", 'pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw')
# Bcrypt is set as default SECURITY_PASSWORD_HASH, which requires a salt
# Generate a good salt using: secrets.SystemRandom().getrandbits(128)
app.config['SECURITY_PASSWORD_SALT'] = os.environ.get("SECURITY_PASSWORD_SALT", '146585145368132386173505678016728509634')

################################
#           Database           #
################################

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portefolio.db'
