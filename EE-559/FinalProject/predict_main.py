import errno
import os
import pickle

import numpy as np

from sklearn.preprocessing import StandardScaler, normalize, MinMaxScaler
from sklearn.feature_selection import SelectKBest, RFE, SequentialFeatureSelector
from sklearn.feature_selection import f_regression, mutual_info_regression
from sklearn import linear_model
from numpy import sum, square, fabs

from my_utils import read_csv, toNumpy


def model_predict(model, X):
    """
       Uses the trained model to predict values given the data.
    :param model: trained model.
    :param X: feature matrix.
    :return: predicted values.
    """
    y_pred = model.predict(X)
    return y_pred


def measure_performance(y_pred, y_test, mode='testing'):
    """
       Get the values of performance measures.
    :param y_pred: predicted target values of the data.
    :param y_test: real target values of the data.
    :param mode: statement for printing.
    """
    total_num = y_pred.shape[0]
    r_value = 10
    r_vector = np.repeat(r_value, total_num)

    mean_AE = sum(fabs(y_pred - y_test)) / total_num
    print("The mean absolute error (MAE) for " + mode + " is %.4f." % mean_AE)

    y_mean = np.mean(y_test)
    y_mean = np.repeat(y_mean, total_num)
    coef_R_square = 1 - sum(square(y_test - y_pred)) / sum(square(y_test - y_mean))
    print("The coefficient of determination (R-square) for " + mode + " is %.4f." % coef_R_square)

    p_mean_SE = sum(square((y_test - y_pred) / (r_vector + y_test))) / total_num
    print("The PMSE for " + mode + " is %.4f." % p_mean_SE)

    p_mean_AE = sum(fabs((y_test - y_pred) / (r_vector + y_test))) / total_num
    print("The PMAE for " + mode + " is %.4f." % p_mean_AE)

    m_R_square = 1 - p_mean_SE / (sum(square((y_test - y_mean) / (r_vector + y_test))) / total_num)
    print("The modified R-square for " + mode + " is %.4f." % m_R_square)
    print(" ")


def measure_model(lasso_reg_model=None, logistic_reg_model=None, extra_forest_reg_model=None,
                  svm_reg_model=None, knn_reg_model=None, X_test=None, y_test=None):
    """
       Gets the performance of my chosen machine learning algorithms.
    :param lasso_reg_model: lasso regression.
    :param logistic_reg_model: logistic regression.
    :param extra_forest_reg_model: extra-trees forest regression.
    :param svm_reg_model: support vector regression.
    :param knn_reg_model: k-neighbors regression.
    :param X_test: feature matrix of the test data.
    :param y_test: target values of the test data.
    """
    lasso_y_pred = model_predict(lasso_reg_model, X_test)
    measure_performance(y_pred=lasso_y_pred, y_test=y_test, mode="lasso")

    logistic_y_pred = model_predict(logistic_reg_model, X_test)
    measure_performance(y_pred=logistic_y_pred, y_test=y_test, mode="logistic")

    ef_y_pred = model_predict(extra_forest_reg_model, X_test)
    measure_performance(y_pred=ef_y_pred, y_test=y_test, mode="extra forest")

    svr_y_pred = model_predict(svm_reg_model, X_test)
    measure_performance(y_pred=svr_y_pred, y_test=y_test, mode="svm regression")

    knn_y_pred = model_predict(knn_reg_model, X_test)
    measure_performance(y_pred=knn_y_pred, y_test=y_test, mode="knn regression")


def write_csv(csv_path, data_list):
    """
       Saves the file.
    :param csv_path: pathname to save.
    :param data_list: data to be saved.
    """
    outF = open(csv_path, "w")
    for x in data_list:
        x_str = str(x)
        outF.write(x_str)
        outF.write("\n")
    outF.close()


def main():
    # train_file_name = sys.argv[1]
    # output_file_name = sys.argv[2]
    train_data_file_name = "NEWS_Training_data.csv"
    train_label_file_name = "NEWS_Training_label.csv"
    test_data_file_name = "NEWS_Test_data.csv"
    test_label_file_name = "NEWS_Test_label.csv"

    tr_data_frame_X = read_csv(train_data_file_name)
    tr_data_frame_y = read_csv(train_label_file_name)
    te_data_frame_X = read_csv(test_data_file_name)
    te_data_frame_y = read_csv(test_label_file_name)
    alias = test_data_file_name.split('/')[-1].split('_')[0]
    model_filename = "model_{}.pkl".format(alias)
    try:
        linear_reg_model = pickle.load(open(model_filename, 'rb'))
        mode = "rfe"  # prefix to open the models
        lasso_reg_model = pickle.load(open(mode + "lasso_reg_model.pkl", 'rb'))
        logistic_reg_model = pickle.load(open(mode + "logistic_reg_model.pkl", 'rb'))
        # logistic_reg_model = pickle.load(open("model_NEWS.pkl", 'rb'))
        extra_forest_reg_model = pickle.load(open(mode + "extra_forest_reg_model.pkl", 'rb'))
        svm_reg_model = pickle.load(open(mode + "svm_reg_model.pkl", 'rb'))
        knn_reg_model = pickle.load(open(mode + "knn_reg_model.pkl", 'rb'))

    except:
        print("ERROR: You must provide model.pkl file in the current directory.")
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), model_filename)

    X_train, y_train = toNumpy(tr_data_frame_X, tr_data_frame_y)
    X_test, y_test = toNumpy(te_data_frame_X, te_data_frame_y)
    print(X_test.shape[0])
    trivial_y_pred = np.repeat(np.mean(y_train), y_test.shape[0])
    baseline_y_pred = model_predict(linear_reg_model, X_test)
    measure_performance(y_pred=trivial_y_pred, y_test=y_test, mode="trivial testing")
    measure_performance(y_pred=baseline_y_pred, y_test=y_test, mode="baseline testing")
    measure_model(lasso_reg_model, logistic_reg_model, extra_forest_reg_model,
                  svm_reg_model, knn_reg_model, X_test=X_test, y_test=y_test)

    one_hot_cols = [11, 12, 13, 14, 15, 16, 29, 30, 31, 32, 33, 34, 35, 36]
    z_score_cols = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 18, 37, 42, 44, 45, 46, 47, 48, 49, 50, 54, 56, 57]
    normal_cols = [17, 19, 38, 39, 40, 41, 43, 51, 52, 53, 55]
    min_max_cols = [20, 21, 22, 23, 24, 25, 26, 27, 28]
    prepro_tr_X_data = np.zeros((X_train.shape[0], X_train.shape[1]), dtype='float')
    prepro_te_X_data = np.zeros((X_test.shape[0], X_test.shape[1]), dtype='float')
    prepro_tr_X_data[one_hot_cols] = X_train[one_hot_cols]
    prepro_te_X_data[one_hot_cols] = X_test[one_hot_cols]
    # Standardize the test data
    z_score_scaler = StandardScaler()
    z_score_scaler.fit(X_train[z_score_cols])
    prepro_tr_X_data[z_score_cols] = z_score_scaler.transform(X_train[z_score_cols])
    prepro_te_X_data[z_score_cols] = z_score_scaler.transform(X_test[z_score_cols])
    # Normalize the test data
    prepro_tr_X_data[normal_cols] = normalize(X_train[normal_cols], norm='l2', axis=0)
    prepro_te_X_data[normal_cols] = normalize(X_test[normal_cols], norm='l2', axis=0)
    # MinMax scale the test data
    minmax_scaler = MinMaxScaler()
    minmax_scaler.fit(X_train[min_max_cols])
    prepro_tr_X_data[min_max_cols] = minmax_scaler.transform(X_train[min_max_cols])
    prepro_te_X_data[min_max_cols] = minmax_scaler.transform(X_test[min_max_cols])

    measure_model(lasso_reg_model, logistic_reg_model, extra_forest_reg_model,
                  svm_reg_model, knn_reg_model, X_test=prepro_te_X_data, y_test=y_test)

    # Do feature selection (UFS)
    # Univariate Feature Selection
    usf_f = SelectKBest(f_regression, k=50)
    usf_f.fit(prepro_tr_X_data, y_train)
    ufs_f_te_X_data = usf_f.transform(prepro_te_X_data)
    measure_model(lasso_reg_model, logistic_reg_model, extra_forest_reg_model,
                  svm_reg_model, knn_reg_model, X_test=ufs_f_te_X_data, y_test=y_test)

    usf_mu = SelectKBest(mutual_info_regression, k=50)
    usf_mu.fit(prepro_tr_X_data, y_train)
    ufs_mu_te_X_data = usf_mu.transform(prepro_te_X_data)
    measure_model(lasso_reg_model, logistic_reg_model, extra_forest_reg_model,
                  svm_reg_model, knn_reg_model, X_test=ufs_mu_te_X_data, y_test=y_test)

    estimator = linear_model.LinearRegression()
    # Recursive feature elimination
    rfe_selector = RFE(estimator, n_features_to_select=50, step=1)
    rfe_selector.fit(prepro_tr_X_data, y_train)
    rfe_X_data = rfe_selector.transform(prepro_te_X_data)
    measure_model(lasso_reg_model, logistic_reg_model, extra_forest_reg_model,
                  svm_reg_model, knn_reg_model, X_test=rfe_X_data, y_test=y_test)

    # Sequential Feature Selection (SFS)
    sfs = SequentialFeatureSelector(estimator, n_features_to_select=50, direction='backward')
    sfs.fit(prepro_tr_X_data, y_train)
    sfs_X_data = sfs.transform(prepro_te_X_data)
    measure_model(lasso_reg_model, logistic_reg_model, extra_forest_reg_model,
                  svm_reg_model, knn_reg_model, X_test=sfs_X_data, y_test=y_test)


if __name__ == '__main__':
    main()

