import csv

import numpy as np
import matplotlib.pyplot as plt

from numpy import sum, multiply, square, sqrt
from numpy import average, std, dot, expand_dims
from sklearn import svm
from sklearn.model_selection import StratifiedKFold

from plotSVMBoundaries import plotSVMBoundaries


def input_data(datafile_w, data_m, data_n, mode):
    """
       Input the data or label(y) data. Set mode as 'feature' when
    we want to input feature data or set mode as 'label' when we want
    to input label data.
    :param datafile_w: location of the data file.
    :param data_m: number of rows.
    :param data_n: number of columns.
    :param mode: feature or label.
    :return: feature matrix X
    """
    if mode == "feature":
        in_data = np.zeros((data_m, data_n), dtype='float')
    elif mode == "label":
        in_data = np.zeros((data_m, data_n), dtype='int')
    else:
        print("Mode unmatched!")
        return None
    with open(datafile_w, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            data = [float(datum) for datum in row]
            in_data[i] = data
    if mode == "label":
        in_data = np.squeeze(in_data)

    return in_data


def finish_prob2(part, train_X, train_y, C_value=None, gamma_value=None, verbose=True):
    """
       Finishes the problem2 of the homework6 of EE559. When part is 'a', solve the part (a)
    of problem 2. When part is 'abc', solve the part (b) and (c) of problem 2. When part is 'd',
    solve the part (d) of problem 2. When part is 'e', solve the part (e) of problem 2.
    :param part: to denote which subpart we want to solve.
    :param train_X: feature matrix for training data.
    :param train_y: label vector for training data.
    :param C_value: value C to control support vector machine.
    :param gamma_value: value gamma to control 'rbf' kernel.
    :param verbose: whether to print information.
    Outputs the requried information.
    """
    if part == 'a' or part == 'abc':
        # Get the trained SVM model
        svm_model = svm_demo(C_value=C_value, gamma_value='scale', kernel_type='linear',
                             train_X=train_X, train_y=train_y, verbose=True, to_return=True)
        if part == 'abc':
            if verbose:
                print("When C is {}, the support vectors are {}."
                      .format(C_value, svm_model.support_vectors_))
                print("The coef_ and intercept_ are {} and {}".format(svm_model.coef_, svm_model.intercept_))
                print("Decision boundary equation", svm_model.dual_coef_)

            # Use loop to verify whether support vectors are located on the margin boundary
            for sup_vec_i in range(svm_model.support_vectors_.shape[0]):
                if verbose:
                    print(dot(svm_model.coef_, expand_dims(svm_model.support_vectors_[sup_vec_i], axis=1))
                          + svm_model.intercept_)
            plotSVMBoundaries(training=train_X, label_train=train_y, classifier=svm_model,
                              support_vectors=svm_model.support_vectors_)

    elif part == 'd' or part == 'e':
        if part == 'd':
            svm_demo(C_value=C_value, gamma_value='auto', kernel_type='rbf',
                     train_X=train_X, train_y=train_y, verbose=True)
        elif part == 'e':
            svm_demo(C_value=1.0, gamma_value=gamma_value, kernel_type='rbf',
                     train_X=train_X, train_y=train_y, verbose=True)
        else:
            print("Part error!")
            return None

    else:
        print("Part error!")
        return None


def svm_demo(C_value, gamma_value, kernel_type, train_X, train_y, verbose=False, to_return=False):
    """
       Train the SVM model with different hyperparameters to do experiments. If we want to return
    the trained model, just set to_return as True.
    :param C_value: value of C.
    :param gamma_value: value of gamma.
    :param kernel_type: type of kernel.
    :param train_X: feature matirx.
    :param train_y: label vector.
    :param verbose: whether to print results and show the picture or not.
    :param to_return: if true, return the trained model.
    :return: the trained model if we want.
    """
    svm_model = svm.SVC(C=C_value, gamma=gamma_value, kernel=kernel_type)
    svm_model.fit(X=train_X, y=train_y)
    if verbose:
        print("When C is {} and gamma is {}, the classification accuracy is {:4.3f}."
              .format(C_value, gamma_value, svm_model.score(X=train_X, y=train_y)))
        plotSVMBoundaries(training=train_X, label_train=train_y, classifier=svm_model)
    if to_return:
        return svm_model


def finish_prob3(part, train_X, train_y, test_X, test_y, C_value=None, gamma_value=None, verbose=True):
    """
       Finishes the problem3 of the homework6 of EE559. When part is 'a', solve the part (a)
    of problem 3. When part is 'b', solve the part (b) of problem 3. When part is 'cd',
    solve the part (c) and (d) of problem 3.
    :param part: to denote which subpart we want to solve.
    :param train_X: feature matrix for training data.
    :param train_y: label vector for training data.
    :param test_X: feature matrix for test data.
    :param test_y: label vector for test data.
    :param C_value: value C to control support vector machine.
    :param gamma_value: value gamma to control 'rbf' kernel.
    :param verbose: whether to print information.
    Outputs the requried information.
    """
    if part == 'a':
        # Report the average crossvalidation accuracy
        cross_vali_acc = get_cross_vali_acc(C_value=C_value, gamma_value=gamma_value,
                                            train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y)
        if verbose:
            print("When gamma is {} and C is {}, the average cross-validation accuracy is {:4.3f}."
                  .format(gamma_value, C_value, average(cross_vali_acc)))

    elif part == 'b':
        # use cross validation to find the best parameter set (model selection).
        acc_matrix, std_matrix = solve_prob3_b(train_X=train_X, train_y=train_y,
                                               test_X=test_X, test_y=test_y,
                                               gamma_value=gamma_value,
                                               C_value=C_value)
        # (i) Do the visualization of Accuracy
        fig, ax = plt.subplots(1, 1)
        c = ax.pcolor(acc_matrix, cmap='coolwarm', edgecolors='k')
        ax.set_ylabel("gamma values")
        ax.set_xlabel("C values")
        ax.set_title('mean accuracy')
        fig.colorbar(c, ax=ax)
        fig.tight_layout()
        plt.savefig("Accuracy visualization")
        plt.show()

        # (ii) Find the best value pair of [gamma, C]
        gamma_num, C_num = gamma_value.shape[0], C_value.shape[0]
        max_acc, target_gamma_i, target_C_i = get_target(gamma_num=gamma_num, C_num=C_num,
                                                         acc_matrix=acc_matrix)
        print("The target gamma position is {} and the target C position is {}."
              .format(target_gamma_i, target_C_i))
        print("When gamma is {:4.3f} and C is {:4.3f}, the best average cross-validation accuracy is {:4.3f} "
              "and its standard deviation is {:4.3f}."
              .format(gamma_value[target_gamma_i], C_value[target_C_i],
                      max_acc, std_matrix[target_gamma_i, target_C_i]))

    elif part == 'cd':
        """
           Repeat the cross validation procedure in (b) T=20 times (runs), storing the
        resulting arrays accuracy(t) and std_dev(t) each time.
        """
        T_num = 20
        acc_matrix_T = []
        std_matrix_T = []
        # Perform 20 trials
        for T_i in range(T_num):
            acc_matrix, std_matrix = solve_prob3_b(train_X=train_X, train_y=train_y,
                                                   test_X=test_X, test_y=test_y,
                                                   gamma_value=gamma_value,
                                                   C_value=C_value)
            acc_matrix_T.append(acc_matrix)
            std_matrix_T.append(std_matrix)

        gamma_num, C_num = gamma_value.shape[0], C_value.shape[0]
        target_gamma_list, target_C_list = [], []
        best_acc_list = []
        """
           Get maxumum accuracy, target gamma index, target C index in each trial.
        """
        for T_i in range(T_num):
            max_acc, target_gamma_i, target_C_i = get_target(gamma_num=gamma_num, C_num=C_num,
                                                             acc_matrix=acc_matrix_T[T_i])
            best_acc_list.append(max_acc)
            target_gamma_list.append(target_gamma_i)
            target_C_list.append(target_C_i)

        print("The target gamma position is {} and the target C position is {}."
              .format(target_gamma_list, target_C_list))
        max_acc = 0
        target_gamma_i, target_C_i = 0, 0
        for T_i in range(T_num):
            print("When gamma is {:4.3f} and C is {:4.3f}, "
                  "the best average cross-validation accuracy is {:4.3f} and the standard deviation is {:4.3f}."
                  .format(gamma_value[target_gamma_list[T_i]], C_value[target_C_list[T_i]],
                          best_acc_list[T_i], std_matrix_T[T_i][target_gamma_list[T_i], target_C_list[T_i]]))
            if max_acc < best_acc_list[T_i]:
                max_acc = best_acc_list[T_i]
                target_gamma_i = target_gamma_list[T_i]
                target_C_i = target_C_list[T_i]

        """
           Use the full training set to train the final classifier using the best pair of
        [γ, C] from (c) (ii) above. Then use the test set to estimate the accuracy of
        the final classifier on unknowns.
        """
        svm_model = svm.SVC(C=C_value[target_C_i], kernel='rbf', gamma=gamma_value[target_gamma_i])
        svm_model.fit(X=train_X, y=train_y)
        print("When gamma is {:4.3f} and C is {:4.3f}, the classification accuracy is {:4.3f}."
              .format(gamma_value[target_gamma_i], C_value[target_C_i],
                      svm_model.score(X=test_X, y=test_y)))
    else:
        print("Part error!")
        return None


def get_cross_vali_acc(C_value, gamma_value, train_X, train_y, test_X, test_y, kernel_type='rbf'):
    """
       Get cross-validation accuracy matrix with different hyperparameters.
    :param C_value: value of C.
    :param gamma_value: value of gamma.
    :param train_X: feature matrix for training data.
    :param train_y: label vector for training data.
    :param test_X: feature matrix for test data.
    :param test_y: label vector for test data.
    :param kernel_type: kernel type.
    :return: the resulting cross-validation accuracy matrix.
    """
    fold_num = 5
    stfied_k_fold = StratifiedKFold(n_splits=fold_num, shuffle=True)
    k_fold_tr_X, k_fold_tr_y = [], []
    k_fold_te_X, k_fold_te_y = [], []
    for train_index, test_index in stfied_k_fold.split(X=train_X, y=train_y):
        k_fold_tr_X.append(train_X[train_index])
        k_fold_tr_y.append(train_y[train_index])
        k_fold_te_X.append(test_X[test_index])
        k_fold_te_y.append(test_y[test_index])

    cross_vali_acc = np.zeros(fold_num, dtype='float')
    for fold_i in range(fold_num):
        svm_model = svm_demo(C_value=C_value, gamma_value=gamma_value, kernel_type=kernel_type,
                             train_X=train_X, train_y=train_y, to_return=True)
        cross_vali_acc[fold_i] = svm_model.score(X=k_fold_te_X[fold_i], y=k_fold_te_y[fold_i])

    return cross_vali_acc


def solve_prob3_b(train_X, train_y, test_X, test_y, gamma_value, C_value):
    """
       Get accuracy and standard deviation matrices for specified ranges.
    of gamma and C values.
    :param train_X: feature matrix for training data.
    :param train_y: label vector for training data.
    :param test_X: feature matrix for test data.
    :param test_y: label vector for test data.
    :param gamma_value: value of gamma.
    :param C_value: value of C.
    :return: the resulting accuracy and standard deviation matrices.
    """
    gamma_num, C_num = gamma_value.shape[0], C_value.shape[0]
    acc_matrix = np.zeros((gamma_num, C_num), dtype='float')
    std_matrix = np.zeros((gamma_num, C_num), dtype='float')
    for gamma_i in range(gamma_num):
        for C_i in range(C_num):
            cross_vali_acc = get_cross_vali_acc(C_value=C_value[C_i], gamma_value=gamma_value[gamma_i],
                                                train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y)
            acc_matrix[gamma_i, C_i] = average(cross_vali_acc)
            std_matrix[gamma_i, C_i] = std(cross_vali_acc)

    return acc_matrix, std_matrix


def get_target(gamma_num, C_num, acc_matrix):
    """
       Get the maximum accuracy and relevant gamma and C indices.
    :param gamma_num: number of gamma values.
    :param C_num: number of C values.
    :param acc_matrix: accuracy matrix.
    :return: maxumum accuracy, target gamma index, target C index.
    """
    target_gamma_i, target_C_i = 0, 0
    max_acc = 0
    for gamma_i in range(gamma_num):
        for C_i in range(C_num):
            if max_acc < acc_matrix[gamma_i, C_i]:
                max_acc = acc_matrix[gamma_i, C_i]
                target_gamma_i = gamma_i
                target_C_i = C_i

    return max_acc, target_gamma_i, target_C_i