from flask import Flask

app = Flask(__name__)

# import defined files (Não e aconselhavel alterar a ordem dos import's)
import settings
import database
import routes