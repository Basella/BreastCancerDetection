from flask import Flask, render_template, url_for, redirect
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from frontend.forms import TextForm


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config.from_object(Config)
# app.config.from_pyfile('config.py')

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
# app.config.from_envvar(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from views.dashboard import dashboard_blueprint
from views.diagnose import diagnose_blueprint
from views.result import result
# from frontend.api import result as api_result
# from .util import assets

# register blueprint
app.register_blueprint(dashboard_blueprint)
app.register_blueprint(diagnose_blueprint)
app.register_blueprint(result)
# app.register_blueprint(api_result, url_prefix='/api')


@app.route('/')
def index():
    return render_template("layout.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard/dashboard.html")

@app.route('/diagnose', methods=["GET", "POST"])
def diagnose():
    form = TextForm()
    if form.validate_on_submit():
        return redirect(url_for('result'))
    return render_template('diagnose/diagnose.html', title='Diagnose', form=form)
