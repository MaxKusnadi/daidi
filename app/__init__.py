import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

logging.basicConfig(level=logging.INFO,
                    format=' %(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# Views
from app.daidi.views import *

# Models
from app.daidi.models.game import *
from app.daidi.models.player import *
from app.daidi.models.gameplayer import *
