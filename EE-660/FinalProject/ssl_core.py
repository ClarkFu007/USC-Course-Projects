import copy
import random
import pickle

import numpy as np

from sklearn.model_selection import train_test_split
from qns3vm import QN_S3VM
from sklearn.svm import SVC
from utils import save_model


def do_ssl_experiments(train_X, train_y, unlabel_num, test_X, test_y, label_name):
    """
       Implements experiments based on semi-supervised learning.
    :param train_X: feature matrix for training
    :param train_y: label vector for training
    :param unlabel_num: number of unlabeled data points
    :param test_X: feature matrix for test
    :param test_y: label vector for test
    :param label_name: label name to save models
    """
    train_l_X, train_ul_X, train_l_y, _ = train_test_split(train_X, train_y, test_size=unlabel_num,
                                                           random_state=660)
    print("train_l_X.shape", train_l_X.shape)
    print("train_ul_X.shape", train_ul_X.shape)
    print("test_X.shape", test_X.shape)

    new_train_y = copy.deepcopy(train_y)
    new_train_y[new_train_y == 0] = -1
    new_train_l_y = copy.deepcopy(train_l_y)
    new_train_l_y[new_train_l_y == 0] = -1
    new_test_y = copy.deepcopy(test_y)
    new_test_y[new_test_y == 0] = -1

    train_l_X_list = []
    for sample_i in range(train_l_X.shape[0]):
        train_l_X_list.append(train_l_X[sample_i])
    train_ul_X_list = []
    for sample_i in range(train_ul_X.shape[0]):
        train_ul_X_list.append(train_ul_X[sample_i])
    new_train_l_y = new_train_l_y.astype(int).tolist()

    my_random_generator = random.Random()
    my_random_generator.seed(0)
    model = QN_S3VM(train_l_X_list, new_train_l_y, train_ul_X_list, my_random_generator, lam=0.00001, lamU=1,
                    kernel_type="RBF", sigma=0.2, estimate_r=0.00)
    preds_train_y = model.train()
    preds_test_y = model.getPredictions(test_X)
    train_acc = np.sum(np.array(preds_train_y) == new_train_y) / train_y.shape[0]
    print("Classification accuracy of QN-S3VM on training data: ", train_acc)
    test_acc = np.sum(np.array(preds_test_y) == new_test_y) / test_y.shape[0]
    print("Classification accuracy of QN-S3VM on test data: ", test_acc)
    save_model(filename='S3VM ' + label_name, model=model)

    baseline = SVC(C=0.1, kernel='rbf', random_state=660)
    baseline.fit(train_l_X, train_l_y)
    print('SVC: test acc:', baseline.score(X=test_X, y=test_y))
    save_model(filename='SVM ' + label_name, model=baseline)


def get_ssl_results(train_X, train_y, unlabel_num, test_X, test_y, label_name):
    """
       Gets results of experiments on semi-supervised learning.
    :param train_X: feature matrix for training
    :param train_y: label vector for training
    :param unlabel_num: number of unlabeled data points
    :param test_X: feature matrix for test
    :param test_y: label vector for test
    :param label_name: label name to save models
    """
    train_l_X, train_ul_X, train_l_y, _ = train_test_split(train_X, train_y, test_size=unlabel_num,
                                                           random_state=660)
    new_train_y = copy.deepcopy(train_y)
    new_train_y[new_train_y == 0] = -1
    new_train_l_y = copy.deepcopy(train_l_y)
    new_train_l_y[new_train_l_y == 0] = -1
    new_test_y = copy.deepcopy(test_y)
    new_test_y[new_test_y == 0] = -1

    train_l_X_list = []
    for sample_i in range(train_l_X.shape[0]):
        train_l_X_list.append(train_l_X[sample_i])
    train_ul_X_list = []
    for sample_i in range(train_ul_X.shape[0]):
        train_ul_X_list.append(train_ul_X[sample_i])

    s3vm_filename = 'saved_models/ssl/S3VM ' + label_name + '.pkl'
    with open(s3vm_filename, 'rb') as s3vm_pickle_file:
        s3vm_model = pickle.load(s3vm_pickle_file)
    s3vm_pickle_file.close()

    preds_test_y = s3vm_model.getPredictions(test_X)
    test_acc = np.sum(np.array(preds_test_y) == new_test_y) / test_y.shape[0]
    print("Classification accuracy of QN-S3VM"+label_name+" on test data: ", test_acc)

    svm_filename = 'saved_models/ssl/SVM ' + label_name + '.pkl'
    with open(svm_filename, 'rb') as svm_pickle_file:
        svm_model = pickle.load(svm_pickle_file)
    svm_pickle_file.close()
    print('SVC'+label_name+' test acc:', svm_model.score(X=test_X, y=test_y))




