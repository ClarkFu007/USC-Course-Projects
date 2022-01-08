import pickle

import numpy as np

from sklearn.linear_model import Perceptron
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import KFold
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from utils import save_model


def get_final_performance(model, name, train_X, train_y, test_X, test_y):
    """
       Gets the final performance of trained model.
    :param model: trained model
    :param name: name of the classifier
    :param train_X: feature matrix for training
    :param train_y: label vector for training
    :param test_X: feature matrix for test
    :param test_y: label vector for test
    """
    print("For the " + name + " classifier, "
          "the classification accuracy is {:.4f} on training data."
          .format(model.score(X=train_X, y=train_y)))
    print("For the " + name + " classifier, "
          "the classification accuracy is {:.4f} on test data."
          .format(model.score(X=test_X, y=test_y)))


def do_cr_val_training(values, fold_num, name, k_fold_tr_X, k_fold_tr_y, k_fold_te_X, k_fold_te_y):
    """
       Implements the cross-validation experiments to get the cross-validation matrix.
    :param values: a set of values
    :param fold_num: number of folds
    :param name: name of the classifier
    :param k_fold_tr_X: k folds for training features
    :param k_fold_tr_y: k folds for training labels
    :param k_fold_te_X: k folds for test features
    :param k_fold_te_y: k folds for test labels
    :return: cross-validation matrix
    """
    num = values.shape[0]
    cross_vali_acc = np.zeros((fold_num, num), dtype='float')
    for fold_i in range(fold_num):
        for value_i in range(num):
            if name == "support vector machine":
                model = SVC(C=values[value_i], kernel='rbf', random_state=660)
            elif name == "logistic regression":
                model = LogisticRegression(C=values[value_i], solver='newton-cg', random_state=660)
            elif name == "decision tree":
                model = DecisionTreeClassifier(max_depth=values[value_i], random_state=660)
            elif name == "random forest":
                model = RandomForestClassifier(n_estimators=values[value_i], max_depth=3,
                                               random_state=660)
            elif name == "AdaBoost":
                model = AdaBoostClassifier(n_estimators=values[value_i], random_state=660)
            model.fit(X=k_fold_tr_X[fold_i], y=k_fold_tr_y[fold_i])
            cross_vali_acc[fold_i, value_i] = model.score(X=k_fold_te_X[fold_i], y=k_fold_te_y[fold_i])
    return cross_vali_acc


def get_cr_val_performance(cross_vali_acc, values, name,
                           train_X, train_y, test_X, test_y, label_name):
    """
       Gets the cross-validation performance of trained model.
    :param cross_vali_acc: cross-validation accuracy matrix
    :param values: a set of candidate values
    :param name: name of the classifier
    :param train_X: feature matrix for training
    :param train_y: label vector for training
    :param test_X: feature matrix for test
    :param test_y: label vector for test
    :param label_name: label name to save models
    """
    mean_vali_acc = np.average(cross_vali_acc, axis=0)
    std_vali_acc = np.std(cross_vali_acc, axis=0)
    target_index = np.argmax(mean_vali_acc)
    target_value = values[target_index]
    print("For the " + name + " classifier, "
          "the mean classification accuracy is {} for cross-validation."
          .format(mean_vali_acc))
    print("For the " + name + " classifier, "
          "the standard deviation of classification accuracy is {} for cross-validation."
          .format(std_vali_acc))

    print("For the " + name + " classifier, "
          "the best value is {} after cross-validation."
          .format(target_value))
    if name == "support vector machine":
        final_model = SVC(C=target_value, kernel='rbf', random_state=660)
    elif name == "logistic regression":
        final_model = LogisticRegression(C=target_value, solver='newton-cg', random_state=660)
    elif name == "decision tree":
        final_model = DecisionTreeClassifier(max_depth=target_value, random_state=660)
    elif name == "random forest":
        final_model = RandomForestClassifier(n_estimators=target_value,
                                             max_depth=3, random_state=660)
    elif name == "AdaBoost":
        final_model = AdaBoostClassifier(n_estimators=target_value, random_state=660)
    final_model.fit(X=train_X, y=train_y)
    save_model(filename=name+' '+label_name, model=final_model)
    get_final_performance(model=final_model, name=name, train_X=train_X, train_y=train_y,
                          test_X=test_X, test_y=test_y)


def do_sl_experiments(train_X, train_y, test_X, test_y, label_name):
    """
       Implements experiments based on supervised learning.
    :param train_X: feature matrix for training
    :param train_y: label vector for training
    :param test_X: feature matrix for test
    :param test_y: label vector for test
    :param label_name: label name to save models
    """
    # For the linear perceptron classifier:
    perceptron_model = Perceptron(tol=1e-3, random_state=0)
    perceptron_model.fit(X=train_X, y=train_y)
    save_model(filename='linear perceptron ' + label_name , model=perceptron_model)
    get_final_performance(model=perceptron_model, name='linear perceptron',
                          train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y)

    # For the Gaussian Naive Bayes classifier:
    gaussian_nb_model = GaussianNB()
    gaussian_nb_model.fit(X=train_X, y=train_y)
    save_model(filename='Gaussian Naive Bayes ' + label_name, model=gaussian_nb_model)
    get_final_performance(model=gaussian_nb_model, name='Gaussian Naive Bayes',
                          train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y)

    # Prepare the data for cross-validation:
    fold_num = 5
    stfied_k_fold = KFold(n_splits=fold_num, shuffle=True, random_state=660)
    k_fold_tr_X, k_fold_tr_y = [], []
    k_fold_te_X, k_fold_te_y = [], []
    for train_index, test_index in stfied_k_fold.split(X=train_X, y=train_y):
        k_fold_tr_X.append(train_X[train_index])
        k_fold_tr_y.append(train_y[train_index])
        k_fold_te_X.append(train_X[test_index])
        k_fold_te_y.append(train_y[test_index])

    # For the SVM and logistic regression classifiers:
    C_values = np.arange(0.1, 3, 0.1)
    svm_cross_vali_acc = do_cr_val_training(values=C_values, fold_num=fold_num, name='support vector machine',
                                            k_fold_tr_X=k_fold_tr_X, k_fold_tr_y=k_fold_tr_y,
                                            k_fold_te_X=k_fold_te_X, k_fold_te_y=k_fold_te_y)
    get_cr_val_performance(cross_vali_acc=svm_cross_vali_acc, values=C_values, name='support vector machine',
                           train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y, label_name=label_name)
    lgr_cross_vali_acc = do_cr_val_training(values=C_values, fold_num=fold_num, name='logistic regression',
                                            k_fold_tr_X=k_fold_tr_X, k_fold_tr_y=k_fold_tr_y,
                                            k_fold_te_X=k_fold_te_X, k_fold_te_y=k_fold_te_y)
    get_cr_val_performance(cross_vali_acc=lgr_cross_vali_acc, values=C_values, name='logistic regression',
                           train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y, label_name=label_name)

    # For the decision tree classifier:
    depth_values = np.arange(1, 30, 1)
    dt_cross_vali_acc = do_cr_val_training(values=depth_values, fold_num=fold_num, name='decision tree',
                                            k_fold_tr_X=k_fold_tr_X, k_fold_tr_y=k_fold_tr_y,
                                            k_fold_te_X=k_fold_te_X, k_fold_te_y=k_fold_te_y)
    get_cr_val_performance(cross_vali_acc=dt_cross_vali_acc, values=depth_values, name='decision tree',
                           train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y, label_name=label_name)

    # For the random forest and AdaBoost classifiers:
    estimator_values = np.arange(1, 20, 1)
    rf_cross_vali_acc = do_cr_val_training(values=estimator_values, fold_num=fold_num, name='random forest',
                                            k_fold_tr_X=k_fold_tr_X, k_fold_tr_y=k_fold_tr_y,
                                            k_fold_te_X=k_fold_te_X, k_fold_te_y=k_fold_te_y)
    get_cr_val_performance(cross_vali_acc=rf_cross_vali_acc, values=estimator_values, name='random forest',
                           train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y, label_name=label_name)
    adb_cross_vali_acc = do_cr_val_training(values=estimator_values, fold_num=fold_num, name='AdaBoost',
                                            k_fold_tr_X=k_fold_tr_X, k_fold_tr_y=k_fold_tr_y,
                                            k_fold_te_X=k_fold_te_X, k_fold_te_y=k_fold_te_y)
    get_cr_val_performance(cross_vali_acc=adb_cross_vali_acc, values=estimator_values, name='AdaBoost',
                           train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y, label_name=label_name)


def get_sl_results(train_X, train_y, test_X, test_y, label_name, lp_filename, gnp_filename,
                   svc_filename, lgr_filename, rf_filename, adb_filename):
    """
       Gets results of experiments on supervised learning.
    :param train_X: feature matrix for training
    :param train_y: label vector for training
    :param test_X: feature matrix for test
    :param test_y: label vector for test
    :param label_name: label name to save models
    :param lp_filename: linear perceptron
    :param gnp_filename: Gaussian Naive Bayes
    :param svc_filename: support vector machine
    :param lgr_filename: logistic regression
    :param rf_filename: random forest
    :param adb_filename: AdaBoost
    """
    # For the linear perceptron classifier:
    with open(lp_filename, 'rb') as lp_pickle_file:
        perceptron_model = pickle.load(lp_pickle_file)
    lp_pickle_file.close()
    get_final_performance(model=perceptron_model, name='linear perceptron '+label_name,
                          train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y)

    # For the Gaussian Naive Bayes classifier:
    with open(gnp_filename, 'rb') as (gnp_pickle_file):
        gaussian_nb_model = pickle.load(gnp_pickle_file)
    gnp_pickle_file.close()
    get_final_performance(model=gaussian_nb_model, name='Gaussian Naive Bayes '+label_name,
                          train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y)

    # For the support vector machine classifier:
    with open(svc_filename, 'rb') as (svc_pickle_file):
        svc_model = pickle.load(svc_pickle_file)
    svc_pickle_file.close()
    get_final_performance(model=svc_model, name='support vector machine '+label_name,
                          train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y)

    # For the logistic regression classifier:
    with open(lgr_filename, 'rb') as (lgr_pickle_file):
        lgr_model = pickle.load(lgr_pickle_file)
    lgr_pickle_file.close()
    get_final_performance(model=lgr_model, name='logistic regression '+label_name,
                          train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y)

    # For the random forest classifier:
    with open(rf_filename, 'rb') as (rf_pickle_file):
        rf_model = pickle.load(rf_pickle_file)
    rf_pickle_file.close()
    get_final_performance(model=rf_model, name='random forest '+label_name,
                          train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y)

    # For the AdaBoost classifier:
    with open(adb_filename, 'rb') as (adb_pickle_file):
        adb_model = pickle.load(adb_pickle_file)
    adb_pickle_file.close()
    get_final_performance(model=adb_model, name='AdaBoost '+label_name,
                          train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y)

