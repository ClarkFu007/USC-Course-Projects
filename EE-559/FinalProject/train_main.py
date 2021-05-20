import pickle
import sklearn

import numpy as np
import pandas as pd

from numpy import sum, fabs
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, normalize, MinMaxScaler
from sklearn.feature_selection import SelectKBest, RFE, SequentialFeatureSelector
from sklearn.feature_selection import f_regression, mutual_info_regression
from sklearn import linear_model
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor

from my_utils import read_csv, toNumpy


def linear_regression(X_train, y_train):
    """
       Baseline technique: linear regression.
    :param X_train: feature matrix of the training data.
    :param y_train: target values of the training data.
    :return: the trained model.
    """
    regr_model = linear_model.LinearRegression()
    regr_model.fit(X_train, y_train)
    return regr_model


def lasso_regression(X_train, y_train):
    """
       Uses the Lasso technique to do regression and chooses the optimal model
    with validation data.
    :param X_train: feature matrix of the training data.
    :param y_train: target values of the training data.
    :return: the trained model.
    """
    tr_X, vali_X, tr_y, vali_y = train_test_split(X_train, y_train, test_size=0.3, random_state=0)
    vali_num = vali_y.shape[0]
    alpha_value, target_alpha = 0.1, 0.1
    lowest_MAE = 10000

    while alpha_value <= 2:
        regr_model = linear_model.Lasso(alpha=alpha_value, max_iter=1000)
        regr_model.fit(tr_X, tr_y)
        vali_y_pred = regr_model.predict(vali_X)
        curr_MAE = sum(fabs(vali_y_pred - vali_y)) / vali_num
        curr_MAE = round(curr_MAE, 4)
        if curr_MAE < lowest_MAE:
            target_alpha = alpha_value
            lowest_MAE = curr_MAE

        alpha_value = round(alpha_value + 0.05, 2)

    print("The optimal alpha value for Lasso regression is {}.".format(target_alpha))
    regr_model = linear_model.Lasso(alpha=target_alpha, max_iter=1000)
    regr_model.fit(X_train, y_train)
    return regr_model


def logistic_regression(X_train, y_train):
    """
       Uses the Logistic regression technique to do regression and chooses the optimal model
    with validation data.
    :param X_train: feature matrix of the training data.
    :param y_train: target values of the training data.
    :return: the trained model.
    """
    tr_X, vali_X, tr_y, vali_y = train_test_split(X_train, y_train, test_size=0.3, random_state=0)
    print(tr_X.shape[0])
    print(vali_X.shape[0])
    vali_num = vali_y.shape[0]
    c_value, target_c = 0.1, 0
    lowest_MAE = 10000

    while c_value <= 1.6:
        regr_model = linear_model.LogisticRegression(C=c_value, max_iter=100)
        regr_model.fit(tr_X, tr_y)
        vali_y_pred = regr_model.predict(vali_X)
        curr_MAE = sum(fabs(vali_y_pred - vali_y)) / vali_num
        curr_MAE = round(curr_MAE, 4)
        if curr_MAE < lowest_MAE:
            target_c = c_value
            lowest_MAE = curr_MAE
        c_value = round(c_value + 0.1, 1)

    print("The optimal C value for Logistic regression is {}.".format(target_c))
    regr_model = linear_model.LogisticRegression(C=target_c, max_iter=300)
    regr_model.fit(X_train, y_train)

    return regr_model


def extra_forest_regression(X_train, y_train):
    """
       Uses the extra-trees forest technique to do regression and chooses the optimal model
    with validation data.
    :param X_train: feature matrix of the training data.
    :param y_train: target values of the training data.
    :return: the trained model.
    """
    tr_X, vali_X, tr_y, vali_y = train_test_split(X_train, y_train, test_size=0.3, random_state=0)
    vali_num = vali_y.shape[0]
    n_value, target_n = 10, 0.01
    lowest_MAE = 10000
    while n_value <= 40:
        regr_model = ExtraTreesRegressor(n_estimators=n_value, max_depth=None)
        regr_model.fit(tr_X, tr_y)
        vali_y_pred = regr_model.predict(vali_X)
        curr_MAE = sum(fabs(vali_y_pred - vali_y)) / vali_num
        curr_MAE = round(curr_MAE, 4)
        if curr_MAE < lowest_MAE:
            target_n = n_value
            lowest_MAE = curr_MAE
        n_value += 1
        print("n_value", n_value)

    print("The optimal n value for Extra-Trees regression is {}.".format(target_n))
    regr_model = ExtraTreesRegressor(n_estimators=target_n, max_depth=None)
    regr_model.fit(X_train, y_train)

    return regr_model


def svm_regression(X_train, y_train):
    """
       Uses the support vector regression technique to do regression and chooses the optimal model
    with validation data.
    :param X_train: feature matrix of the training data.
    :param y_train: target values of the training data.
    :return: the trained model.
    """
    tr_X, vali_X, tr_y, vali_y = train_test_split(X_train, y_train, test_size=0.3, random_state=0)
    vali_num = vali_y.shape[0]
    c_value, target_c = 1.0, 0
    lowest_MAE = 10000
    while c_value <= 1.6:
        regr_model = SVR(C=c_value, epsilon=0.2)
        regr_model.fit(tr_X, tr_y)
        vali_y_pred = regr_model.predict(vali_X)
        curr_MAE = sum(fabs(vali_y_pred - vali_y)) / vali_num
        curr_MAE = round(curr_MAE, 4)
        if curr_MAE < lowest_MAE:
            target_c = c_value
            lowest_MAE = curr_MAE
        c_value = round(c_value + 0.01, 2)
        print("c_value", c_value)

    print("The optimal C value for SVM regression is {}.".format(target_c))
    regr_model = SVR(C=target_c, epsilon=0.1)
    regr_model.fit(X_train, y_train)

    return regr_model


def knn_regression(X_train, y_train):
    """
       Uses the k-neighbors regression technique to do regression and chooses the optimal model
    with validation data.
    :param X_train: feature matrix of the training data.
    :param y_train: target values of the training data.
    :return: the trained model.
    """
    tr_X, vali_X, tr_y, vali_y = train_test_split(X_train, y_train, test_size=0.3, random_state=0)
    vali_num = vali_y.shape[0]
    n_value, target_n = 1, 0
    lowest_MAE = 10000
    while n_value <= 15:
        regr_model = KNeighborsRegressor(n_neighbors=n_value)
        regr_model.fit(tr_X, tr_y)
        vali_y_pred = regr_model.predict(vali_X)
        curr_MAE = sum(fabs(vali_y_pred - vali_y)) / vali_num
        curr_MAE = round(curr_MAE, 4)
        if curr_MAE < lowest_MAE:
            target_n = n_value
            lowest_MAE = curr_MAE
        n_value += 1
        print("n_value", n_value)

    print("The optimal n value for KNN regression is {}.".format(target_n))
    regr_model = KNeighborsRegressor(n_neighbors=target_n)
    regr_model.fit(X_train, y_train)

    return regr_model


def save_model(filename,  model):
    """
       Saves the trained model.
    :param filename: name of the file.
    :param model: model to be saved.
    """
    pickle.dump(model, open(filename, 'wb'))
    print("A model has been saved as {}".format(filename))


def train_model(X_data, y_data, mode=None):
    """
       Trains all the models with my selected machine learning algorithms.
    :param X_data: feature matrix of the training data.
    :param y_data: target values of the training data.
    :param mode: the prefix to save models.
    """
    model = linear_regression(X_data, y_data)
    alias = "NEWS"
    filename = "model_{}.pkl".format(alias)
    # Write the pickled representation of "model" to the open file object file.
    pickle.dump(model, open(filename, 'wb'))
    print("A model has been saved as {}".format(filename))

    model = lasso_regression(X_data, y_data)
    save_model(filename=mode+"lasso_reg_model.pkl", model=model)

    model = logistic_regression(X_data, y_data)
    save_model(filename=mode + "logistic_reg_model.pkl", model=model)

    model = extra_forest_regression(X_data, y_data)
    save_model(filename=mode+"extra_forest_reg_model.pkl", model=model)

    model = svm_regression(X_data, y_data)
    save_model(filename=mode+"svm_reg_model.pkl", model=model)

    model = knn_regression(X_data, y_data)
    save_model(filename=mode+"knn_reg_model.pkl", model=model)


def main():
    print("My Sklearn version is {}".format(sklearn.__version__))
    print("My Pandas version is {}".format(pd.__version__))
    # Read the data from synthetic datasets.
    # train_data_file_name = sys.argv[1]
    # train_label_file_name = sys.argv[2]
    train_data_file_name = "NEWS_Training_data.csv"
    train_label_file_name = "NEWS_Training_label.csv"

    data_frame_X = read_csv(train_data_file_name)
    data_frame_y = read_csv(train_label_file_name)
    print(type(data_frame_X))
    print(type(data_frame_y))

    X_data, y_data = toNumpy(data_frame_X, data_frame_y)
    print("The feature matrix of the training data: ", X_data.shape)
    print("The label vector of the training data: ", y_data.shape)
    train_model(X_data=X_data, y_data=y_data)  # Train with original features.

    one_hot_cols = [11, 12, 13, 14, 15, 16, 29, 30, 31, 32, 33, 34, 35, 36]
    z_score_cols = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 18, 37, 42, 44, 45, 46, 47, 48, 49, 50, 54, 56, 57]
    normal_cols = [17, 19, 38, 39, 40, 41, 43, 51, 52, 53, 55]
    min_max_cols = [20, 21, 22, 23, 24, 25, 26, 27, 28]
    prepro_X_data = np.zeros((X_data.shape[0], X_data.shape[1]), dtype='float')
    prepro_X_data[one_hot_cols] = X_data[one_hot_cols]
    # Standardize the training data
    z_score_scaler = StandardScaler()
    z_score_scaler.fit(X_data[z_score_cols])
    prepro_X_data[z_score_cols] = z_score_scaler.transform(X_data[z_score_cols])
    pickle.dump(z_score_scaler, open('z_score_scaler.pkl', 'wb'))
    # Normalize the training data
    prepro_X_data[normal_cols] = normalize(X_data[normal_cols], norm='l2', axis=0)
    # MinMax scale the training data
    minmax_scaler = MinMaxScaler()
    minmax_scaler.fit(X_data[min_max_cols])
    prepro_X_data[min_max_cols] = minmax_scaler.transform(X_data[min_max_cols])
    pickle.dump(minmax_scaler, open('minmax_scaler.pkl', 'wb'))
    train_model(X_data=prepro_X_data, y_data=y_data)  # Train with preprocessed data.

    #  Do feature selection
    # Univariate Feature Selection (UFS)
    ufs_f_X_data = SelectKBest(f_regression, k=50).fit_transform(prepro_X_data, y_data)
    print("ufs_f_X_data.shape", ufs_f_X_data.shape)
    train_model(X_data=ufs_f_X_data, y_data=y_data, mode='ufs_f')  # f_regression

    ufs_mu_X_data = SelectKBest(mutual_info_regression, k=50).fit_transform(prepro_X_data, y_data)
    print("ufs_mu_X_data.shape", ufs_mu_X_data.shape)
    train_model(X_data=ufs_mu_X_data, y_data=y_data, mode='ufs_mu')  # mutual_info_regression

    estimator = linear_model.LinearRegression()
    # Recursive feature elimination
    rfe_selector = RFE(estimator, n_features_to_select=50, step=1)
    rfe_selector.fit(prepro_X_data, y_data)
    rfe_X_data = rfe_selector.transform(prepro_X_data)
    pickle.dump(rfe_selector, open('rfe_selector.pkl', 'wb'))
    print("rfe_X_data.shape", rfe_X_data.shape)
    train_model(X_data=rfe_X_data, y_data=y_data, mode='rfe')

    # Sequential Feature Selection (SFS)
    sfs = SequentialFeatureSelector(estimator, n_features_to_select=50, direction='backward')
    sfs.fit(prepro_X_data, y_data)
    sfs_X_data = sfs.transform(prepro_X_data)
    print("sfs_X_data.shape", sfs_X_data.shape)
    train_model(X_data=sfs_X_data, y_data=y_data, mode='sfs')


if __name__ == '__main__':
    main()







