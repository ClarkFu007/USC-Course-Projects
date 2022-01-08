import copy
import random
import sklearn

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.svm import SVC
from qns3vm import QN_S3VM


def input_data(ssl_tr_file, te_file):
    """
       Inputs the dataset.
    :param ssl_tr_file: semi-supervised learning training data
    :param te_file: test data
    :return: ssl_train_X, ssl_train_y, test_X, test_y
    """
    ssl_tr_frame = pd.read_csv(ssl_tr_file)
    te_frame = pd.read_csv(te_file)

    return ssl_tr_frame.values[:, 0:10], ssl_tr_frame.values[:, 10], \
           te_frame.values[:, 0:10], te_frame.values[:, 10],


def main():
    """
       The main function.
    """
    # Input the data:
    print("My Sklearn version is {}.".format(sklearn.__version__))
    train_X, train_y, test_X, test_y = \
        input_data(ssl_tr_file='Data/SSL_data/ssl_train_data.csv',
                   te_file='Data/SSL_data/test_data.csv')
    """
    train_X: (200, 10), train_y: (200,)
    test_X: (200, 10), test_y: (200,)
    """
    # For the part(a):
    adb_model_a = SVC(C=1.0, kernel='linear')
    adb_model_a.fit(X=train_X, y=train_y)
    print("For the part (a), the classification accuracy on test data is {:.4f}"
          .format(adb_model_a.score(X=test_X, y=test_y)))
    # For the part(b):
    L_seq = np.arange(1, 11, 1)
    b_acc_array = np.zeros(10, dtype='float')
    for L_i in range(L_seq.shape[0]):
        adb_model_b = SVC(C=1.0, kernel='linear')
        L_index = int(2 * L_seq[L_i])
        adb_model_b.fit(X=train_X[0:L_index], y=train_y[0:L_index])
        b_acc_array[L_i] = adb_model_b.score(X=test_X, y=test_y)
        print("For the part (b) when L is {}, the classification accuracy "
              "on test data is {:.4f}".format(L_i + 1, b_acc_array[L_i]))

    # For the part(c):
    new_train_y = copy.deepcopy(train_y)
    new_train_y[new_train_y == 0] = -1
    new_test_y = copy.deepcopy(test_y)
    new_test_y[new_test_y == 0] = -1
    my_random_generator = random.Random()
    my_random_generator.seed(0)
    L_seq = np.arange(1, 11, 1)
    c_acc_array = np.zeros(10, dtype='float')
    for L_i in range(L_seq.shape[0]):
        L_index = int(2 * L_seq[L_i])
        train_l_X_list = []
        for sample_i in range(L_index):
            train_l_X_list.append(train_X[sample_i])
        train_ul_X_list = []
        for sample_i in range(L_index, train_X.shape[0]):
            train_ul_X_list.append(train_X[sample_i])
        train_l_y = new_train_y[0:L_index].astype(int).tolist()

        s3vm_model_c = QN_S3VM(train_l_X_list, train_l_y, train_ul_X_list,
                               my_random_generator, lam=1.0, kernel_type="Linear")
        _ = s3vm_model_c.train()
        preds_test_y = s3vm_model_c.getPredictions(test_X)
        c_acc_array[L_i] = np.sum(np.array(preds_test_y) == new_test_y) / new_test_y.shape[0]
        print("For the part (c) when L is {}, the classification accuracy "
              "on test data is {:.4f}".format(L_i + 1, c_acc_array[L_i]))

    # For the part(d):
    plt.figure(0)
    plt.plot(L_seq, b_acc_array, 'g', label='SVM')
    plt.plot(L_seq, c_acc_array, 'b', label='S3VM')
    plt.legend()
    plt.title(r'The plot of accuracy vs. $N_L$=2L')
    plt.ylabel(r'Accuracy values')
    plt.xlabel(r'L values')
    plt.tight_layout()
    plt.savefig("prob3d_results.png")
    plt.show()

    return


if __name__ == '__main__':
    main()