from flask import Blueprint, render_template, redirect, url_for

result = Blueprint('result', __name__)

# @result.route('/result/<int:meanradiusvalue>/<int:meantexturevalue>/<int:meanperimetervalue>/<int:meanareavalue>/<int:meansmoothnessvalue>/<int:meancompactnessvalue>/<int:meanconcavityvalue>/<int:meanconcavepointsvalue>/<int:meansymmetryvalue>/<int:meanfractaldimensionvalue>/<int:radiuserrorvalue>/<int:textureerrorvalue>/<int:perimetererrorvalue>/<int:areaerrorvalue>/<int:smoothnesserrorvalue>/<int:compactnesserrorvalue>/<int:concavityerrorvalue>/<int:concavepointserrorvalue>/<int:symmetryerrorvalue>/<int:fractaldimensionerrorvalue>/<int:worstradiusvalue>/<int:worsttexturevalue>/<int:worstperimetervalue>/<int:worstareavalue>/<int:worstsmoothnessvalue>/<int:worstcompactnessvalue>/<int:worstconcavityvalue>/<int:worstconcavepointsvalue>/<int:worstsymmetryvalue>/<int:worstfractaldimensionvalue>')
# def resultpage(meanradiusvalue, meantexturevalue, meanperimetervalue, meanareavalue, meansmoothnessvalue, meancompactnessvalue, meanconcavityvalue, meanconcavepointsvalue, meansymmetryvalue, meanfractaldimensionvalue, radiuserrorvalue, textureerrorvalue, perimetererrorvalue, areaerrorvalue, smoothnesserrorvalue, compactnesserrorvalue, concavityerrorvalue, concavepointserrorvalue, symmetryerrorvalue, fractaldimensionerrorvalue, worstradiusvalue, worsttexturevalue, worstperimetervalue, worstareavalue, worstsmoothnessvalue, worstcompactnessvalue, worstconcavityvalue, worstconcavepointsvalue, worstsymmetryvalue, worstfractaldimensionvalue):
    
#     return render_template('result/result.html')