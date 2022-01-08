import copy

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from numpy import log, sqrt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.model_selection import KFold


def do_prob1_a(data_X, data_y, N_in, N_tol=10**6, N_out=10**5, exp_num=1000):
    """
       Finishes the problem1 part(a).
    :param data_X: features of data
    :param data_y: real values of data
    :param N_in: total number of in-sample data points
    :param N_tol: number of total data points
    :param N_out: number of out-of-sample data points
    :param exp_num: number of experiments
    """
    # Part(i): compute theoretical generalization bound values as a function of delta.
    tolerance_seq = np.arange(0.01, 0.501, 0.01)
    vc_num = 4
    t_gb_values = sqrt(8 * (log(4) + vc_num * log(2 * N_in) - log(tolerance_seq)) / N_in)
    print("t_gb_values", t_gb_values)

    # Part(ii): extract D_out with N_out samples and the first d (d_vc-1) features.
    d_num = vc_num - 1
    in_X, out_X, in_y, out_y = train_test_split(data_X, data_y, test_size=N_out, random_state=660)
    out_X = out_X[:, 0:d_num]

    # Part(iii) and Part(iv):
    E_in_results = np.zeros(exp_num, dtype='float')
    E_out_results = np.zeros(exp_num, dtype='float')
    fold_num = int(N_tol / N_in)
    for exp_i in range(exp_num):
        stfied_k_fold = KFold(n_splits=fold_num, shuffle=True, random_state=exp_i)
        np.random.seed(exp_i)
        target_index, index = np.random.randint(fold_num), 0
        for _, test_index in stfied_k_fold.split(X=data_X, y=data_y):
            if index == 1:
                in_bag_X = data_X[test_index]
                in_bag_y = data_y[test_index]
                break
            index += 1

        in_bag_X = in_bag_X[:, 0:d_num]
        perceptron_model = Perceptron(random_state=660)
        perceptron_model.fit(X=in_bag_X, y=in_bag_y)
        E_in_results[exp_i] = 1 - perceptron_model.score(X=in_bag_X, y=in_bag_y)
        E_out_results[exp_i] = 1 - perceptron_model.score(X=out_X, y=out_y)

    # Part(v):
    diff_results = np.absolute(E_out_results - E_in_results)
    diff_results.sort()
    max_values = np.zeros(t_gb_values.shape[0], dtype='float')
    for tolerance_i in range(tolerance_seq.shape[0]):
        tolerance_value = tolerance_seq[tolerance_i]
        position = int((1 - tolerance_value) * exp_num)
        max_values[tolerance_i] = diff_results[position - 1]

    plt.figure(0)
    plt.subplot(211)  # rows, columns, th_plot
    plt.plot(tolerance_seq, t_gb_values, 'b')
    plt.ylabel('Generalization bounds')
    plt.xlabel('Tolerance values')
    plt.title(r'The plot for the prob1_a_i when $N_i$$_n$=' + str(N_in))
    plt.subplot(212)
    plt.plot(tolerance_seq, max_values, 'b')
    plt.ylabel('Max values')
    plt.xlabel('Tolerance values')
    plt.title(r'The plot for the prob1_a_v when $N_i$$_n$=' + str(N_in))
    plt.tight_layout()
    plt.savefig('problem1_a_Nin' + str(N_in) + '.png')
    plt.show()


def do_prob1_b(data_X, data_y, N_in, N_tol=10**6, N_out=10**5, exp_num=100):
    """
       Finishes the problem1 part(b).
    :param data_X: features of data
    :param data_y: real values of data
    :param N_in: total number of in-sample data points
    :param N_tol: number of total data points
    :param N_out: number of out-of-sample data points
    :param exp_num: number of experiments
    """
    # Part(i): compute theoretical generalization bound values as a function of VC dimension.
    vc_seq = np.arange(2, 11 + 1, 1)
    tolerance_value = 0.1
    t_gb_values = sqrt(8 * (log(4) + vc_seq * log(2 * N_in) - log(tolerance_value)) / N_in)
    print("t_gb_values", t_gb_values)

    # Part(ii): extract D_out with N_out samples and the 10 features.
    _, out_X, _, out_y = train_test_split(data_X, data_y, test_size=N_out, random_state=660)

    # Part(iii) and Part(iv):
    E_in_results = np.zeros((exp_num, vc_seq.shape[0]), dtype='float')
    E_out_results = np.zeros((exp_num, vc_seq.shape[0]), dtype='float')

    fold_num = int(N_tol / N_in)
    for exp_i in range(exp_num):
        stfied_k_fold = KFold(n_splits=fold_num, shuffle=True, random_state=exp_i)
        np.random.seed(exp_i)
        target_index, index = np.random.randint(fold_num), 0
        for _, test_index in stfied_k_fold.split(X=data_X, y=data_y):
            if index == 1:
                in_bag_X = data_X[test_index]
                in_bag_y = data_y[test_index]
                break
            index += 1
        for vc_i in range(vc_seq.shape[0]):
            vc_num = vc_seq[vc_i]
            temp_in_X = copy.deepcopy(in_bag_X[:, 0:vc_num - 1])
            temp_out_X = copy.deepcopy(out_X[:, 0:vc_num - 1])
            perceptron_model = Perceptron(random_state=660)
            perceptron_model.fit(X=temp_in_X, y=in_bag_y)
            E_in_results[exp_i, vc_i] = 1 - perceptron_model.score(X=temp_in_X, y=in_bag_y)
            E_out_results[exp_i, vc_i] = 1 - perceptron_model.score(X=temp_out_X, y=out_y)

    # Part(v):
    diff_results = np.absolute(E_out_results - E_in_results)
    max_values = np.zeros(t_gb_values.shape[0], dtype='float')
    for vc_i in range(vc_seq.shape[0]):
        diff_results_vc_i = copy.deepcopy(diff_results[:, vc_i])
        diff_results_vc_i.sort()
        position = int((1 - tolerance_value) * exp_num)
        max_values[vc_i] = diff_results_vc_i[position - 1]

    plt.figure(0)
    plt.subplot(211)  # rows, columns, th_plot
    plt.plot(vc_seq, t_gb_values, 'b')
    plt.ylabel('Generalization bounds')
    plt.xlabel('VC dimensions')
    plt.title(r'The plot for the prob1_b_i when $N_i$$_n$=' + str(N_in))
    plt.subplot(212)
    plt.plot(vc_seq, max_values, 'b')
    plt.ylabel('Max values')
    plt.xlabel('VC dimensions')
    plt.title(r'The plot for the prob1_b_vi when $N_i$$_n$=' + str(N_in))
    plt.tight_layout()
    plt.savefig('problem1_b_Nin' + str(N_in) + '.png')
    plt.show()


def display_prob1_c(E_out_results, E_results, t_gb_values, N, mode, tolerance_value=0.1, exp_num=100):
    """
       Displays the results of the problem1 part(c).
    :param E_out_results: results of out-of-sample errors
    :param E_results: results of out-of-sample errors
    :param t_gb_values: theoretical generalization bound values
    :param N: number of data points
    :param mode: crucial words to print
    :param tolerance_value: tolerance value
    :param exp_num: number of experiments
    """
    diff_results = np.absolute(E_out_results - E_results)
    max_values = np.zeros(t_gb_values.shape[0], dtype='float')
    for N_i in range(N.shape[0]):
        diff_results_i = copy.deepcopy(diff_results[:, N_i])
        diff_results_i.sort()
        position = int((1 - tolerance_value) * exp_num)
        max_values[N_i] = diff_results_i[position - 1]

    plt.figure(0)
    plt.subplot(211)  # rows, columns, th_plot
    plt.plot(N, t_gb_values, 'b')
    plt.ylabel('Generalization bounds')
    if mode == 'training':
        plt.xlabel('# of training points')
        plt.title('The plot for the prob1_c_i')
    elif mode == 'test':
        plt.xlabel('# of test points')
        plt.title('The plot for the prob1_c_ii')
    plt.subplot(212)
    plt.plot(N, max_values, 'b')
    plt.ylabel('Max values')
    if mode == 'training':
        plt.xlabel('# of training points')
        plt.title('The plot for the prob1_c_vi')
    elif mode == 'test':
        plt.xlabel('# of test points')
        plt.title('The plot for the prob1_c_vii')
    plt.tight_layout()
    plt.savefig('problem1_c_' + mode + '.png')
    plt.show()


def do_prob1_c(data_X, data_y, N_tol=10**6, N_out=10**5, exp_num=100, vc_num=4, tolerance_value=0.1):
    """
       Finishes the problem1 part(c).
    :param data_X: features of data
    :param data_y: real values of data
    :param N_tol: total number of data points
    :param N_out: number of out-of-sample data points
    :param exp_num: number of experiments
    :param vc_num: value of VD dimension
    :param tolerance_value: tolerance value
    """
    # Part(i): compute theoretical generalization bound values as a function of N_train.
    N_tr = np.array([10, 30, 100, 300, 1000, 3000, 10000], dtype='int')
    N_te = np.array([2, 6, 20, 60, 200, 600, 2000], dtype='int')
    t_gb_values_tr = sqrt(8 * (log(4) + vc_num * log(2 * N_tr) - log(tolerance_value)) / N_tr)
    print("t_gb_values_tr", t_gb_values_tr)
    t_gb_values_te = sqrt((log(2) - log(tolerance_value)) / (N_te * 2))
    print("t_gb_values_te", t_gb_values_te)

    # Part(ii): extract D_out with N_out samples and the 10 features.
    _, out_X, _, out_y = train_test_split(data_X, data_y, test_size=N_out, random_state=660)
    out_X = out_X[:, 0:vc_num - 1]

    # Part(iii), Part(iv), and Part(v):
    E_train_results = np.zeros((exp_num, N_tr.shape[0]), dtype='float')
    E_test_results = np.zeros((exp_num, N_tr.shape[0]), dtype='float')
    E_out_results = np.zeros((exp_num, N_te.shape[0]), dtype='float')
    for exp_i in range(exp_num):
        for N_i in range(N_tr.shape[0]):
            tr_num = N_tr[N_i]
            te_num = N_te[N_i]
            train_X, rest_X, train_y, rest_y = train_test_split(data_X, data_y, test_size=N_tol - tr_num,
                                                                random_state=exp_i)
            test_X, _, test_y, _ = train_test_split(rest_X, rest_y, test_size=N_tol - tr_num - te_num,
                                                    random_state=exp_i + N_i)
            train_X = train_X[:, 0:vc_num - 1]
            test_X = test_X[:, 0:vc_num - 1]
            perceptron_model = Perceptron(random_state=660)
            perceptron_model.fit(X=train_X, y=train_y)
            E_train_results[exp_i, N_i] = 1 - perceptron_model.score(X=train_X, y=train_y)
            E_test_results[exp_i, N_i] = 1 - perceptron_model.score(X=test_X, y=test_y)
            E_out_results[exp_i, N_i] = 1 - perceptron_model.score(X=out_X, y=out_y)

    # Part(vi):
    display_prob1_c(E_out_results=E_out_results, E_results=E_train_results,
                    t_gb_values=t_gb_values_tr, N=N_tr, mode='training')
    # Part(vii):
    display_prob1_c(E_out_results=E_out_results, E_results=E_test_results,
                    t_gb_values=t_gb_values_te, N=N_te, mode='test')


def do_prob1():
    """
       Implements the experiment of generalization bounds in the problem1.
    """
    # Input the data.
    data_frame = pd.read_csv("dataset/prob1/problem1_data.csv.")
    data = data_frame.values  # (1000000, 11)
    data_X, data_y = copy.deepcopy(data[:, 0:10]), copy.deepcopy(data[:, 10])

    # From part(a) to part(c):
    do_prob1_a(data_X=data_X, data_y=data_y, N_in=1000)
    do_prob1_b(data_X=data_X, data_y=data_y, N_in=1000)
    do_prob1_c(data_X=data_X, data_y=data_y)

    # Part(d):
    do_prob1_a(data_X=data_X, data_y=data_y, N_in=10)
    do_prob1_b(data_X=data_X, data_y=data_y, N_in=10)
    do_prob1_a(data_X=data_X, data_y=data_y, N_in=100)
    do_prob1_b(data_X=data_X, data_y=data_y, N_in=100)
