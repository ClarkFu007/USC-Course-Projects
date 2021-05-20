import sklearn

from numpy import mean, repeat
from hw7_utils import input_data, get_MSE, get_results


def main():
    print("My Sklearn version is {}".format(sklearn.__version__))
    # For problem 1:
    train_X, train_y = input_data(datafile_w='H7_Dn_train.csv', data_m=500, data_n=3, label_col=3)
    test_X, test_y = input_data(datafile_w='H7_Dn_test.csv', data_m=300, data_n=3, label_col=3)
    # Part a: Calculate an approximate default choice for gamma.
    # Part b:
    # Compute the MSE of a trivial system always outputting the mean value on training data:
    te_num = test_X.shape[0]
    trivial_y_pred = repeat(mean(train_y), te_num)
    get_MSE(y_pred=trivial_y_pred, y_test=test_y, mode="trivial testing")

    # Part c: Choose the basis function centers as all the data points.
    get_results(experiment_num=5, train_X=train_X, train_y=train_y,
                test_X=test_X, test_y=test_y, select_method='all select')
    # Part d: Randomly choose the basis function centers, without replacement, from the training data.
    get_results(experiment_num=5, train_X=train_X, train_y=train_y,
                test_X=test_X, test_y=test_y, select_method='random select')
    # Part e: Use K-means clustering to choose basis function centers.
    get_results(experiment_num=5, train_X=train_X, train_y=train_y,
                test_X=test_X, test_y=test_y, select_method='k-means clustering')


if __name__ == '__main__':
    main()







