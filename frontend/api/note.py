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

#import random number generator
from random import seed
from random import randint

def get_user_input(userInput):

       inputDataFrame = pd.DataFrame(userInput)

       return train_test_model(inputDataFrame)

def train_test_model(userInputDataFrame):

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

       #lets divide our data along a 80% to 20% border line
       #i.e 80% for training data and 20% for test data
       # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 20)

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
       # userInputDataFrame_min = userInputDataFrame.min()
       # userInputDataFrame_range = (userInputDataFrame - userInputDataFrame_min).max()
       # userInputDataFrame_scaled = (userInputDataFrame - userInputDataFrame_min)/userInputDataFrame_range

       # print(userInputDataFrame_scaled)

       #lets load our Support Vector Machine Model again and train our data with it furthermore
       svc_model = gg()
       #training our 80% normailised training dataset
       svc_model.fit(X_scaled, y)

       #lets predict with our training dataset
       y_predict = svc_model.predict(userInputDataFrame)

       if y_predict == 0:
              seed(1)
              percent = randint(0, 30)
              return percent
       seed(1)
       percentLow = randint(50, 99)
       return percentLow


# def get_result_accuracy(y_predict):

#        #lets import confusion matrix
#        from sklearn.metrics import classification_report, confusion_matrix

#        cm = np.array(confusion_matrix(y_test, y_predict, labels=[1,0]))

#        print(classification_report(y_test, y_predict))






#lets vsualise how correct our training dataset was with the aid of the imported confusion matrix
