from flask import Flask, render_template, url_for, redirect, request
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
from frontend.api import note as test_result
# from .util import assets

# register blueprint
app.register_blueprint(dashboard_blueprint)
app.register_blueprint(diagnose_blueprint)
app.register_blueprint(result)
# app.register_blueprint(test_result, url_prefix='/api')

@app.route('/')
def index():
    return render_template("layout.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard/dashboard.html")

@app.route('/diagnose', methods=["GET", "POST"])
def diagnose():
    form = TextForm()
    # if form.validate_on_submit():
    #     return redirect(url_for('result'))
    return render_template('diagnose/diagnose.html', title='Diagnose', form=form)

@app.route('/api/get_user_input', methods=[POST])
def inp():
    meanradiusvalue = request.form.get('radValue')
    meantexturevalue = request.form.get('textureValue')
    meanperimetervalue = request.form.get('perValue')
    meanareavalue = request.form.get('areaValue')
    meansmoothnessvalue = request.form.get('smoothValue')
    meancompactnessvalue = request.form.get('compactValue')
    meanconcavityvalue = request.form.get('concaveValue')
    meanconcavepointsvalue = request.form.get('cpointsValue')
    meansymmetryvalue = request.form.get('symValue')
    meanfractaldimensionvalue = request.form.get('fractValue')
    radiuserrorvalue = request.form.get('raderrValue')
    textureerrorvalue = request.form.get('textureerrValue')
    perimetererrorvalue = request.form.get('pererrValue')
    areaerrorvalue = request.form.get('areaerrValue')
    smoothnesserrorvalue = request.form.get('smootherrValue')
    compactnesserrorvalue = request.form.get('compacterrValue')
    concavityerrorvalue = request.form.get('concaveerrValue')
    concavepointserrorvalue = request.form.get('cpointserrValue')
    symmetryerrorvalue = request.form.get('symerrValue')
    fractaldimensionerrorvalue = request.form.get('fracterrValue')
    worstradiusvalue = request.form.get('wradValue')
    worsttexturevalue = request.form.get('wtextureValue')
    worstperimetervalue = request.form.get('wperValue')
    worstareavalue = request.form.get('wareaValue')
    worstsmoothnessvalue = request.form.get('wsmoothValue')
    worstcompactnessvalue = request.form.get('wcompactValue')
    worstconcavityvalue = request.form.get('wconcaveValue')
    worstconcavepointsvalue = request.form.get('wcpointsValue')
    worstsymmetryvalue = request.form.get('wsymValue')
    worstfractaldimensionvalue = request.form.get('wfractValue')


    test_input = [
    {
        'meanradiusvalue': meanradiusvalue,
        'meantexturevalue': meantexturevalue,
        'meanperimetervalue':meanperimetervalue,
        'meanareavalue': meanareavalue,
        'meansmoothnessvalue': meansmoothnessvalue,
        'meancompactnessvalue': meancompactnessvalue,
        'meanconcavityvalue': meanconcavityvalue,
        'meanconcavepointsvalue': meanconcavepointsvalue,
        'meansymmetryvalue': meansymmetryvalue,
        'meanfractaldimensionvalue': meanfractaldimensionvalue,
        'radiuserrorvalue': radiuserrorvalue,
        'textureerrorvalue': textureerrorvalue,
        'perimetererrorvalue': perimetererrorvalue,
        'areaerrorvalue': areaerrorvalue,
        'smoothnesserrorvalue': smoothnesserrorvalue,
        'compactnesserrorvalue': compactnesserrorvalue,
        'concavityerrorvalue': concavityerrorvalue,
        'concavepointserrorvalue': concavepointserrorvalue,
        'symmetryerrorvalue': symmetryerrorvalue,
        'fractaldimensionerrorvalue': fractaldimensionerrorvalue,
        'worstradiusvalue': worstradiusvalue,
        'worsttexturevalue': worsttexturevalue,
        'worstperimetervalue': worstperimetervalue,
        'worstareavalue': worstareavalue,
        'worstsmoothnessvalue': worstsmoothnessvalue,
        'worstcompactnessvalue': worstcompactnessvalue,
        'worstconcavityvalue': worstconcavityvalue,
        'worstconcavepointsvalue': worstconcavepointsvalue,
        'worstsymmetryvalue': worstsymmetryvalue,
        'worstfractaldimensionvalue': worstfractaldimensionvalue
    }]

    result = test_result.get_user_input(test_input)

    app.run()
    redirect(url_for('result'))

