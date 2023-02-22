from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_moment import Moment

app = Flask(__name__)

app.config.from_object(Config)

#ORM - Obejct relational mapper - flask-sqlalchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)
moment= Moment(app)

from . import routes, models

#C - POST
#R - GET
#U -PUT/PATCH
#D - DELETE