import numpy as np

from hw6_utils import input_data
from hw6_utils import finish_prob2
from hw6_utils import finish_prob3


def main():
    print("My Sklearn verion is {}".format(sklearn.__version__))

    """
       For problem 2: I will use the full dataset for training, and where requested,
    the classification accuracy is calculated on the (same) training dataset
    """
    train1_X = input_data(datafile_w='HW6_1_csv/train_x.csv', data_m=20, data_n=2, mode="feature")
    train1_y = input_data(datafile_w='HW6_1_csv/train_y.csv', data_m=20, data_n=1, mode="label")
    # Part a-c: For parts (a)-(c), load HW6_1, which is a linearly separable case.
    finish_prob2(part='a', train_X=train1_X, train_y=train1_y, C_value=1)
    finish_prob2(part='a', train_X=train1_X, train_y=train1_y, C_value=100)
    finish_prob2(part='abc', train_X=train1_X, train_y=train1_y, C_value=1000)
    # Part d-e: For parts (d)-(e), load HW6_2, which is not linearly separable.
    train2_X = input_data(datafile_w='HW6_2_csv/train_x.csv', data_m=20, data_n=2, mode="feature")
    train2_y = input_data(datafile_w='HW6_2_csv/train_y.csv', data_m=20, data_n=1, mode="label")
    finish_prob2(part='d', train_X=train2_X, train_y=train2_y, C_value=50)
    finish_prob2(part='d', train_X=train2_X, train_y=train2_y, C_value=5000)
    finish_prob2(part='e', train_X=train2_X, train_y=train2_y, gamma_value=10)
    finish_prob2(part='e', train_X=train2_X, train_y=train2_y, gamma_value=50)
    finish_prob2(part='e', train_X=train2_X, train_y=train2_y, gamma_value=500)

    """
       For problem 3: In this problem, I will use cross-validation for model (parameter) 
    selection, in order to more optimally design an SVM classifier. There is also a separate 
    test set that I can use.
    """
    train3_X = input_data(datafile_w='wine_csv/feature_train.csv',
                          data_m=89, data_n=13, mode="feature")[:, 0:2]
    train3_y = input_data(datafile_w='wine_csv/label_train.csv', data_m=89, data_n=1, mode="label")
    test3_X = input_data(datafile_w='wine_csv/feature_test.csv',
                         data_m=89, data_n=13, mode="feature")[:, 0:2]
    test3_y = input_data(datafile_w='wine_csv/label_test.csv', data_m=89, data_n=1, mode="label")
    # Part a: Report the average crossvalidation accuracy.
    finish_prob3(part='a', train_X=train3_X, train_y=train3_y, 
                 test_X=test3_X, test_y=test3_y, C_value=1, gamma_value=1)
    # Part b: use cross validation to find the best parameter set (model selection)
    finish_prob3(part='b', train_X=train3_X, train_y=train3_y,
                 test_X=test3_X, test_y=test3_y, 
                 C_value=np.logspace(start=-3, stop=3, endpoint=True), 
                 gamma_value=np.logspace(start=-3, stop=3, endpoint=True))
    # Part c-d: Repeat the cross validation procedure in (b) T=20 times (runs),
    # Use the full training set to train the final classifier using the best pair
    # of [γ, C] from (c) (ii) above
    finish_prob3(part='cd', train_X=train3_X, train_y=train3_y,
                 test_X=test3_X, test_y=test3_y, 
                 C_value=np.logspace(start=-3, stop=3, endpoint=True), 
                 gamma_value=np.logspace(start=-3, stop=3, endpoint=True))


if __name__ == '__main__':
    main()







