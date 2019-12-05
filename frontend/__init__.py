from .util import assets
from flask import Flask, render_template, url_for
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from views.dashboard import dashboard
from views.diagnose import diagnose
from views.result import result
from frontend.api import result as api_result


app = Flask(__name__)
db = SQLAlchemy(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config.from_object(Config)
# app.config.from_pyfile('config.py')

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
# app.config.from_envvar(Config)


migrate = Migrate(app, db)

# register blueprint
app.register_blueprint(dashboard)
app.register_blueprint(diagnose)
app.register_blueprint(result)
app.register_blueprint(api_result, url_prefix='/api')


@app.route('/')
def index():
    return render_template("dashboard/dashboard.html")
