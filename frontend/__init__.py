from flask import Flask, render_template, url_for, redirect, request
from config import Config
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from frontend.forms import TextForm
from waitress import serve


app = Flask(__name__)
app.config.from_object(Config)

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
# app.config.from_envvar(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from views.diagnose import diagnose_blueprint
from views.result import result
from frontend.api import note as test_result
# from .util import assets

# register blueprint
app.register_blueprint(diagnose_blueprint)
app.register_blueprint(result)

@app.route('/')
def index():
    return render_template("layout.html")

@app.route('/diagnose', methods=["GET", "POST"])
def diagnose():
    form = TextForm()
    return render_template('diagnose/diagnose.html', title='Diagnose', form=form)

@app.route('/api/get_user_input', methods=["POST", "GET"])
def inp():
    meanradiusvalue = request.form.get('meanradiusvalue')
    meantexturevalue = request.form.get('meantexturevalue')
    meanperimetervalue = request.form.get('meanperimetervalue')
    meanareavalue = request.form.get('meanareavalue')
    meansmoothnessvalue = request.form.get('meansmoothnessvalue')
    meancompactnessvalue = request.form.get('meancompactnessvalue')
    meanconcavityvalue = request.form.get('meanconcavityvalue')
    meanconcavepointsvalue = request.form.get('meanconcavepointsvalue')
    meansymmetryvalue = request.form.get('meansymmetryvalue')
    meanfractaldimensionvalue = request.form.get('meanfractaldimensionvalue')
    radiuserrorvalue = request.form.get('radiuserrorvalue')
    textureerrorvalue = request.form.get('textureerrorvalue')
    perimetererrorvalue = request.form.get('perimetererrorvalue')
    areaerrorvalue = request.form.get('areaerrorvalue')
    smoothnesserrorvalue = request.form.get('smoothnesserrorvalue')
    compactnesserrorvalue = request.form.get('compactnesserrorvalue')
    concavityerrorvalue = request.form.get('concavityerrorvalue')
    concavepointserrorvalue = request.form.get('concavepointserrorvalue')
    symmetryerrorvalue = request.form.get('symmetryerrorvalue')
    fractaldimensionerrorvalue = request.form.get('fractaldimensionerrorvalue')
    worstradiusvalue = request.form.get('worstradiusvalue')
    worsttexturevalue = request.form.get('worsttexturevalue')
    worstperimetervalue = request.form.get('worstperimetervalue')
    worstareavalue = request.form.get('worstareavalue')
    worstsmoothnessvalue = request.form.get('worstsmoothnessvalue')
    worstcompactnessvalue = request.form.get('worstcompactnessvalue')
    worstconcavityvalue = request.form.get('worstconcavityvalue')
    worstconcavepointsvalue = request.form.get('worstconcavepointsvalue')
    worstsymmetryvalue = request.form.get('worstsymmetryvalue')
    worstfractaldimensionvalue = request.form.get('worstfractaldimensionvalue')

    test_input = [
    {
        'meanradiusvalue': float(meanradiusvalue),
        'meantexturevalue': float(meantexturevalue),
        'meanperimetervalue': float(meanperimetervalue),
        'meanareavalue': float(meanareavalue),
        'meansmoothnessvalue': float(meansmoothnessvalue),
        'meancompactnessvalue': float(meancompactnessvalue),
        'meanconcavityvalue': float(meanconcavityvalue),
        'meanconcavepointsvalue': float(meanconcavepointsvalue),
        'meansymmetryvalue': float(meansymmetryvalue),
        'meanfractaldimensionvalue': float(meanfractaldimensionvalue),
        'radiuserrorvalue': float(radiuserrorvalue),
        'textureerrorvalue': float(textureerrorvalue),
        'perimetererrorvalue': float(perimetererrorvalue),
        'areaerrorvalue': float(areaerrorvalue),
        'smoothnesserrorvalue': float(smoothnesserrorvalue),
        'compactnesserrorvalue': float(compactnesserrorvalue),
        'concavityerrorvalue': float(concavityerrorvalue),
        'concavepointserrorvalue': float(concavepointserrorvalue),
        'symmetryerrorvalue': float(symmetryerrorvalue),
        'fractaldimensionerrorvalue': float(fractaldimensionerrorvalue),
        'worstradiusvalue': float(worstradiusvalue),
        'worsttexturevalue': float(worsttexturevalue),
        'worstperimetervalue': float(worstperimetervalue),
        'worstareavalue': float(worstareavalue),
        'worstsmoothnessvalue': float(worstsmoothnessvalue),
        'worstcompactnessvalue': float(worstcompactnessvalue),
        'worstconcavityvalue': float(worstconcavityvalue),
        'worstconcavepointsvalue': float(worstconcavepointsvalue),
        'worstsymmetryvalue': float(worstsymmetryvalue),
        'worstfractaldimensionvalue': float(worstfractaldimensionvalue)
    }]

    resultValue = test_result.get_user_input(test_input)

    return redirect(url_for('resultpage', resultValue=resultValue, test_input=test_input))



@app.route('/result/<int:resultValue>/<test_input>', methods=["GET"])
def resultpage(resultValue, test_input):
        return render_template("result/result.html", resultValue=resultValue, test_input=test_input)


if __name__ == '__main__':
        # app.run()
        serve(app)