
import csv
import numpy as np
import sys
import pandas as pd

from sklearn import preprocessing as pp
from sklearn import datasets, linear_model
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import pickle

def read_csv(list_path):
    lines = []
    with open(list_path, 'rb') as f:
        lines = pd.read_csv(list_path, header= 0, encoding= 'unicode_escape')
    return lines

def convert_categorical(data_frame):
    convert_col_list = ['Date', 'Seasons', 'Holiday', 'Functioning Day']
    le = pp.LabelEncoder()

    for col_name in convert_col_list:
        le.fit(data_frame[col_name])
        converted = le.transform(data_frame[col_name])
        data_frame[col_name] = converted

    return data_frame

def linear_regression(X_train, y_train):
    regr_model = linear_model.LinearRegression()
    regr_model.fit(X_train, y_train)
    return regr_model

def perceptron_normalized(X_train, y_train):
    regr_model = Pipeline([('scaler', StandardScaler()),
                           ('clf', Perceptron())])
    regr_model.fit(X_train, y_train)
    return regr_model

def toNumpy(data_frame_X, data_frame_y):
    X_data = data_frame_X.to_numpy()
    y_data = data_frame_y.to_numpy().ravel()
    return X_data, y_data

if __name__ == "__main__":
    
    train_data_file_name = sys.argv[1]
    train_label_file_name = sys.argv[2]
    data_frame_X = read_csv(train_data_file_name)
    data_frame_y = read_csv(train_label_file_name)

    if 'BIKE' in train_data_file_name:
        data_frame_X = convert_categorical(data_frame_X)
        X_data, y_data = toNumpy(data_frame_X, data_frame_y)
        model = linear_regression(X_data, y_data)
        alias = "BIKE"
    
    elif 'NEWS' in train_data_file_name:
        X_data, y_data = toNumpy(data_frame_X, data_frame_y)
        model = linear_regression(X_data, y_data)
        alias = "NEWS"
    
    elif 'WINE' in train_data_file_name:
        X_data, y_data = toNumpy(data_frame_X, data_frame_y)
        model = perceptron_normalized(X_data, y_data)
        alias = "WINE"
  
    filename = "model_{}.pkl".format(alias)
    pickle.dump(model, open(filename, 'wb'))
    print("A model has been saved as {}".format(filename))

    

