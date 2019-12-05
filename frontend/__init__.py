from flask import Flask, render_template, url_for
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from views.dashboard import dashboard
from views.diagnose import diagnose
from views.result import result
from frontend.api import bp as api_bp


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config.from_object(config)

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
app.config.from_envvar(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# register blueprint
app.register_blueprint(dashboard)
app.register_blueprint(diagnose)
app.register_blueprint(result)
app.register_blueprint(api_bp, url_prefix='/api')

from .util import assets

@app.route('/dashboard')
def index():
    return render_template("dashboard/dashboard.html")
