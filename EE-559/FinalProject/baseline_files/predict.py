import csv
import numpy as np
import sys
import pandas as pd

from sklearn import preprocessing as pp
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
from sklearn.linear_model import Perceptron
import pickle

import errno
import os
import warnings
warnings.filterwarnings("ignore")


def read_csv(list_path):
    lines = []
    with open(list_path, 'rb') as f:
        lines = pd.read_csv(list_path, header=0, encoding='unicode_escape')
    return lines


def write_csv(csv_path, data_list):
    outF = open(csv_path, "w")
    for x in data_list:
        x_str = str(x)
        outF.write(x_str)
        outF.write("\n")
    outF.close()


def convert_categorical(data_frame):
    convert_col_list = ['Date', 'Seasons', 'Holiday', 'Functioning Day']
    le = pp.LabelEncoder()

    for col_name in convert_col_list:
        le.fit(data_frame[col_name])
        converted = le.transform(data_frame[col_name])
        data_frame[col_name] = converted

    return data_frame


def data_split(data_frame, y_col_name):
    y_data = data_frame.pop(y_col_name)
    X_data = data_frame.to_numpy()
    return X_data, y_data


def linear_regression_predict(model, X):
    y_pred = model.predict(X)
    return y_pred


def logistic_regression_predict(model, X):
    y_pred = model.predict(X)
    return y_pred


def perceptron_predict(mode, X):
    y_pred = model.predict(X)
    return y_pred


if __name__ == "__main__":
    
    train_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    data_frame = read_csv(train_file_name)

    alias = train_file_name.split('/')[-1].split('_')[0]
    try:
        model_filename = "model_{}.pkl".format(alias)
        model = pickle.load(open(model_filename, 'rb')) 
    except:
        print("ERROR: You must provide model.pkl file in the current directory.")
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), model_filename)

    if 'BIKE' in train_file_name:
        data_frame = convert_categorical(data_frame)
        X_test = data_frame.to_numpy()
        y_pred = linear_regression_predict(model, X_test)

    elif 'NEWS' in train_file_name:
        X_test = data_frame.to_numpy()
        y_pred = linear_regression_predict(model, X_test)

    elif 'WINE' in train_file_name:
        X_test = data_frame.to_numpy()
        y_pred = perceptron_predict(model, X_test)
    
    # print(result_dict)
    write_csv(output_file_name, y_pred.tolist())
