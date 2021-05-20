import csv
import numpy as np
import sys
import pandas as pd

from sklearn import preprocessing as pp
from sklearn.preprocessing import normalize
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
from sklearn.linear_model import Perceptron
import pickle

import errno
import os
import warnings
warnings.filterwarnings("ignore")


def read_csv(list_path):
    """
       Reads the data from csv files.
    :param list_path: the file path.
    :return: the Pandas dataframe type.
    """
    lines = []
    with open(list_path, 'rb') as f:
        lines = pd.read_csv(list_path, header= 0, encoding= 'unicode_escape')
    return lines


def write_csv(csv_path, data_list):
    """
       Converts the Pandas dataframe type to Numpy array type.
    :param csv_path: file path.
    :param data_list: data list.
    """
    outF = open(csv_path, "w")
    for x in data_list:
        x_str = str(x)
        outF.write(x_str)
        outF.write("\n")
    outF.close()


def convert_categorical(data_frame):
    """
       Converts categorical features.
    :param data_frame: data frame.
    :return: data frame.
    """
    convert_col_list = ['Date', 'Seasons', 'Holiday', 'Functioning Day']
    le = pp.LabelEncoder()

    for col_name in convert_col_list:
        le.fit(data_frame[col_name])
        converted = le.transform(data_frame[col_name])
        data_frame[col_name] = converted

    return data_frame


def data_split(data_frame, y_col_name):
    """
       Gets feature matrix and target vector.
    :param data_frame: data frame.
    :param y_col_name: target column
    :return: feature matrix and target vector.
    """
    y_data = data_frame.pop(y_col_name)
    X_data = data_frame.to_numpy()
    return X_data, y_data


def linear_regression_predict(model, X):
    """
       Predicts the values.
    :param model: trained model.
    :param X: feature matrix.
    :return: predicted values.
    """
    y_pred = model.predict(X)
    return y_pred


def logistic_regression_predict(model, X):
    """
       Predicts the values.
    :param model: trained model.
    :param X: feature matrix.
    :return: predicted values.
    """
    y_pred = model.predict(X)
    return y_pred


def perceptron_predict(model, X):
    """
       Predicts the values.
    :param model: trained model.
    :param X: feature matrix.
    :return: predicted values.
    """
    y_pred = model.predict(X)
    return y_pred


if __name__ == "__main__":
    test_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    te_data_frame = read_csv(test_file_name)

    alias = test_file_name.split('/')[-1].split('_')[0]
    try:
        model_filename = "model_{}.pkl".format(alias)
        model = pickle.load(open(model_filename, 'rb')) 
    except:
        print("ERROR: You must provide model.pkl file in the current directory.")
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), model_filename)

    if 'BIKE' in test_file_name:
        data_frame = convert_categorical(te_data_frame)
        X_test = data_frame.to_numpy()
        y_pred = linear_regression_predict(model, X_test)

    elif 'NEWS' in test_file_name:
        X_test = te_data_frame.to_numpy()

        one_hot_cols = [11, 12, 13, 14, 15, 16, 29, 30, 31, 32, 33, 34, 35, 36]
        z_score_cols = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 18, 37, 42, 44, 45, 46, 47, 48, 49, 50, 54, 56, 57]
        normal_cols = [17, 19, 38, 39, 40, 41, 43, 51, 52, 53, 55]
        min_max_cols = [20, 21, 22, 23, 24, 25, 26, 27, 28]
        prepro_te_X_data = np.zeros((X_test.shape[0], X_test.shape[1]), dtype='float')
        # One-hot encoding
        prepro_te_X_data[one_hot_cols] = X_test[one_hot_cols]
        # Standardize the test data
        z_score_scaler = pickle.load(open('z_score_scaler.pkl', 'rb'))
        prepro_te_X_data[z_score_cols] = z_score_scaler.transform(X_test[z_score_cols])
        # Normalize the test data
        prepro_te_X_data[normal_cols] = normalize(X_test[normal_cols], norm='l2', axis=0)
        # MinMax scale the test data
        minmax_scaler = pickle.load(open('minmax_scaler.pkl', 'rb'))
        prepro_te_X_data[min_max_cols] = minmax_scaler.transform(X_test[min_max_cols])

        # Recursive feature elimination
        rfe_selector = pickle.load(open('rfe_selector.pkl', 'rb'))
        rfe_X_data = rfe_selector.transform(prepro_te_X_data)

        y_pred = linear_regression_predict(model, rfe_X_data)

    elif 'WINE' in test_file_name:
        X_test = te_data_frame.to_numpy()
        y_pred = perceptron_predict(model, X_test)
    
    # print(result_dict)
    write_csv(output_file_name, y_pred.tolist())
