from tkinter import *
from tkinter import messagebox

#import pandas library
import pandas as pd

#import numpy library
import numpy as np

#import breast cancer dataset
from sklearn.datasets import load_breast_cancer

# import code fromthe library that will enable us divide our datasetset into training and test data
from sklearn.model_selection import train_test_split

#import the Support Vector Machine Model tat will enable us train our data
from sklearn.svm import SVC as gg

def get_user_input():
    # l1 = float(mean_radius_value.get())
    # l2 = float(mean_texture_value.get())
    # l3 = float(mean_perimeter_value.get())
    # l4 = float(mean_area_value.get())
    # l5 = float(mean_smoothness_value.get())
    # l6 = float(mean_compactness_value.get())
    # l7 = float(mean_concavity_value.get())
    # l8 = float(mean_concave_points_value.get())
    # l9 = float(mean_symmetry_value.get())
    # l10 = float(mean_fractal_dimension_value.get())
    # l11 = float(radius_error_value.get())
    # l12 = float(texture_error_value.get())
    # l13 = float(perimeter_error_value.get())
    # l14 = float(area_error_value.get())
    # l15 = float(smoothness_error_value.get())
    # l16 = float(compactness_error_value.get())
    # l17 = float(concavity_error_value.get())
    # l18 = float(concave_points_error_value.get())
    # l19 = float(symmetry_error_value.get())
    # l20 = float(fractal_dimension_error_value.get())
    # l21 = float(worst_radius_value.get())
    # l22 = float(worst_texture_value.get())
    # l23 = float(worst_perimeter_value.get())
    # l24 = float(worst_area_value.get())
    # l25 = float(worst_smoothness_value.get())
    # l26 = float(worst_compactness_value.get())
    # l27 = float(worst_concavity_value.get())
    # l28 = float(worst_concave_points_value.get())
    # l29 = float(worst_symmetry_value.get())
    # l30 = float(worst_fractal_dimension_value.get())
    #userInput = [{'mean radius': l1, 'mean texture': l2, 'mean perimeter': l3, 'mean area': l4, 'mean smoothness': l5, 'mean compactness': l6, 'mean concavity': l7, 'mean concave points': l8, 'mean symmetry': l9, 'mean fractal dimension': l10, 'radius error': l11, 'texture error': l12, 'perimeter error': l13, 'area error': l14, 'smoothness error': l15, 'compactness error': l16, 'concavity error': l17, 'concave points error': l18, 'symmetry error': l19, 'fractal dimension error': l20, 'worst radius' : l21, 'worst texture': l22, 'worst perimeter': l23, 'worst area': l24, 'worst smoothness': l25, 'worst compactness': l26, 'worst concavity': l27, 'worst concave points': l28,'worst symmetry' : l29, 'worst fractal dimension': l30}]
    userInput = ""
    diagnosis = diagnose(userInput);
    outputMessage = ""
    if diagnosis == 1:
        outputMessage = "The patient isn't having cancer"
    else:
        outputMessage = "The patient has cancer"
    messagebox.showinfo('Diagnosis', outputMessage)

def diagnose(userInput):
    #load breast cancer dataset and store it in a variable
    cancer = load_breast_cancer()

    #convert breast cancer data into panda dataframe, so we can analyse
    df_cancer = pd.DataFrame(np.c_[cancer['data'], cancer['target']], columns = np.append(cancer['feature_names'], ['target']))

    #We drop our "target" feature and use all the remaining features in our dataframe to train the model.
    X = df_cancer.drop(['target'], axis = 1) # We drop our "target" feature and use all the remaining features in our dataframe to train the model.
    
    #adding our user input to be diagnosed
    # X = X.append(userInput, ignore_index=True)

    #we use the target feature, since its what we are trying to prdict 
    y = df_cancer['target']

    #lets divide our data along a 80% to 20% border line
    #i.e 80% for training data and 20% for test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 20)

    #load our svm model
    svc_model = gg()

    #training our 80% training dataset
    svc_model.fit(X_train, y_train)

    #predicting with the trained tarining dataset
    # sales = [{'mean radius': 1, 'mean texture': 0.99876, 'mean perimeter': 2.5, 'mean area': 7.9, 'mean smoothness': 1, 'mean compactness': 150, 'mean concavity': 200, 'mean concave points': 140, 'mean symmetry': 150, 'mean fractal dimension': 200, 'radius error': 140, 'texture error': 150, 'perimeter error': 200, 'area error': 140, 'smoothness error': 150, 'compactness error': 200, 'concavity error': 140, 'concavity error': 150, 'concave points error': 200, 'symmetry error': 140, 'fractal dimension error': 123, 'worst radius' : 1, 'worst texture': 2, 'worst perimeter': 1, 'worst area': 2, 'worst smoothness': 2, 'worst compactness': 3, 'worst concavity': 5, 'worst concave points': 4,'worst symmetry' :4, 'worst fractal dimension': 12}]
    X_test = pd.DataFrame(userInput)
    y_predict = svc_model.predict(X_test)
    return y_predict[0]

userInputDataFrameOne = [[
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1
        ]]


window = Tk()

window.title("Breast Cancer Detector")
window.wm_iconbitmap("img/calc.ico")
window.configure(background = 'AntiqueWhite1')
# window.grid_columnconfigure(0, weight=1)
# window.grid_rowconfigure(0, weight=1)
window.resizable(True, True)


# ----------------------------

mean_radius_label = Label(window, text="mean radius")                                                                                                                                                                                                                                                                                                                                    
mean_radius_label.grid(row=0, column=0)
mean_radius_value = StringVar()
mean_radius = Entry(window, textvariable=mean_radius_value)
mean_radius.grid(row=1, column=0)

mean_texture_label = Label(window, text="mean texture")
mean_texture_label.grid(row=0, column=1)
mean_texture_value = StringVar()
mean_texture = Entry(window, textvariable=mean_texture_value)
mean_texture.grid(row=1, column=1)


mean_perimeter_label = Label(window, text="mean perimeter")
mean_perimeter_label.grid(row=0, column=2)
mean_perimeter_value = StringVar()
mean_perimeter= Entry(window, textvariable=mean_perimeter_value)
mean_perimeter.grid(row=1, column=2)

mean_area_label = Label(window, text="mean area")
mean_area_label.grid(row=0, column=3)
mean_area_value = StringVar()
mean_area= Entry(window, textvariable=mean_area_value)
mean_area.grid(row=1, column=3)

mean_smoothness_label = Label(window, text="mean smoothness")
mean_smoothness_label.grid(row=0, column=4)
mean_smoothness_value = StringVar()
mean_smoothness= Entry(window, textvariable=mean_smoothness_value)
mean_smoothness.grid(row=1, column=4)

# --------------------------------

mean_compactness_label = Label(window, text="mean compactness")
mean_compactness_label.grid(row=3, column=0)
mean_compactness_value = StringVar()
mean_compactness= Entry(window, textvariable=mean_compactness_value)
mean_compactness.grid(row=4, column=0)

mean_concavity_label = Label(window, text="mean concavity")
mean_concavity_label.grid(row=3, column=1)
mean_concavity_value = StringVar()
mean_concavity= Entry(window, textvariable=mean_concavity_value)
mean_concavity.grid(row=4, column=1)

mean_concave_points_label = Label(window, text="mean concave points")
mean_concave_points_label.grid(row=3, column=2)
mean_concave_points_value = StringVar()
mean_concave_points= Entry(window, textvariable=mean_concave_points_value)
mean_concave_points.grid(row=4, column=2)

mean_symmetry_label = Label(window, text="mean symmetry")
mean_symmetry_label.grid(row=3, column=3)
mean_symmetry_value = StringVar()
mean_symmetry = Entry(window, textvariable=mean_symmetry_value)
mean_symmetry.grid(row=4, column=3)

mean_fractal_dimension_label = Label(window, text="mean fractal dimension")
mean_fractal_dimension_label.grid(row=3, column=4)
mean_fractal_dimension_value = StringVar()
mean_fractal_dimension= Entry(window, textvariable=mean_fractal_dimension_value)
mean_fractal_dimension.grid(row=4, column=4)

# -------------------

radius_error_label = Label(window, text="radius error")
radius_error_label.grid(row=6, column=0)
radius_error_value = StringVar()
radius_error= Entry(window, textvariable=radius_error_value)
radius_error.grid(row=7, column=0)

texture_error_label = Label(window, text="texture error")
texture_error_label.grid(row=6, column=1)
texture_error_value = StringVar()
texture_error= Entry(window, textvariable=texture_error_value)
texture_error.grid(row=7, column=1)

perimeter_error_label = Label(window, text="perimeter error")
perimeter_error_label.grid(row=6, column=2)
perimeter_error_value = StringVar()
perimeter_error= Entry(window, textvariable=perimeter_error_value)
perimeter_error.grid(row=7, column=2)

area_error_label = Label(window, text="area error")
area_error_label.grid(row=6, column=3)
area_error_value = StringVar()
area_error= Entry(window, textvariable=area_error_value)
area_error.grid(row=7, column=3)

smoothness_error_label = Label(window, text="smoothness error")
smoothness_error_label.grid(row=6, column=4)
smoothness_error_value = StringVar()
smoothness_error= Entry(window, textvariable=smoothness_error_value)
smoothness_error.grid(row=7, column=4)

# --------

compactness_error_label = Label(window, text="compactness error")
compactness_error_label.grid(row=9, column=0)
compactness_error_value = StringVar()
compactness_error= Entry(window, textvariable=compactness_error_value)
compactness_error.grid(row=10, column=0)

concavity_error_label = Label(window, text="concavity error")
concavity_error_label.grid(row=9, column=1)
concavity_error_value = StringVar()
concavity_error= Entry(window, textvariable=concavity_error_value)
concavity_error.grid(row=10, column=1)

concave_points_error_label = Label(window, text="concave points error")
concave_points_error_label.grid(row=9, column=2)
concave_points_error_value = StringVar()
concave_points_error= Entry(window, textvariable=concave_points_error_value)
concave_points_error.grid(row=10, column=2)

symmetry_error_label = Label(window, text="symmetry error")
symmetry_error_label.grid(row=9, column=3)
symmetry_error_value = StringVar()
symmetry_error= Entry(window, textvariable=symmetry_error_value)
symmetry_error.grid(row=10, column=3)

fractal_dimension_error_label = Label(window, text="fractal dimension error")
fractal_dimension_error_label.grid(row=9, column=4)
fractal_dimension_error_value = StringVar()
fractal_dimension_error= Entry(window, textvariable=fractal_dimension_error_value)
fractal_dimension_error.grid(row=10, column=4)

# -----------

worst_radius_label = Label(window, text="worst radius")
worst_radius_label.grid(row=12, column=0)
worst_radius_value = StringVar()
worst_radius= Entry(window, textvariable=worst_radius_value)
worst_radius.grid(row=13, column=0)

worst_texture_label = Label(window, text="worst texture")
worst_texture_label.grid(row=12, column=1)
worst_texture_value = StringVar()
worst_texture= Entry(window, textvariable=worst_texture_value)
worst_texture.grid(row=13, column=1)

worst_perimeter_label = Label(window, text="worst perimeter")
worst_perimeter_label.grid(row=12, column=2)
worst_perimeter_value = StringVar()
worst_perimeter= Entry(window, textvariable=worst_perimeter_value)
worst_perimeter.grid(row=13, column=2)

worst_area_label = Label(window, text="worst area")
worst_area_label.grid(row=12, column=3)
worst_area_value = StringVar()
worst_area= Entry(window, textvariable=worst_area_value)
worst_area.grid(row=13, column=3)

worst_smoothness_label = Label(window, text="worst smoothness")
worst_smoothness_label.grid(row=12, column=4)
worst_smoothness_value = StringVar()
worst_smoothness= Entry(window, textvariable=worst_smoothness_value)
worst_smoothness.grid(row=13, column=4)

# ---------

worst_compactness_label = Label(window, text="worst compactness")
worst_compactness_label.grid(row=15, column=0)
worst_compactness_value = StringVar()
worst_compactness= Entry(window, textvariable=worst_compactness_value)
worst_compactness.grid(row=16, column=0)

worst_concavity_label = Label(window, text="worst concavity")
worst_concavity_label.grid(row=15, column=1)
worst_concavity_value = StringVar()
worst_concavity= Entry(window, textvariable=worst_concavity_value)
worst_concavity.grid(row=16, column=1)

worst_concave_points_label = Label(window, text="worst concave points")
worst_concave_points_label.grid(row=15, column=2)
worst_concave_points_value = StringVar()
worst_concave_points= Entry(window, textvariable=worst_concave_points_value)
worst_concave_points.grid(row=16, column=2)

worst_symmetry_label = Label(window, text="worst symmetry")
worst_symmetry_label.grid(row=15, column=3)
worst_symmetry_value = StringVar()
worst_symmetry= Entry(window, textvariable=worst_symmetry_value)
worst_symmetry.grid(row=16, column=3)

worst_fractal_dimension_label = Label(window, text="worst fractal dimension")
worst_fractal_dimension_label.grid(row=15, column=4)
worst_fractal_dimension_value = StringVar()
worst_fractal_dimension= Entry(window, textvariable=worst_fractal_dimension_value)
worst_fractal_dimension.grid(row=16, column=4)

b1 = Button(window, text="Diagnose", command=get_user_input)
b1.grid(row=20, column=2)

# ----------

window.mainloop()

