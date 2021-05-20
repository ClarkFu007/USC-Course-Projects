import sklearn
import numpy as np

from sklearn.preprocessing import PolynomialFeatures

from mid_utils import input_data
from mid_utils import do_part_a, do_part_b
from mid_utils import do_part_c, do_part_d
from mid_utils import do_part_f, part_f_plot


def final_test(target_M, model, test_X, test_y, unknown_X, save_name):
    """
       Runs the best system on the test set and reports on the MSE.
    Then runs the system to predict output values on the unknown dataset
    and saves the output predicted values as a csv file.
    :param target_M: optimal M to do nolinear feature transformation.
    :param model: optimal model to do regression.
    :param test_X: feature matrix for test data.
    :param test_y: real values for test data.
    :param unknown_X: unknown feature matrix.
    :param save_name: the csv file name.
    """
    poly_transformation = PolynomialFeatures(target_M)
    poly_test_X = poly_transformation.fit_transform(test_X)
    pred_test_y = model.predict(X=poly_test_X)
    mse_test_y = np.average(np.square(pred_test_y - test_y))
    print("The MSE on the test set is %.4f." % mse_test_y)
    poly_unknown_X = poly_transformation.fit_transform(unknown_X)
    pred_unknown_y = model.predict(X=poly_unknown_X)
    np.savetxt(save_name, pred_unknown_y, delimiter=',')


def main():
    print("My Sklearn version is {}".format(sklearn.__version__))
    # Read the data from synthetic datasets.
    train_X, train_y = input_data(datafile_w='dataset1_train.csv', data_m=400, data_n=3, lable_col=3)
    vali_X, vali_y = input_data(datafile_w='dataset1_val.csv', data_m=200, data_n=3, lable_col=3)
    test_X, test_y = input_data(datafile_w='dataset1_test.csv', data_m=200, data_n=3, lable_col=3)
    unknown_X = input_data(datafile_w='dataset1_unknowns.csv', data_m=1000, data_n=2, lable_col=3, unknown=True)

    # Computes the MSE of a trivial system that always outputs the mean value.
    do_part_a(data_y=train_y, string_name="training")
    do_part_a(data_y=vali_y, string_name="validation")
    do_part_a(data_y=test_y, string_name="testing")
    # Runs MSE regression with the original feature space:
    do_part_b(train_X=train_X, train_y=train_y, vali_X=vali_X, vali_y=vali_y)
    # Runs nonlinear MSE regression by using a transformation of feature space:
    do_part_c(train_X=train_X, train_y=train_y, vali_X=vali_X, vali_y=vali_y)
    # Implements the visualization of parts (b) and (c):
    do_part_d(train_X=train_X, train_y=train_y, vali_X=vali_X, vali_y=vali_y)
    # Reports the optimal MST on test data and saves predicted values of the unknown data:
    opt_mse_reg_model, target_M = do_part_c(train_X=train_X, train_y=train_y,
                                            vali_X=vali_X, vali_y=vali_y, to_return=True)
    final_test(target_M=target_M, model=opt_mse_reg_model, test_X=test_X, test_y=test_y,
               unknown_X=unknown_X, save_name='EE559_midterm_3e.csv')

    # Runs Ridge Regression on training data, and finds optimal hyperparameter:
    target_M, vali_mse_matrix, opt_ridge_model = do_part_f(train_X=train_X,
                                                           train_y=train_y,
                                                           vali_X=vali_X,
                                                           vali_y=vali_y)
    # Implements the visualization of the part (f):
    part_f_plot(vali_mse_matrix=vali_mse_matrix, target_M=target_M)
    #  Reports the optimal MST on test data and saves predicted values of the unknown data:
    final_test(target_M=target_M, model=opt_ridge_model, test_X=test_X, test_y=test_y,
               unknown_X=unknown_X, save_name='EE559_midterm_3h.csv')


if __name__ == '__main__':
    main()







