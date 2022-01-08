import random

import numpy as np
import matplotlib.pyplot as plt


def do_prob2_d(epsilon, tolerance, vc_num):
    """
       Implements the experiment of the problem2-d.
    :param epsilon: value of epsilon
    :param tolerance: value of tolerance
    :param vc_num: number of VC dimension
    """
    N_value = 3000
    while True:
        N_temp = 8 * (np.log(4) + vc_num * np.log(2 * N_value) - np.log(tolerance)) / epsilon ** 2
        if N_value >= N_temp:
            print("{} training samples would ensure a generalization error of {}.".format(N_value, epsilon))
            break
        else:
            N_value = int(np.ceil(N_temp))


def get_K_datasets(K_value):
    """
       Gets K datasets.
    :param K_value: value of K
    :return: K datasets
    """
    datasets = []
    for index_i in range(K_value):
        random.seed(index_i)
        x1 = random.uniform(-1, 1)
        random.seed(index_i + K_value)
        x2 = random.uniform(-1, 1)
        datasets.append([[x1, x1 ** 2], [x2, x2 ** 2]])
    return datasets


def do_prob3_c():
    """
       Implements the experiment of the problem3-c.
    """
    hyp_set_num = 10000
    K_datasets = get_K_datasets(K_value=hyp_set_num)

    # For bias
    a_seq = np.zeros(hyp_set_num, dtype='float')
    b_seq = np.zeros(hyp_set_num, dtype='float')
    for hyp_set_i in range(hyp_set_num):
        x1_value = K_datasets[hyp_set_i][0][0]
        x2_value = K_datasets[hyp_set_i][1][0]
        a_seq[hyp_set_i] = x1_value + x2_value
        b_seq[hyp_set_i] = - x1_value * x2_value
    a_hat = np.mean(a_seq)
    b_hat = np.mean(b_seq)
    print("a_hat", a_hat)
    print("b_hat", b_hat)
    bias = 0
    x_seq = np.arange(-1., 1., 0.001)
    y_seq = np.square(x_seq)
    y_pred_seq = a_hat * x_seq + b_hat
    for x_i in range(x_seq.shape[0]):
        bias = bias + (y_pred_seq[x_i] - y_seq[x_i]) ** 2
    print("The value of bias is {:.4f}.".format(bias / x_seq.shape[0]))

    # For variance
    var_value = 0
    for hyp_set_i in range(hyp_set_num):
        x1_value = K_datasets[hyp_set_i][0][0]
        y1_value = K_datasets[hyp_set_i][0][1]
        y1_pred = a_hat * x1_value + b_hat
        x2_value = K_datasets[hyp_set_i][1][0]
        y2_value = K_datasets[hyp_set_i][1][1]
        y2_pred = a_hat * x2_value + b_hat
        var_value = var_value + (y1_pred - y1_value) ** 2 + (y2_pred - y2_value) ** 2
    print("The value of var is {:.4f}.".format(var_value / hyp_set_num))

    # The plot of g_(x) and f(x)
    plt.figure()
    plt.plot(x_seq, y_seq, 'g')
    plt.plot(x_seq, y_pred_seq, 'b')
    plt.title(r'The plot of $\bar g$(x) and f(x) for -1 < x < 1')
    plt.ylabel(r'y values')
    plt.xlabel(r'x values')
    plt.tight_layout()
    plt.savefig("The plot of g_(x) and f(x).png")
    plt.show()


def main():
    """
       The main function.
    """
    do_prob2_d(epsilon=0.1, tolerance=0.1, vc_num=11)
    do_prob3_c()

    return


if __name__ == '__main__':
    main()