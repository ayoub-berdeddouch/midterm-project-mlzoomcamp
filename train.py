#!/usr/bin/env python
# coding: utf-8


import numpy as np
import pandas as pd


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, confusion_matrix,classification_report
from sklearn.metrics import mean_squared_error,r2_score, accuracy_score
from sklearn.feature_extraction import DictVectorizer

# fix random seed for reproducibility
seed = 7
np.random.seed(seed)
import warnings; 
warnings.simplefilter('ignore')


df = pd.read_csv("abalone.csv")

##From problem statement and feature discription, let's first compute the target varible of the problem Age and assign it to the dataset.
## `Age = 1.5 + Rings` in years

df['age'] = df['Rings'] + 1.5
df.drop('Rings', axis = 1, inplace = True)


# Notice the minimum value for height is zero. These rows will be excluded.
df[df['height'] == 0]
# Remove rows 1257 and 3996
df.drop(index=[1257,3996], inplace = True)


# from Correlation plot
# ** High coorelation between Length & Diameter
# ** High corelation between `shucked weight, viscera weight Vs Whole_weight & Shell weight vs Whole_weight`

columns_to_drop = ['diameter', 'shucked_weight', 'viscera_weight', 'shell_weight']

# Drop columns
df1 = df.drop(columns_to_drop, axis=1)

# by calculating the VIF

# We should Normalise Height
# By doing Square root transofrmation

df1['height'] = np.sqrt(df1['height'])

# So  for our training 
# Features :
##- Sex
##- Length
##- Height
##- Whole_weight

#Target :
##- Age.

df2= df1.copy()

# Create a matrix of features (x; independant variables) and a dependant variable vector (y)
X = df2.iloc[:, :-1]
y = df2.iloc[:, -1]

categorical= ["sex"]
numerical = ['length', 'height', 'whole_weight']
dicts = X[categorical + numerical].to_dict(orient='records')

dv = DictVectorizer(sparse=False)
X = dv.fit_transform(dicts)

# Split our data into train test, 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# Random Forest Regressor

# training the final model

print('training the final model')
regressor = RandomForestRegressor(n_estimators = 400)
regressor.fit(X, y)


y_pred = regressor.predict(X_test)


print("R^2 Score= {}\n".format(r2_score(y_test, y_pred))

print("RMSE = {}".format(mean_squared_error(y_test, y_pred, squared=False))


# Save the model
n_estimators = 400
output_file = f'model_n_estimators={n_estimators}.bin'

with open(output_file, 'wb') as f_out:
    pickle.dump((dv, regressor), f_out)

print(f'the model is saved to {output_file}')