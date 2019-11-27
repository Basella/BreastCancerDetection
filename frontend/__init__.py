from flask import Flask, render_template, url_for
# import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)