import numpy as np

from hw4_utils import input_data
from hw4_utils import get_error_rate
from hw4_utils import plot_demo
from perceptron_classifier import PerceptronModel


def finish_expeiment(train_X, train_y, test_X, test_y, sgd_method, experiment_num):
    """
       Finishes experiments in a specific stochastic gradient descent variant.
    :param train_X: feature matrix for training data.
    :param train_y: label vector for training data.
    :param test_X: feature matrix for test data.
    :param test_y: label vector for test data.
    :param sgd_method: "SGD1" or "SGD2".
    :param experiment_num: number of experiments.
    Outputs error rates for training and test and three plots.
    """
    my_perceptron = PerceptronModel(learning_rate=0.01, max_iter_num=10000, last_num=100)
    my_perceptron.fit(data_X=train_X, data_y=train_y, sgd_method=sgd_method)

    pred_tr_y = my_perceptron.transform(data_X=train_X, mode="test")
    get_error_rate(data_y=train_y, predict_y=pred_tr_y, log_word="training set for " + sgd_method,
                   to_return=False)
    pred_te_y = my_perceptron.transform(data_X=test_X, mode="test")
    get_error_rate(data_y=test_y, predict_y=pred_te_y, log_word="test set for " + sgd_method,
                   to_return=False)
    print("The number of iterations is", str(my_perceptron.total_iter_num) + ".")

    error_rate_matrix = np.zeros((experiment_num, int(my_perceptron.max_iter_num / experiment_num)))
    for experiment_i in range(experiment_num):
        my_perceptron = PerceptronModel(learning_rate=0.01, max_iter_num=10000, last_num=100)
        error_rate_matrix[experiment_i] = my_perceptron.fit(data_X=train_X, data_y=train_y,
                                                            sgd_method=sgd_method, to_return=True)

    plot_demo(error_rate_matrix=error_rate_matrix, sgd_method=sgd_method)


def main():
    # Read the data from two synthetic datasets.
    wine_tr_X, wine_tr_y = input_data(datafile_w='wine_train.csv', data_m=89, data_n=14, lable_col=14)
    wine_te_X, wine_te_y = input_data(datafile_w='wine_test.csv', data_m=89, data_n=14, lable_col=14)

    # Finishes experiments in two stochastic gradient descent variants.
    finish_expeiment(train_X=wine_tr_X, train_y=wine_tr_y, test_X=wine_te_X, test_y=wine_te_y,
                     sgd_method="SGD1", experiment_num=10)
    finish_expeiment(train_X=wine_tr_X, train_y=wine_tr_y, test_X=wine_te_X, test_y=wine_te_y,
                     sgd_method="SGD2", experiment_num=10)


if __name__ == '__main__':
    main()







