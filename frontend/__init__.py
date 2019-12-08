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

@app.route('/diagnose', methods=["GET", "POST"])
def diagnose():
    form = TextForm()
    # if form.validate_on_submit():
    #     return redirect(url_for('result'))
    return render_template('diagnose/diagnose.html', title='Diagnose', form=form)

@app.route('/api/get_user_input', methods=["POST", "GET"])
def inp():
    meanradiusvalue = request.form.get('radValues')
    meantexturevalue = request.form.get('textureValues')
    meanperimetervalue = request.form.get('perValues')
    meanareavalue = request.form.get('areaValues')
    meansmoothnessvalue = request.form.get('smoothValues')
    meancompactnessvalue = request.form.get('compactValues')
    meanconcavityvalue = request.form.get('concaveValues')
    meanconcavepointsvalue = request.form.get('cpointsValues')
    meansymmetryvalue = request.form.get('symValues')
    meanfractaldimensionvalue = request.form.get('fractValues')
    radiuserrorvalue = request.form.get('raderrValues')
    textureerrorvalue = request.form.get('textureerrValues')
    perimetererrorvalue = request.form.get('pererrValues')
    areaerrorvalue = request.form.get('areaerrValues')
    smoothnesserrorvalue = request.form.get('smootherrValues')
    compactnesserrorvalue = request.form.get('compacterrValues')
    concavityerrorvalue = request.form.get('concaveerrValues')
    concavepointserrorvalue = request.form.get('cpointserrValues')
    symmetryerrorvalue = request.form.get('symerrValues')
    fractaldimensionerrorvalue = request.form.get('fracterrValues')
    worstradiusvalue = request.form.get('wradValues')
    worsttexturevalue = request.form.get('wtextureValues')
    worstperimetervalue = request.form.get('wperValues')
    worstareavalue = request.form.get('wareaValues')
    worstsmoothnessvalue = request.form.get('wsmoothValues')
    worstcompactnessvalue = request.form.get('wcompactValues')
    worstconcavityvalue = request.form.get('wconcaveValues')
    worstconcavepointsvalue = request.form.get('wcpointsValues')
    worstsymmetryvalue = request.form.get('wsymValues')
    worstfractaldimensionvalue = request.form.get('wfractValues')

    print(meanradiusvalue);
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

    resultValue = test_result.get_user_input(test_input)

    redirect('/result/<int:resultValue>')
    app.run()


@app.route('/result/<int:resultValue>', methods=["GET"])
def resultpage(resultValue):
    if resultValue == 0:
        resultString = "You do not have cancer"
        return redirect(url_for('result/<string:resultString>'))
    
    resultString = "You have cancer"
    return redirect(url_for('result/<string:resultString>'))
