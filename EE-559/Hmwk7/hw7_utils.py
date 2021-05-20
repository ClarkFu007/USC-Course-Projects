import csv
import numpy as np

from numpy import sum,  square, average, std
from sklearn.model_selection import train_test_split
from RBFN_model import RBNF


def input_data(datafile_w, data_m, data_n, label_col):
    """
        Inputs the dataset.
    :param datafile_w: the location of the data file.
    :param data_m: the number of rows.
    :param data_n: the number of columns.
    :param label_col: the column for the labels.
    :return: feature matrix X, label vector y
    """

    InputData = np.zeros((data_m, data_n), dtype='float')
    with open(datafile_w, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            data = [float(datum) for datum in row]
            InputData[i] = data

    Data_X = InputData[0:data_m, 0:label_col-1]  # Feature matrix X
    Data_y = InputData[0:data_m, label_col-1]    # Label vector y
    print(datafile_w[0:-3] + "shape", Data_X.shape)
    print(datafile_w[0:-3] + "shape", Data_y.shape)

    return Data_X, Data_y


def get_MSE(y_pred, y_test, mode='testing', verbose=True):
    """
       Gets the mean squared error.
    :param y_pred: predicted values.
    :param y_test: real values.
    :param mode: for print statements.
    :param verbose: print the statement if true, return mse value otherwise.
    :return:
    """
    total_num = y_pred.shape[0]
    mean_SE = sum(square(y_pred - y_test)) / total_num
    if verbose:
        print("The mean absolute error (MSE) for " + mode + " is %.4f." % mean_SE)
        print(" ")
    else:
        return mean_SE


def get_results(experiment_num, train_X, train_y, test_X, test_y, select_method):
    """
       Gets cross-validation accuracy matrix with different hyper-parameters.
    :param experiment_num: number of experiment.
    :param train_X: feature matrix for training data.
    :param train_y: label vector for training data.
    :param test_X: feature matrix for test data.
    :param test_y: label vector for test data.
    :param select_method: 'all select', 'random select' or 'k-means clustering'.
    """
    scale_list = [0.25, 0.5, 1, 2.0, 4.0]
    if select_method == 'all select':  # For the part (c)
        do_all_choose_part(experiment_num=experiment_num, scale_list=scale_list,
                           train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y,
                           select_method=select_method)

    elif select_method == 'random select':  # For the part (d)
        do_random_choose_part(experiment_num=experiment_num, scale_list=scale_list,
                              train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y,
                              select_method=select_method)
    elif select_method == 'k-means clustering':  # For the part (e)
        do_k_clustering_part(experiment_num=experiment_num, scale_list=scale_list,
                             train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y,
                             select_method=select_method)
    else:
        print("Please select the correct method!")


def do_all_choose_part(experiment_num, scale_list, train_X, train_y, test_X, test_y, select_method):
    """
       Implements the experiment when choosing all the data points as centers.
    :param experiment_num: number of experiment.
    :param scale_list: [0.25, 0.5, 1, 2.0, 4.0].
    :param train_X: feature matrix for training data.
    :param train_y: label vector for training data.
    :param test_X: feature matrix for test data.
    :param test_y: label vector for test data.
    :param select_method: 'all select', 'random select' or 'k-means clustering'.
    """
    cross_vali_mse = []
    lowest_vali_mse = 100
    target_scale = 0.25
    for experiment_i in range(experiment_num):
        tr_X, vali_X, tr_y, vali_y = train_test_split(train_X, train_y, test_size=0.3, random_state=experiment_i)

        my_rbnf_model = RBNF(select_method=select_method)
        curr_vali_mse = np.zeros((len(scale_list)), dtype='float')
        for scale_i in range(len(scale_list)):
            my_rbnf_model.fit(X=tr_X, y=tr_y, scale_factor=scale_list[scale_i])
            y_pred = my_rbnf_model.predict(X=vali_X)
            curr_vali_mse[scale_i] = get_MSE(y_pred=y_pred, y_test=vali_y, verbose=False)

        curr_best_mse = np.min(curr_vali_mse)
        cross_vali_mse.append(curr_best_mse)
        if lowest_vali_mse > curr_best_mse:
            lowest_vali_mse = curr_best_mse
            target_scale = scale_list[np.argmin(curr_vali_mse)]

    my_rbnf_model = RBNF(select_method=select_method)
    get_final_performance(my_model=my_rbnf_model, train_X=train_X, train_y=train_y,
                          test_X=test_X, test_y=test_y, cross_vali_mse=cross_vali_mse,
                          target_scale=target_scale, select_method=select_method)


def do_random_choose_part(experiment_num, scale_list, train_X, train_y, test_X, test_y, select_method):
    """
       Implements the experiment when randomly choosing centers.
    :param experiment_num: number of experiment.
    :param scale_list: [0.25, 0.5, 1, 2.0, 4.0].
    :param train_X: feature matrix for training data.
    :param train_y: label vector for training data.
    :param test_X: feature matrix for test data.
    :param test_y: label vector for test data.
    :param select_method: 'all select', 'random select' or 'k-means clustering'.
    """
    cross_vali_mse = []
    lowest_vali_mse = 100
    target_v = 0.01
    target_scale = None
    for experiment_i in range(experiment_num):
        tr_X, vali_X, tr_y, vali_y = train_test_split(train_X, train_y, test_size=0.3, random_state=experiment_i)
        v_value = 0.01
        while v_value <= 0.5:
            my_rbnf_model = RBNF(v_value=v_value, select_method=select_method)
            curr_vali_mse = np.zeros((len(scale_list)), dtype='float')
            for scale_i in range(len(scale_list)):
                my_rbnf_model.fit(X=tr_X, y=tr_y, scale_factor=scale_list[scale_i])
                y_pred = my_rbnf_model.predict(X=vali_X)
                curr_vali_mse[scale_i] = get_MSE(y_pred=y_pred, y_test=vali_y, verbose=False)

            curr_best_mse = np.min(curr_vali_mse)
            cross_vali_mse.append(curr_best_mse)
            if lowest_vali_mse > curr_best_mse:
                lowest_vali_mse = curr_best_mse
                target_v = v_value
                target_scale = scale_list[np.argmin(curr_vali_mse)]

            v_value = round(v_value + 0.01, 2)

    my_rbnf_model = RBNF(v_value=target_v, select_method=select_method)
    get_final_performance(my_model=my_rbnf_model, train_X=train_X, train_y=train_y,
                          test_X=test_X, test_y=test_y, cross_vali_mse=cross_vali_mse,
                          target_scale=target_scale, select_method=select_method, target_v=target_v)


def do_k_clustering_part(experiment_num, scale_list, train_X, train_y, test_X, test_y, select_method):
    """
       Implements the experiment when using k-means clustering to choose centers.
    :param experiment_num: number of experiment.
    :param scale_list: [0.25, 0.5, 1, 2.0, 4.0].
    :param train_X: feature matrix for training data.
    :param train_y: label vector for training data.
    :param test_X: feature matrix for test data.
    :param test_y: label vector for test data.
    :param select_method: 'all select', 'random select' or 'k-means clustering'.
    """
    cross_vali_mse = []
    lowest_vali_mse = 1e7
    target_k = 20
    target_scale = None
    for experiment_i in range(experiment_num):
        tr_X, vali_X, tr_y, vali_y = train_test_split(train_X, train_y, test_size=0.3, random_state=experiment_i)
        target_scale = 0.25
        for k_value in range(20, 91):
            my_rbnf_model = RBNF(k_value=k_value, select_method=select_method)
            curr_vali_mse = np.zeros((len(scale_list)), dtype='float')
            for scale_i in range(len(scale_list)):
                my_rbnf_model.fit(X=tr_X, y=tr_y, scale_factor=scale_list[scale_i])
                y_pred = my_rbnf_model.predict(X=vali_X)
                curr_vali_mse[scale_i] = get_MSE(y_pred=y_pred, y_test=vali_y, verbose=False)

            curr_best_mse = np.min(curr_vali_mse)
            cross_vali_mse.append(curr_best_mse)
            if lowest_vali_mse > curr_best_mse:
                lowest_vali_mse = curr_best_mse
                target_k = k_value
                target_scale = scale_list[np.argmin(curr_vali_mse)]

    my_rbnf_model = RBNF(k_value=target_k, select_method=select_method)
    get_final_performance(my_model=my_rbnf_model, train_X=train_X, train_y=train_y,
                          test_X=test_X, test_y=test_y, cross_vali_mse=cross_vali_mse,
                          target_scale=target_scale, select_method=select_method, target_k=target_k)


def get_final_performance(my_model, train_X, train_y, test_X, test_y,
                          cross_vali_mse, target_scale, select_method,
                          target_v=None, target_k=None):
    """
       Gets the final performance of the trained model in three techniques.
    :param my_model: trained model.
    :param train_X: feature matrix for training data.
    :param train_y: label vector for training data.
    :param test_X: feature matrix for test data.
    :param test_y: label vector for test data.
    :param cross_vali_mse: array to store a series of mean squared errors.
    :param target_scale: optimum value to scale gamma.
    :param select_method: 'all select', 'random select' or 'k-means clustering'.
    :param target_v: optimum v value.
    :param target_k: optimum k value.
    :return:
    """
    my_model.fit(X=train_X, y=train_y, scale_factor=target_scale)
    y_pred = my_model.predict(X=test_X)
    cross_vali_mse_arr = np.array(cross_vali_mse)
    print("When using " + select_method + ",")
    print("The mean and std of cross validation MSE are {:4.4f} and {:4.4f}".
          format(average(cross_vali_mse_arr), std(cross_vali_mse_arr)))
    if select_method == 'all select':
        print("The optimum scale value is {:4.2f}.".format(target_scale))
    elif select_method == 'random select':
        print("The optimum v, scale value, and M are {:4.2f} , {:4.2f} and {}.".
              format(target_v, target_scale, my_model.m_value))
    elif select_method == 'k-means clustering':
        print("The optimum k and scale value are {} and {:4.2f}.".
              format(target_k, target_scale))
    else:
        print("Please select the correct method!")

    get_MSE(y_pred=y_pred, y_test=test_y, mode='test for ' + select_method)

