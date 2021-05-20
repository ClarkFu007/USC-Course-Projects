import sklearn
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.multiclass import OneVsRestClassifier

from hw5_utils import input_data, get_accuracy
from mse_classifier import MSE_Binary


def finish_part_c(train_X, train_y, test_X, test_y, data_type, seed_value,
                  verbose=True, to_return=False):
    """
       Finishes the part(c) of the homework5 of EE559.
    :param train_X: feature matrix for training data.
    :param train_y: label vector for training data.
    :param test_X: feature matrix for test data.
    :param test_y: label vector for test data.
    :param data_type: "unnormalized" or "standardized".
    :param seed_value: value to control starting weight vectors.
    :param verbose: whether to print information.
    :param to_return: whether to return accuracy value or not.
    Outputs the requried information.
    """
    perceptron_model = Perceptron(max_iter=10000, tol=None, random_state=0)
    np.random.seed(seed_value)
    coef = np.random.rand(len(np.unique(train_y)), train_X.shape[1])
    intercept = np.random.rand(len(np.unique(train_y)), 1)
    perceptron_OvR = OneVsRestClassifier(estimator=perceptron_model)
    perceptron_OvR.coef_ = coef            # Initialize coefficients with the specific seed value
    perceptron_OvR.intercept_ = intercept  # Initialize intercepts with the specific seed value
    perceptron_OvR.fit(train_X, train_y)
    train_y_pred = perceptron_OvR.predict(train_X)
    test_y_pred = perceptron_OvR.predict(test_X)
    if verbose:
        print("The weights for each feature for " + data_type + " data", perceptron_OvR.coef_)
        print("The constants for each feature for " + data_type + " data", perceptron_OvR.intercept_)

    if to_return:
        return get_accuracy(train_y, train_y_pred, log_word=data_type + " training data", to_return=to_return)
    else:
        get_accuracy(train_y, train_y_pred, log_word=data_type + " training data")
        get_accuracy(test_y, test_y_pred, log_word=data_type + " test data")
        print(" ")


def finish_part_d(train_X, train_y, test_X, test_y, data_type, experiment_num=100):
    """
       Finishes the part(d) of the homework5 of EE559.
    :param train_X: feature matrix for training data.
    :param train_y: label vector for training data.
    :param test_X: feature matrix for test data.
    :param test_y: label vector for test data.
    :param data_type: "unnormalized" or "standardized".
    :param experiment_num: number of experiments.

    Outputs the required information.
    """
    max_accuracy, target_seed = 0, 0
    for seed_i in range(experiment_num):
        current_accuracy = finish_part_c(train_X=train_X, train_y=train_y,
                                         test_X=test_X, test_y=test_y, data_type=data_type,
                                         seed_value=seed_i, verbose=False, to_return=True)
        if max_accuracy < current_accuracy:
            target_seed = seed_i
            max_accuracy = current_accuracy

    finish_part_c(train_X=train_X, train_y=train_y,
                  test_X=test_X, test_y=test_y,
                  data_type=data_type + " when the performance is the best among " + str(experiment_num) + " trials",
                  seed_value=target_seed)


def finish_part_g(train_X, train_y, test_X, test_y, data_type, to_return=False):
    """
       Finishes the part(g) of the homework5 of EE559.
    :param train_X: feature matrix for training data.
    :param train_y: label vector for training data.
    :param test_X: feature matrix for test data.
    :param test_y: label vector for test data.
    :param data_type: "unnormalized" or "standardized".
    :param to_return: whether to return accuracy value or not.
    Outputs the requried information.
    """
    pseudoinverse_model = MSE_Binary()
    pseudoinverse_OvR = OneVsRestClassifier(estimator=pseudoinverse_model).fit(train_X, train_y)
    train_y_pred = pseudoinverse_OvR.predict(train_X)
    test_y_pred = pseudoinverse_OvR.predict(test_X)

    if to_return:
        return get_accuracy(train_y, train_y_pred, log_word=data_type + " training data", to_return=to_return)
    else:
        get_accuracy(train_y, train_y_pred, log_word=data_type + " training data")
        get_accuracy(test_y, test_y_pred, log_word=data_type + " test data")
        print(" ")


def main():
    print("My Sklearn verion is {}".format(sklearn.__version__))

    # Read the data from two synthetic datasets.
    wine_tr_X, wine_tr_y = input_data(datafile_w='wine_train.csv', data_m=89, data_n=14, lable_col=14)
    wine_te_X, wine_te_y = input_data(datafile_w='wine_test.csv', data_m=89, data_n=14, lable_col=14)

    # Standardize the training data and test data
    z_score_scaler = StandardScaler()
    z_score_scaler.fit(wine_tr_X)
    std_wine_tr_X = z_score_scaler.transform(wine_tr_X)
    std_wine_te_X = z_score_scaler.transform(wine_te_X)
    print("The mean values for each feature of the training data", z_score_scaler.mean_)
    print("The standard deviation values for each feature of the training data", np.sqrt(z_score_scaler.var_))

    finish_part_c(train_X=wine_tr_X, train_y=wine_tr_y,
                  test_X=wine_te_X, test_y=wine_te_y, data_type="unnormalized", seed_value=0)
    finish_part_c(train_X=std_wine_tr_X, train_y=wine_tr_y,
                  test_X=std_wine_te_X, test_y=wine_te_y, data_type="standarized", seed_value=0)
    
    finish_part_d(train_X=wine_tr_X, train_y=wine_tr_y,
                  test_X=wine_te_X, test_y=wine_te_y, data_type="unnormalized", experiment_num=100)
    finish_part_d(train_X=std_wine_tr_X, train_y=wine_tr_y,
                  test_X=std_wine_te_X, test_y=wine_te_y, data_type="standarized", experiment_num=100)

    finish_part_g(train_X=wine_tr_X, train_y=wine_tr_y,
                  test_X=wine_te_X, test_y=wine_te_y, data_type="unnormalized", to_return=False)
    finish_part_g(train_X=std_wine_tr_X, train_y=wine_tr_y,
                  test_X=std_wine_te_X, test_y=wine_te_y, data_type="standarized", to_return=False)


if __name__ == '__main__':
    main()







