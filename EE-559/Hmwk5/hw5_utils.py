import csv
import numpy as np

from numpy import sum, multiply, square, sqrt


def input_data(datafile_w, data_m, data_n, lable_col):
    """
       Input the dataset.
    :param datafile_w: the location of the data file.
    :param data_m: the number of rows.
    :param data_n: the number of columns.
    :param lable_col: the column for the labels.
    :return: feature matrix X, label vector y
    """
    InputData = np.zeros((data_m, data_n), dtype='float')
    with open(datafile_w, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            data = [float(datum) for datum in row]
            InputData[i] = data
    # print("InputData.shape", InputData.shape)

    Data_X = InputData[0:data_m, 0:lable_col-1]  # Feature matrix X
    Data_y = InputData[0:data_m, lable_col-1]    # Label vector y
    Data_y = Data_y.astype(np.int)
    # Data_y = np.expand_dims(Data_y, axis=1)
    print(datafile_w[0:-3] + "shape", Data_X.shape)
    print(datafile_w[0:-3] + "shape", Data_y.shape)

    return Data_X, Data_y


def get_accuracy(data_y, predict_y, log_word=None, to_return=False):
    """
       Gets error rates between predicted labels and real labels.
    :param data_y: The real target set.
    :param predict_y: The predicted target set.
    :param log_word: Whether to print.
    :param to_return: Whether to return.
    :return: The value of accuracy.
    """
    accuracy = np.zeros((data_y.shape[0], 1), dtype='int')
    accuracy[data_y == predict_y] = 1
    accuracy_value = np.average(accuracy)
    if to_return:
        return accuracy_value
    else:
        print("For {}, the classification accuracy is {:4.3f}.".format(log_word, accuracy_value))


