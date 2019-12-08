from flask import Flask, request, jsonify
# from models.models import Entry

app = Flask(__name__)
# @result.route('/result/<int:meanradiusvalue>/<int:meantexturevalue>/<int:meanperimetervalue>/<int:meanareavalue>/<int:meansmoothnessvalue>/<int:meancompactnessvalue>/<int:meanconcavityvalue>/<int:meanconcavepointsvalue>/<int:meansymmetryvalue>/<int:meanfractaldimensionvalue>/<int:radiuserrorvalue>/<int:textureerrorvalue>/<int:perimetererrorvalue>/<int:areaerrorvalue>/<int:smoothnesserrorvalue>/<int:compactnesserrorvalue>/<int:concavityerrorvalue>/<int:concavepointserrorvalue>/<int:symmetryerrorvalue>/<int:fractaldimensionerrorvalue>/<int:worstradiusvalue>/<int:worsttexturevalue>/<int:worstperimetervalue>/<int:worstareavalue>/<int:worstsmoothnessvalue>/<int:worstcompactnessvalue>/<int:worstconcavityvalue>/<int:worstconcavepointsvalue>/<int:worstsymmetryvalue>/<int:worstfractaldimensionvalue>', methods=['POST'])
# def get_result(meanradiusvalue, meantexturevalue, meanperimetervalue, meanareavalue, meansmoothnessvalue, meancompactnessvalue, meanconcavityvalue, meanconcavepointsvalue, meansymmetryvalue, meanfractaldimensionvalue, radiuserrorvalue, textureerrorvalue, perimetererrorvalue, areaerrorvalue, smoothnesserrorvalue, compactnesserrorvalue, concavityerrorvalue, concavepointserrorvalue, symmetryerrorvalue, fractaldimensionerrorvalue, worstradiusvalue, worsttexturevalue, worstperimetervalue, worstareavalue, worstsmoothnessvalue, worstcompactnessvalue, worstconcavityvalue, worstconcavepointsvalue, worstsymmetryvalue, worstfractaldimensionvalue):
    
#     return jsonify(Entry.query.get_or_404(meanradiusvalue, meantexturevalue, meanperimetervalue, meanareavalue, meansmoothnessvalue, meancompactnessvalue, meanconcavityvalue, meanconcavepointsvalue, meansymmetryvalue, meanfractaldimensionvalue, radiuserrorvalue, textureerrorvalue, perimetererrorvalue, areaerrorvalue, smoothnesserrorvalue, compactnesserrorvalue, concavityerrorvalue, concavepointserrorvalue, symmetryerrorvalue, fractaldimensionerrorvalue, worstradiusvalue, worsttexturevalue, worstperimetervalue, worstareavalue, worstsmoothnessvalue, worstcompactnessvalue, worstconcavityvalue, worstconcavepointsvalue, worstsymmetryvalue, worstfractaldimensionvalue).to_dict())




# @app.route('/api/testinput', methods=['POST'])
# def add_test_input():
#     all_inputs = []
#     if not request.json:
#         return "Not JSON"
#     test_input = {
#         'meanradiusvalue': request.json.get('meanradiusvalue'),
#         'meantexturevalue': request.json.get('meantexturevalue'),
#         'meanperimetervalue': request.json.get('meanperimetervalue'),
#         'meanareavalue': request.json.get('meanareavalue'),
#         'meansmoothnessvalue': request.json.get('meansmoothnessvalue'),
#         'meancompactnessvalue': request.json.get('meancompactnessvalue'),
#         'meanconcavityvalue': request.json.get('meanconcavityvalue'),
#         'meanconcavepointsvalue': request.json.get('meanconcavepointsvalue'),
#         'meansymmetryvalue': request.json.get('meansymmetryvalue'),
#         'meanfractaldimensionvalue': request.json.get('meanfractaldimensionvalue'),
#         'radiuserrorvalue': request.json.get('radiuserrorvalue'),
#         'textureerrorvalue': request.json.get('textureerrorvalue'),
#         'perimetererrorvalue': request.json.get('perimetererrorvalue'),
#         'areaerrorvalue': request.json.get('areaerrorvalue'),
#         'smoothnesserrorvalue': request.json.get('smoothnesserrorvalue'),
#         'compactnesserrorvalue': request.json.get('compactnesserrorvalue'),
#         'concavityerrorvalue': request.json.get('concavityerrorvalue'),
#         'concavepointserrorvalue': request.json.get('concavepointserrorvalue'),
#         'symmetryerrorvalue': request.json.get('symmetryerrorvalue'),
#         'fractaldimensionerrorvalue': request.json.get('fractaldimensionerrorvalue'),
#         'worstradiusvalue': request.json.get('worstradiusvalue'),
#         'worsttexturevalue': request.json.get('worsttexturevalue'),
#         'worstperimetervalue': request.json.get('worstperimetervalue'),
#         'worstareavalue': request.json.get('worstareavalue'),
#         'worstsmoothnessvalue': request.json.get('worstsmoothnessvalue'),
#         'worstcompactnessvalue': request.json.get('worstcompactnessvalue'),
#         'worstconcavityvalue': request.json.get('worstconcavityvalue'),
#         'worstconcavepointsvalue': request.json.get('worstconcavepointsvalue'),
#         'worstsymmetryvalue': request.json.get('worstsymmetryvalue'),
#         'worstfractaldimensionvalue': request.json.get('worstfractaldimensionvalue'),
#     }

#     # all_inputs.append(test_input)

#     return jsonify({ 'input' : test_input }), 201

# app.run()

#import pandas library
import pandas as pd

#import numpy library
import numpy as np

#import matplotlib library
import matplotlib.pyplot as plt

#import seaborn library
import seaborn as sns

#import breast cancer dataset
from sklearn.datasets import load_breast_cancer

@app.route('/api/falseinput', methods=['POST'])
def trythis():
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

    changedData = pd.DataFrame(test_input)

    #load breast cancer dataset and store it in a variable
    cancer = load_breast_cancer()

    #convert breast cancer data into panda dataframe, so we can analyse
    df_cancer = pd.DataFrame(np.c_[cancer['data'], cancer['target']], columns = np.append(cancer['feature_names'], ['target']))

    #We drop our "target" feature and use all the remaining features in our dataframe to train the model.
    X = df_cancer.drop(['target'], axis = 1)

    #we use the target feature, since its what we are trying to predict 
    y = df_cancer['target']

    #create our test and training data from our dataset
    # import code fromthe library that will enable us divide our datasetset into training and test data
    from sklearn.model_selection import train_test_split

    #import the Support Vector Machine Model that will enable us train our data
    from sklearn.svm import SVC as gg
    #load our svm model
    svc_model = gg()

    #training with our training dataset
    svc_model.fit(X, y)

    #lets improve our model by normalizing our training data 
    X_min = X.min()
    X_max = X.max()
    X_range = (X_max- X_min)
    X_scaled = (X - X_min)/(X_range)

    #lets improve our model by normalizing our test data 
    changedData_min = changedData.min()
    changedData_range = (changedData - changedData_min).max()
    changedData_scaled = (changedData - changedData_min)/changedData_range

    #lets load our Support Vector Machine Model again and train our data with it furthermore
    svc_model = gg()
    #training our 80% normailised training dataset
    svc_model.fit(X_scaled, y)

    #lets predict with our training dataset
    y_predict = svc_model.predict(changedData)
    print(y_predict)
    if y_predict == 0:
        return "You do not have cancer"
    return "You have cancer"

# app.debug = True
app.run()