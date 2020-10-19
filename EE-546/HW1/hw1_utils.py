import csv
import random
import numpy as np
from numpy import dot, exp, log, sum, square
from numpy import expand_dims, absolute
import matplotlib.pyplot as plt


def input_data(datafile_w, data_m, data_n):
    """
    Inputs:
        the location of the data file
        the number of row
        the number of column
    Outputs:
        feature matrix X
        label vector y
    """
    InputData = np.zeros((data_m, data_n), dtype='float')
    with open(datafile_w, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            data = [float(datum) for datum in row]
            InputData[i] = data
    print("InputData.shape", InputData.shape)

    Data_X = InputData[0:data_m, 2:32]  # Feature matrix X
    Data_y = InputData[0:data_m, 1]  # Label vector y
    Data_y = Data_y.astype(np.int)
    Data_y = np.expand_dims(Data_y, axis=1)
    print("Data_X.shape", Data_X.shape)
    print("Data_y.shape", Data_y.shape)

    return Data_X, Data_y


def normalize_data(Data_X, sample_num):
    """
    Inputs:
        the feature matrix X
        the number of samples
    Outputs:
        normalized feature matrix X
    """
    X_mean = np.mean(Data_X, axis=0)
    X_mean = np.expand_dims(X_mean, axis=0)
    Data_mean = np.repeat(a=X_mean, repeats=sample_num, axis=0)

    Data_X = Data_X - Data_mean
    Data_L2 = np.expand_dims(np.sqrt(np.sum(np.square(Data_X), axis=1)), axis=1)
    Data_X = np.true_divide(Data_X, Data_L2)

    return Data_X


def split_tr_te(dataset, label_set, train_num, seed_value):
    """
    Inputs:
        the total dataset
        the total label set
        the number of the training set
        the seed value to random sampling
    Output: the training set x & y and the test set x & y
    """
    sample_num, fea_num = dataset.shape[:]
    index_list = list(range(sample_num))
    random.seed(seed_value)  # Make the shuffle function behave the same
    random.shuffle(index_list)
    train_index = index_list[0: train_num]
    test_index = index_list[train_num: sample_num]

    train_x = np.zeros((train_num, fea_num), dtype='float')
    train_y = np.zeros((train_num, 1), dtype='int')
    for sample_i in range(train_num):
        train_x[sample_i] = dataset[train_index[sample_i]]
        train_y[sample_i] = label_set[train_index[sample_i]]

    test_num = sample_num - train_num
    test_x = np.zeros((test_num, fea_num), dtype='float')
    test_y = np.zeros((test_num, 1), dtype='int')
    for sample_i in range(test_num):
        test_x[sample_i] = dataset[test_index[sample_i]]
        test_y[sample_i] = label_set[test_index[sample_i]]

    return train_x, train_y, test_x, test_y


class logi_regre(object):
    def __init__(self, train_x, train_y, lr, lamb_da):
        self.train_x = train_x    # The feature matrix of the training set
        self.train_y = train_y    # The label vector of the training set
        self.lr = lr              # The value of learning rate
        self.lamb_da = lamb_da     # The value of lam_da

    def fit_transform(self, w, b, iter_num, test_x, test_y):
        """
            Train the model and test it
        :param w: The w coefficient
        :param b: The b coefficient
        :param iter_num: The number of iterations
        :param test_x: The feature matrix of the test set
        :param test_y: The label vector of the test set
        :return: The accuracy of testing patients
        """
        accuracy = np.zeros((self.train_x.shape[0], 1))  # 100 trials
        for trial_i in range(self.train_x.shape[0]):
            for iter_i in range(iter_num):
                total_w = np.zeros((30, 1))
                total_b = 0
                for train_i in range(self.train_x.shape[1]):
                    inner_part = dot(w.T, self.train_x[trial_i, train_i].T) + b
                    exp_part = exp(inner_part)
                    total_w = total_w - \
                              self.train_y[trial_i, train_i] * \
                              expand_dims(self.train_x[trial_i, train_i].T, axis=1) + \
                              expand_dims(self.train_x[trial_i, train_i].T, axis=1) * \
                              exp_part / (1 + exp_part)
                    total_b = total_b - self.train_y[trial_i, train_i] + exp_part / (1 + exp_part)

                total_w = total_w + self.lamb_da * w
                w = w - self.lr * total_w
                b = b - self.lr * total_b

            accuracy_i = np.zeros(test_y.shape[:], dtype='int')
            for test_i in range(test_x.shape[1]):
                test_p = 1 / (1 + exp(- np.dot(w.T, test_x[trial_i, test_i].T) - b))
                if test_p >= 0.5:
                    predict_label = 0
                else:
                    predict_label = 1
                if predict_label == test_y[trial_i, test_i]:
                    accuracy_i[0, test_i] = 1
            accuracy[trial_i] = accuracy_i[0].mean()
        print("The accuracy of testing patients is %f" % (accuracy.mean()))

    def check_iterations(self, w, b, epsilon, eta, method, verbose=False):
        """
            Check how many iterations to converge
                :param w: The w coefficient
        :param b: The b coefficient
        :param epsilon: The value of epsilon
        :param eta: The value of eta1
        :param method: 'gradent descent', 'heavy ball', or 'Nesterov'
        :param verbose: "True" or "False" to print the situation
        :return: The average iterations for three different algorithms
        """
        iter_num = np.zeros((self.train_x.shape[0], 1))  # (100, 0)
        for trial_i in range(self.train_x.shape[0]):
            iter_i = 0
            while True:
                total_w = np.zeros((30, 1))
                total_b = 0
                total_wb = 0
                for train_i in range(self.train_x.shape[1]):
                    inner_part = dot(w.T, self.train_x[trial_i, train_i].T) + b
                    exp_part = exp(inner_part)

                    total_w = total_w - \
                              self.train_y[trial_i, train_i] * \
                              expand_dims(self.train_x[trial_i, train_i].T, axis=1) + \
                              expand_dims(self.train_x[trial_i, train_i].T, axis=1) * \
                              exp_part / (1 + exp_part)
                    total_b = total_b - self.train_y[trial_i, train_i] + exp_part / (1 + exp_part)
                    total_wb = total_wb + absolute(- self.train_y[trial_i, train_i] * inner_part +
                                                   log(1 + exp_part))

                total_w = total_w + self.lamb_da * w
                total_wb = total_wb + 0.5 * self.lamb_da * sum(square(w))
                if method == 'gradient descent':
                    w = w - self.lr * total_w
                    b = b - self.lr * total_b

                elif method == 'heavy ball':
                    if iter_i == 0:
                        w_1 = w
                        w = w - self.lr * total_w
                        b_1 = b
                        b = b - self.lr * total_b
                    else:
                        temp_w = w - w_1
                        w_1 = w
                        w = w - self.lr * total_w + eta * temp_w

                        temp_b = b - b_1
                        b_1 = b
                        b = b - self.lr * total_b + eta * temp_b

                elif method == 'Nesterov':
                    if iter_i == 0:
                        temp_w_y = - self.lr * total_w
                        temp_w = w + temp_w_y
                        w = temp_w + eta * temp_w_y

                        temp_b_y = - self.lr * total_b
                        temp_b = b + temp_b_y
                        b = temp_b + eta * temp_b_y
                    else:
                        temp_w_y = - self.lr * total_w + eta * temp_w_y
                        temp_w = w + temp_w_y
                        w = temp_w + eta * temp_w_y

                        temp_b_y = - self.lr * total_b + eta * temp_b_y
                        temp_b = b + temp_b_y
                        b = temp_b + eta * temp_b_y

                else:
                    print("Please input the correct method!")
                    return False

                iter_i += 1

                upper_part = sum(square(total_w)) + sum(square(total_b))
                lower_part = 1 + total_wb
                if upper_part / lower_part <= epsilon:
                    iter_num[trial_i] = iter_i
                    if verbose:
                        print("The %d/%d is finished!" % (trial_i+1, self.train_x.shape[0]))
                    break

        print("The average number of converging iterations is %f for the %s method."
              % (iter_num.mean(), method))

    def plot_rate_curve(self, total_iter, eta, trial_i):
        """
            Check how many iterations to converge
        :param total_iter: total iteration numbers
        :param eta: The value of eta1
        :param trial_i: The ith trial
        """
        GD_ratio = np.zeros((total_iter, 1))  # (100, 0)
        HB_ratio = np.zeros((total_iter, 1))  # (100, 0)
        NT_ratio = np.zeros((total_iter, 1))  # (100, 0)

        # Use the gradient descent method
        b = 0.05
        np.random.seed(1)
        w = np.random.normal(0, 0.5, size=(30, 1))
        for iter_i in range(total_iter):
            total_w = np.zeros((30, 1))
            total_b = 0
            total_wb = 0
            for train_i in range(self.train_x.shape[1]):
                inner_part = dot(w.T, self.train_x[trial_i, train_i].T) + b
                exp_part = exp(inner_part)

                total_w = total_w - \
                          self.train_y[trial_i, train_i] * \
                          expand_dims(self.train_x[trial_i, train_i].T, axis=1) + \
                          expand_dims(self.train_x[trial_i, train_i].T, axis=1) * \
                          exp_part / (1 + exp_part)
                total_b = total_b - self.train_y[trial_i, train_i] + exp_part / (1 + exp_part)
                total_wb = total_wb + absolute(- self.train_y[trial_i, train_i] * inner_part +
                                               log(1 + exp_part))

            total_w = total_w + self.lamb_da * w
            total_wb = total_wb + 0.5 * self.lamb_da * sum(square(w))

            w = w - self.lr * total_w
            b = b - self.lr * total_b

            upper_part = sum(np.square(total_w)) + np.sum(np.square(total_b))
            lower_part = 1 + total_wb

            GD_ratio[iter_i] = upper_part / lower_part

        # Use the heavy ball method
        b = 0.05
        np.random.seed(1)
        w = np.random.normal(0, 0.5, size=(30, 1))
        for iter_i in range(total_iter):
            total_w = np.zeros((30, 1))
            total_b = 0
            total_wb = 0
            for train_i in range(self.train_x.shape[1]):
                inner_part = dot(w.T, self.train_x[trial_i, train_i].T) + b
                exp_part = exp(inner_part)

                total_w = total_w - \
                          self.train_y[trial_i, train_i] * \
                          expand_dims(self.train_x[trial_i, train_i].T, axis=1) + \
                          expand_dims(self.train_x[trial_i, train_i].T, axis=1) * \
                          exp_part / (1 + exp_part)
                total_b = total_b - self.train_y[trial_i, train_i] + exp_part / (1 + exp_part)
                total_wb = total_wb + absolute(- self.train_y[trial_i, train_i] * inner_part +
                                               log(1 + exp_part))

            total_w = total_w + self.lamb_da * w
            total_wb = total_wb + 0.5 * self.lamb_da * sum(square(w))

            if iter_i == 0:
                w_1 = w
                w = w - self.lr * total_w
                b_1 = b
                b = b - self.lr * total_b
            else:
                temp_w = w - w_1
                w_1 = w
                w = w - self.lr * total_w + eta * temp_w

                temp_b = b - b_1
                b_1 = b
                b = b - self.lr * total_b + eta * temp_b

            upper_part = sum(square(total_w)) + sum(square(total_b))
            lower_part = 1 + total_wb
            HB_ratio[iter_i] = upper_part / lower_part

        # Use the Nesterov's method
        b = 0.05
        np.random.seed(1)
        w = np.random.normal(0, 0.5, size=(30, 1))
        for iter_i in range(total_iter):
            total_w = np.zeros((30, 1))
            total_b = 0
            total_wb = 0
            for train_i in range(self.train_x.shape[1]):
                inner_part = np.dot(w.T, self.train_x[trial_i, train_i].T) + b
                exp_part = exp(inner_part)

                total_w = total_w - \
                          self.train_y[trial_i, train_i] * \
                          expand_dims(self.train_x[trial_i, train_i].T, axis=1) + \
                          expand_dims(self.train_x[trial_i, train_i].T, axis=1) * \
                          exp_part / (1 + exp_part)
                total_b = total_b - self.train_y[trial_i, train_i] + exp_part / (1 + exp_part)
                total_wb = total_wb + absolute(- self.train_y[trial_i, train_i] * inner_part +
                                                  log(1 + exp_part))

            total_w = total_w + self.lamb_da * w
            total_wb = total_wb + 0.5 * self.lamb_da * sum(square(w))
            if iter_i == 0:
                temp_w_y = - self.lr * total_w
                temp_w = w + temp_w_y
                w = temp_w + eta * temp_w_y

                temp_b_y = - self.lr * total_b
                temp_b = b + temp_b_y
                b = temp_b + eta * temp_b_y
            else:
                temp_w_y = - self.lr * total_w + eta * temp_w_y
                temp_w = w + temp_w_y
                w = temp_w + eta * temp_w_y

                temp_b_y = - self.lr * total_b + eta * temp_b_y
                temp_b = b + temp_b_y
                b = temp_b + eta * temp_b_y

            upper_part = sum(square(total_w)) + sum(square(total_b))
            lower_part = 1 + total_wb
            NT_ratio[iter_i] = upper_part / lower_part

        """
        solid, dashed, dashdot, dotted
        red, green, blue, cyan, magenta, yellow
        """

        plt.figure()
        plt.plot(GD_ratio, linestyle='solid', color='green')
        plt.plot(HB_ratio, linestyle='dashed', color='red')
        plt.plot(NT_ratio, linestyle='dotted', color='blue')
        plt.title("The convergence curves of three methods")
        plt.legend(["gradident descent", "heavy ball", "Nesterov"], loc='upper right')
        plt.ylabel("The ratio")
        plt.xlabel("The ith iteration")
        plt.savefig("The convergence curves")
        plt.show()

        plt.figure()
        plt.plot(GD_ratio, linestyle='solid', color='green')
        plt.title("The convergence curve of gradient descent")
        plt.ylabel("The ratio")
        plt.xlabel("The ith iteration")
        plt.savefig("The convergence curve1")
        plt.show()

        plt.figure()
        plt.plot(HB_ratio, linestyle='solid', color='red')
        plt.title("The convergence curve of heavy ball")
        plt.ylabel("The ratio")
        plt.xlabel("The ith iteration")
        plt.savefig("The convergence curve2")
        plt.show()

        plt.figure()
        plt.plot(NT_ratio, linestyle='solid', color='blue')
        plt.title("The convergence curve of Nesterov")
        plt.ylabel("The ratio")
        plt.xlabel("The ith iteration")
        plt.savefig("The convergence curve3")
        plt.show()






        

        










