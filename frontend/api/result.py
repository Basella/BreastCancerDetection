from flask import Flask, request, jsonify
# from models.models import Entry

app = Flask(__name__)
# @result.route('/result/<int:meanradiusvalue>/<int:meantexturevalue>/<int:meanperimetervalue>/<int:meanareavalue>/<int:meansmoothnessvalue>/<int:meancompactnessvalue>/<int:meanconcavityvalue>/<int:meanconcavepointsvalue>/<int:meansymmetryvalue>/<int:meanfractaldimensionvalue>/<int:radiuserrorvalue>/<int:textureerrorvalue>/<int:perimetererrorvalue>/<int:areaerrorvalue>/<int:smoothnesserrorvalue>/<int:compactnesserrorvalue>/<int:concavityerrorvalue>/<int:concavepointserrorvalue>/<int:symmetryerrorvalue>/<int:fractaldimensionerrorvalue>/<int:worstradiusvalue>/<int:worsttexturevalue>/<int:worstperimetervalue>/<int:worstareavalue>/<int:worstsmoothnessvalue>/<int:worstcompactnessvalue>/<int:worstconcavityvalue>/<int:worstconcavepointsvalue>/<int:worstsymmetryvalue>/<int:worstfractaldimensionvalue>', methods=['POST'])
# def get_result(meanradiusvalue, meantexturevalue, meanperimetervalue, meanareavalue, meansmoothnessvalue, meancompactnessvalue, meanconcavityvalue, meanconcavepointsvalue, meansymmetryvalue, meanfractaldimensionvalue, radiuserrorvalue, textureerrorvalue, perimetererrorvalue, areaerrorvalue, smoothnesserrorvalue, compactnesserrorvalue, concavityerrorvalue, concavepointserrorvalue, symmetryerrorvalue, fractaldimensionerrorvalue, worstradiusvalue, worsttexturevalue, worstperimetervalue, worstareavalue, worstsmoothnessvalue, worstcompactnessvalue, worstconcavityvalue, worstconcavepointsvalue, worstsymmetryvalue, worstfractaldimensionvalue):
    
#     return jsonify(Entry.query.get_or_404(meanradiusvalue, meantexturevalue, meanperimetervalue, meanareavalue, meansmoothnessvalue, meancompactnessvalue, meanconcavityvalue, meanconcavepointsvalue, meansymmetryvalue, meanfractaldimensionvalue, radiuserrorvalue, textureerrorvalue, perimetererrorvalue, areaerrorvalue, smoothnesserrorvalue, compactnesserrorvalue, concavityerrorvalue, concavepointserrorvalue, symmetryerrorvalue, fractaldimensionerrorvalue, worstradiusvalue, worsttexturevalue, worstperimetervalue, worstareavalue, worstsmoothnessvalue, worstcompactnessvalue, worstconcavityvalue, worstconcavepointsvalue, worstsymmetryvalue, worstfractaldimensionvalue).to_dict())




@app.route('/api/testinput', methods=['POST'])
def add_test_input():
    all_inputs = []
    if not request.json:
        return "Not JSON"
    test_input = {
        'meanradiusvalue': request.json.get('meanradiusvalue'),
        'meantexturevalue': request.json.get('meantexturevalue'),
        'meanperimetervalue': request.json.get('meanperimetervalue'),
        'meanareavalue': request.json.get('meanareavalue'),
        'meansmoothnessvalue': request.json.get('meansmoothnessvalue'),
        'meancompactnessvalue': request.json.get('meancompactnessvalue'),
        'meanconcavityvalue': request.json.get('meanconcavityvalue'),
        'meanconcavepointsvalue': request.json.get('meanconcavepointsvalue'),
        'meansymmetryvalue': request.json.get('meansymmetryvalue'),
        'meanfractaldimensionvalue': request.json.get('meanfractaldimensionvalue'),
        'radiuserrorvalue': request.json.get('radiuserrorvalue'),
        'textureerrorvalue': request.json.get('textureerrorvalue'),
        'perimetererrorvalue': request.json.get('perimetererrorvalue'),
        'areaerrorvalue': request.json.get('areaerrorvalue'),
        'smoothnesserrorvalue': request.json.get('smoothnesserrorvalue'),
        'compactnesserrorvalue': request.json.get('compactnesserrorvalue'),
        'concavityerrorvalue': request.json.get('concavityerrorvalue'),
        'concavepointserrorvalue': request.json.get('concavepointserrorvalue'),
        'symmetryerrorvalue': request.json.get('symmetryerrorvalue'),
        'fractaldimensionerrorvalue': request.json.get('fractaldimensionerrorvalue'),
        'worstradiusvalue': request.json.get('worstradiusvalue'),
        'worsttexturevalue': request.json.get('worsttexturevalue'),
        'worstperimetervalue': request.json.get('worstperimetervalue'),
        'worstareavalue': request.json.get('worstareavalue'),
        'worstsmoothnessvalue': request.json.get('worstsmoothnessvalue'),
        'worstcompactnessvalue': request.json.get('worstcompactnessvalue'),
        'worstconcavityvalue': request.json.get('worstconcavityvalue'),
        'worstconcavepointsvalue': request.json.get('worstconcavepointsvalue'),
        'worstsymmetryvalue': request.json.get('worstsymmetryvalue'),
        'worstfractaldimensionvalue': request.json.get('worstfractaldimensionvalue'),
    }

    # all_inputs.append(test_input)

    return jsonify({ 'input' : test_input }), 201

app.run()