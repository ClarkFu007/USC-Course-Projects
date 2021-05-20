import csv
import numpy as np
import matplotlib.pyplot as plt

from numpy import sum, multiply, square, sqrt


def input_data(datafile_w, data_m, data_n, lable_col):
    """
       Input the dataset.
    :param datafile_w: the location of the data file.
    :param data_m: the number of rows.
    :param data_n: the number of columns.
    :param lable_col: the column for the labels.
    :return: feature matrix X, label vector y
    """
    InputData = np.zeros((data_m, data_n), dtype='float')
    with open(datafile_w, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            data = [float(datum) for datum in row]
            InputData[i] = data
    # print("InputData.shape", InputData.shape)

    Data_X = InputData[0:data_m, 0:lable_col-1]  # Feature matrix X
    Data_y = InputData[0:data_m, lable_col-1]    # Label vector y
    Data_y = Data_y.astype(np.int) - 1
    Data_y = np.expand_dims(Data_y, axis=1)
    print(datafile_w[0:-3] + "shape", Data_X.shape)
    print(datafile_w[0:-3] + "shape", Data_y.shape)

    return Data_X, Data_y


def get_error_rate(data_y, predict_y, log_word=None, to_return=False):
    """
       Gets error rates between predicted labels and real labels.
    :param data_y: The real target set.
    :param predict_y: The predicted target set.
    :param log_word: Whether to print.
    :param to_return: Whether to return.
    :return: The value of error rate.
    """
    accuracy = np.zeros((data_y.shape[0], 1), dtype='int')
    accuracy[data_y == predict_y] = 1
    error_rate = 1 - np.average(accuracy)
    if to_return:
        return error_rate
    else:
        print("For {}, the error rate is {:4.3f}.".format(log_word, error_rate))


def plot_demo(error_rate_matrix, sgd_method=None):
    """
       Plot three required figures.
    :param error_rate_matrix: error rate matrix to be used.
    :param sgd_method: "SGD1" or "SGD2".
    Shows and saves three plots.
    """
    # Line types: solid, dashed, dashdot, dotted
    # Color types: red, green, blue, cyan, magenta, yellow
    plt.figure(1)
    plt.plot(error_rate_matrix[0], linestyle='solid', color='blue')
    plt.title("The curve of error rate vs. iteration for my first run in " + sgd_method)
    plt.ylabel("Error rate")
    plt.xlabel("The ith iteration")
    plt.tight_layout()
    plt.savefig("The plot i for " + sgd_method)
    plt.show()

    mean_error_rate_array = np.mean(error_rate_matrix, axis=0)
    std_error_rate_array = np.std(error_rate_matrix, axis=0)
    plt.figure(2)
    plt.plot(mean_error_rate_array, linestyle='solid', color='blue')
    plt.plot(std_error_rate_array, linestyle='solid', color='green')
    plt.title("The curve of mean and std vs. iteration over 10 runs in " + sgd_method)
    plt.legend(["mean values", "std values"], loc='upper right')
    plt.ylabel("Value")
    plt.xlabel("The ith iteration")
    plt.tight_layout()
    plt.savefig("The plot ii for " + sgd_method)
    plt.show()

    max_error_rate_array = np.max(error_rate_matrix, axis=0)
    min_error_rate_array = np.min(error_rate_matrix, axis=0)
    plt.figure(3)
    plt.plot(max_error_rate_array, linestyle='solid', color='blue')
    plt.plot(min_error_rate_array, linestyle='solid', color='green')
    plt.title("The curve of max and min error rate vs. iteration over 10 runs in " + sgd_method)
    plt.legend(["maximum", "minimum"], loc='upper right')
    plt.ylabel("Value")
    plt.xlabel("The ith iteration")
    plt.tight_layout()
    plt.savefig("The plot iii for " + sgd_method)
    plt.show()
