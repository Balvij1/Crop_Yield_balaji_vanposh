# -*- coding: utf-8 -*-
"""CropYieldProduction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14uurLAjB1SrDJ2D6k1qKasvcaSB4tbXF
"""

import pandas as pd

data = pd.read_excel('crop_csv_file.xlsx')

data.info()

"""# HANDLING MISSING DATA"""

data = data.dropna()
data.info()

data.describe()

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

State_Name = le.fit_transform(data.State_Name)
District_Name = le.fit_transform(data.District_Name)
Crop_Year = le.fit_transform(data.Crop_Year)
crop = le.fit_transform(data.Crop)
Season = le.fit_transform(data.Season)
data['State_Name'] = State_Name
data['District_Name'] = District_Name
data['Crop_Year'] = Crop_Year
data['Crop'] = crop
data['Season']  = Season

data.describe()

"""# Train and test Split"""

from sklearn.model_selection import  train_test_split

X = data.iloc[:,:-1]
Y = data.iloc[:,-1]

X.info()

Y.describe()

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, random_state=100)

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import roc_auc_score , classification_report, mean_squared_error, r2_score
forest = RandomForestRegressor(n_estimators=1000, 
                               criterion='squared_error', 
                               random_state=1, 
                               n_jobs=-1)
forest.fit(X_train, Y_train)
y_train_pred = forest.predict(X_train)
y_test_pred = forest.predict(X_test)

print('SE train: %.3f, test: %.3f' % (
        mean_squared_error(Y_train, y_train_pred),
        mean_squared_error(Y_test, y_test_pred)))
print('R^2 train: %.3f, test: %.3f' % (
        r2_score(Y_train, y_train_pred),
        r2_score(Y_test, y_test_pred)))

"""coefficient of Determination"""

print(forest.score(X_test,Y_test))

"""Prediction Model"""

print(forest.predict(X_test))

print(X_test)

print(forest.predict([[2,64,1,4,41,37,40,46,7365.0]]))

import pickle
with open ('forest_pickle','wb')as f:
    pickle.dump(forest,f)