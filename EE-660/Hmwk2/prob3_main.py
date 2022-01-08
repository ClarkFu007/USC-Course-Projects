import sklearn
import random

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def input_data(tr_X_file, tr_y_file, te_X_file, te_y_file):
    """
       Inputs the dataset.
    :param tr_X_file: features of training data
    :param tr_y_file: labels of training data
    :param te_X_file: features of test data
    :param te_y_file: labels of test data
    :return: train_X, train_y, test_X, test_y
    """
    tr_X_data_frame = pd.read_csv(tr_X_file)
    tr_y_data_frame = pd.read_csv(tr_y_file, header=None)
    te_X_data_frame = pd.read_csv(te_X_file)
    te_y_data_frame = pd.read_csv(te_y_file, header=None)

    return tr_X_data_frame.values, np.squeeze(tr_y_data_frame.values), \
           te_X_data_frame.values, np.squeeze(te_y_data_frame.values)


def get_categories(train_y):
    """
       Gets the unique categories.
    :param train_y: labels of training data
    :return: the unique categories
    """
    return np.unique(train_y)


def get_err(pred_y, true_y):
    """
       Gets error rate.
    :param pred_y: predicted labels
    :param true_y: true labels
    :return: error rate
    """
    assert len(pred_y) == len(true_y)
    total_num = len(pred_y)
    err_num = 0
    for index_i in range(total_num):
        err_num += 1 if pred_y[index_i] != true_y[index_i] else 0

    return err_num / total_num


def get_label_withProb(pdf_seq, seed_value):
    """
       Gets the label with certain probability.
    :param pdf_seq: probability density function
    :param seed_value: value of seed
    :return: the label name with probability
    """
    random.seed(seed_value)
    x = random.uniform(0, 1)
    cumulative_probability = 0.0
    for item in pdf_seq:
        item_probability = pdf_seq[item]
        cumulative_probability += item_probability
        if x < cumulative_probability:
            break
        return item


def do_base_classification(train_y, test_y):
    """
       Implements the baseline classification.
    :param train_y: labels of training data
    :param test_y: labels of test data
    """
    labels = get_categories(train_y=train_y)
    label_num = {}  # Initialize an empty dictionary
    for index_i in range(len(labels)):
        label_num[labels[index_i]] = 0  # All labels' number is 0
    for index_i in range(len(train_y)):
        label_num[train_y[index_i]] += 1.0
    most_label_num = 0
    for label_i in label_num:
        if most_label_num < label_num[label_i]:
            most_label = label_i
            most_label_num = label_num[label_i]
        label_num[label_i] = label_num[label_i] / len(train_y)

    seed_value = 0
    err_train, err_test = np.zeros(10), np.zeros(10)
    for exp_i in range(10):
        pred_train_y = []
        for index_i in range(len(train_y)):
            pred_train_y.append(get_label_withProb(pdf_seq=label_num, seed_value=seed_value))
            seed_value += 1
        err_train[exp_i] = get_err(pred_y=pred_train_y, true_y=train_y.tolist())
        pred_test_y = []
        for index_i in range(len(test_y)):
            pred_test_y.append(get_label_withProb(pdf_seq=label_num, seed_value=seed_value))
            seed_value += 1
        err_test[exp_i] = get_err(pred_y=pred_test_y, true_y=test_y.tolist())

    print("For (i), the mean of the percent classification error on training is {:.4f}"
          .format(np.mean(err_train)))
    print("For (i), the standard deviation of the percent classification error on training is {:.4f}"
          .format(np.std(err_train)))
    print("For (i), the mean of the percent classification error on test is {:.4f}"
          .format(np.mean(err_test)))
    print("For (i), the standard deviation of the percent classification error on test is {:.4f}"
          .format(np.std(err_test)))

    print("For (ii), the percent classification error on training is {:.4f}"
          .format(get_err(pred_y=[most_label] * len(train_y), true_y=train_y.tolist())))
    print("For (ii), the percent classification error on test is {:.4f}"
          .format(get_err(pred_y=[most_label] * len(test_y), true_y=test_y.tolist())))


def do_rf_classification(B_total, train_X, train_y, test_X, test_y,
                         bag_size, max_depth, max_features):
    """
       Implements the random forest experiments under certain conditions.
    :param B_total: the total number of B
    :param train_X: features of training data
    :param train_y: labels of training data
    :param test_X: features of test data
    :param test_y: labels of test data
    :param bag_size: the friction of the bag
    :param max_depth: the maximum number of depth
    :param max_features: the maximum number of features
    """
    tr_mean_err, tr_std_err = np.zeros(B_total, dtype='float'), np.zeros(B_total, dtype='float')
    te_mean_err, te_std_err = np.zeros(B_total, dtype='float'), np.zeros(B_total, dtype='float')

    for B_value in range(1, B_total + 1):
        train_err, test_err = np.zeros(10, dtype='float'), np.zeros(10, dtype='float')
        for exp_i in range(10):
            train_bag_X, _, train_bag_y, _ = train_test_split(train_X, train_y, test_size=bag_size,
                                                              random_state=B_value+B_value*exp_i)
            rf_model = RandomForestClassifier(n_estimators=B_value, criterion='entropy', max_depth=max_depth,
                                              bootstrap=True, max_features=max_features,
                                              random_state=B_value+B_value*exp_i)
            rf_model.fit(X=train_bag_X, y=train_bag_y)
            pred_tr_y = rf_model.predict(X=train_X)
            train_err[exp_i] = 1 - accuracy_score(y_true=train_y, y_pred=pred_tr_y)
            pred_te_y = rf_model.predict(X=test_X)
            test_err[exp_i] = 1 - accuracy_score(y_true=test_y, y_pred=pred_te_y)

        tr_mean_err[B_value - 1], tr_std_err[B_value - 1] = np.mean(train_err), np.std(train_err)
        te_mean_err[B_value - 1], te_std_err[B_value - 1] = np.mean(test_err), np.std(test_err)

    print("When B={}, bag_size = {:.2f}, max_depth = {}, max_features={}, "
          "the minimum error rate is {:.4f} and its corresponding standard deviation is {:.4f}.".
          format(B_total, bag_size, max_depth, max_features, np.min(te_mean_err),
                 te_std_err[np.argmin(te_mean_err)]))

    B = np.arange(1, B_total + 1, 1)
    plt.figure(0)
    plt.plot(B, tr_mean_err, 'b', label='Training')
    plt.plot(B, te_mean_err, 'g', label='Test')
    plt.legend()
    plt.title('The plot of mean values of error rates')
    plt.ylabel('Mean values of error rates')
    plt.xlabel('The value of B')
    plt.tight_layout()
    plt.savefig("The plot of mean error rates_" + str(B_total) + "_" + str(bag_size) + "_"
                + str(max_depth) + "_" + str(max_features) + ".png")
    plt.show()

    plt.figure(1)
    plt.plot(B, tr_std_err, 'b', label='Training')
    plt.plot(B, te_std_err, 'g', label='Test')
    plt.legend()
    plt.title('The plot of standard deviation of error rates')
    plt.ylabel('Standard deviation of error rates')
    plt.xlabel('The value of B')
    plt.tight_layout()
    plt.savefig("The plot of sd error rates_" + str(B_total) + "_" + str(bag_size) + "_"
                + str(max_depth) + "_" + str(max_features) + ".png")
    plt.show()


def main():
    """
       The main function.
    """
    print("My Sklearn version is {}.".format(sklearn.__version__))
    train_X, train_y, test_X, test_y = input_data(tr_X_file='x_train.csv', tr_y_file='y_train.csv',
                                                  te_X_file='x_test.csv', te_y_file='y_test.csv')

    print("train_X", train_X.shape)
    print("train_y", train_y.shape)
    print("test_X", test_X.shape)
    print("test_y", test_y.shape)

    # Do the part(a)
    do_base_classification(train_y=train_y, test_y=test_y)
    print(" ")
    # Do the part(b).i
    do_rf_classification(B_total=30, train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y,
                         bag_size=0.5, max_depth=5, max_features=3)
    print(" ")
    # Do the part(b).ii
    do_rf_classification(B_total=100, train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y,
                         bag_size=0.5, max_depth=5, max_features=3)
    print(" ")
    # Do the part(b).iii
    do_rf_classification(B_total=30, train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y,
                         bag_size=1/3.0, max_depth=5, max_features=3)
    do_rf_classification(B_total=30, train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y,
                         bag_size=0.5, max_depth=5, max_features=3)
    do_rf_classification(B_total=30, train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y,
                         bag_size=2/3.0, max_depth=5, max_features=3)

    do_rf_classification(B_total=30, train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y,
                         bag_size=0.5, max_depth=1, max_features=3)
    do_rf_classification(B_total=30, train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y,
                         bag_size=0.5, max_depth=5, max_features=3)
    do_rf_classification(B_total=30, train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y,
                         bag_size=0.5, max_depth=None, max_features=3)

    do_rf_classification(B_total=30, train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y,
                         bag_size=0.5, max_depth=5, max_features=1)
    do_rf_classification(B_total=30, train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y,
                         bag_size=0.5, max_depth=5, max_features=3)
    do_rf_classification(B_total=30, train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y,
                         bag_size=0.5, max_depth=5, max_features=8)

    return


if __name__ == '__main__':
    main()