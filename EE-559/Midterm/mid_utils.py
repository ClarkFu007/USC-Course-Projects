import csv
import sklearn
import numpy as np
import matplotlib.pyplot as plt

from numpy import sum, multiply, square, sqrt
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures


def input_data(datafile_w, data_m, data_n, lable_col, unknown=False):
    """
       Input the dataset to finish our tasks.
    :param datafile_w: the location of the data file.
    :param data_m: the number of rows.
    :param data_n: the number of columns.
    :param lable_col: the column for the labels.
    :param unknown: whether the y vector is unknown or not.
    :return: feature matrix X, label vector y
    """
    InputData = np.zeros((data_m, data_n), dtype='float')
    with open(datafile_w, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            data = [float(datum) for datum in row]
            InputData[i] = data
    # print("InputData.shape", InputData.shape)
    if not unknown:
        Data_X = InputData[0:data_m, 0:lable_col - 1]  # Feature matrix X
        Data_y = InputData[0:data_m, lable_col - 1]  # Label vector y
        # Data_y = np.expand_dims(Data_y, axis=1)
        print(datafile_w[0:-3] + "shape", Data_X.shape)
        print(datafile_w[0:-3] + "shape", Data_y.shape)
        return Data_X, Data_y
    else:
        Data_X = InputData[0:data_m, 0:lable_col - 1]  # Feature matrix X
        print(datafile_w[0:-3] + "shape", Data_X.shape)
        return Data_X


def do_part_a(data_y, string_name):
    """
       Computes the mean-squared error (MSE) of a trivial system that
    always outputs the mean value.
    :param data_y: real value vector.
    :param string_name: name for printing.
    """
    mean_value = np.average(data_y)
    mean_vector = np.repeat(a=mean_value, repeats=data_y.shape[0], axis=0)
    mse_value = np.average(square(mean_vector - data_y))
    print("The MSE for {} is {:4.4f}.".format(string_name, mse_value))


def do_part_b(train_X, train_y, vali_X, vali_y, to_aug=True, to_return=False):
    """
       Runs MSE regression on the training data, and prints the resulting MSE on the
    training set and on the validation set. Also prints the final (optimal) weight values.
    :param train_X: nonaugmented feature matrix for training.
    :param train_y: real value vector fro training.
    :param vali_X: nonaugmented feature matrix for validation.
    :param vali_y: real value vector fro validation.
    :param to_aug: whether to use augmentation.
    :param to_return: whether to return results.
    :return: MSE of the validation data.
    """

    if to_aug:
        train_X = np.insert(train_X, 0, np.ones(train_X.shape[0]), axis=1)  # Augments the training data
        vali_X = np.insert(vali_X, 0, np.ones(vali_X.shape[0]), axis=1)     # Augments the validation
    mse_reg_model = LinearRegression(fit_intercept=False).fit(X=train_X, y=train_y)  # Does linear regression
    pred_train_y = mse_reg_model.predict(X=train_X)              # Predicts training data
    mse_train_y = np.average(np.square(pred_train_y - train_y))  # MSE for training
    pred_vali_y = mse_reg_model.predict(X=vali_X)                # Predicts validation data
    mse_vali_y = np.average(np.square(pred_vali_y - vali_y))     # MSE for validation

    if to_return:
        return mse_vali_y, mse_reg_model
    else:
        print("The MSE on the training set is %.4f." % (mse_train_y))
        print("The MSE on the validation set is %.4f." % (mse_vali_y))
        print("The coefficients of the trained model are", mse_reg_model.coef_)
        print("The intercept of the trained model is", mse_reg_model.intercept_)


def do_part_c(train_X, train_y, vali_X, vali_y, to_return=False):
    """
       Runs nonlinear MSE regression by using a transformation of feature space that is
    a polynomial of degree M. Uses model selection to optimize M with the provided
    training and validation sets.
       Prints the optimal value of M, the MSE on training and validation sets, and the
    final weight values.
    :param train_X: nonaugmented feature matrix for training.
    :param train_y: real value vector for training.
    :param vali_X: nonaugmented feature matrix for validation.
    :param vali_y: real value vector for validation.
    :param to_return: whether to return results.
    :return mse_reg_model: optimum model.
            target_M: M for optimum.
    """
    min_mse = 10
    target_M = 0
    for M in range(1, 20):
        poly_transformation = PolynomialFeatures(M)
        poly_train_X = poly_transformation.fit_transform(train_X)  # Nonlinear transformation on training
        poly_vali_X = poly_transformation.fit_transform(vali_X)    # Nonlinear transformation on validation
        current_mse, _ = do_part_b(train_X=poly_train_X, train_y=train_y,
                                   vali_X=poly_vali_X, vali_y=vali_y, to_aug=False, to_return=True)
        if min_mse > current_mse:
            min_mse = current_mse
            target_M = M

    print("The optimal value of M is ", target_M)
    poly_transformation = PolynomialFeatures(target_M)
    poly_train_X = poly_transformation.fit_transform(train_X)
    poly_vali_X = poly_transformation.fit_transform(vali_X)
    if to_return:
        _,  mse_reg_model = do_part_b(train_X=poly_train_X, train_y=train_y,
                                      vali_X=poly_vali_X, vali_y=vali_y, to_aug=False, to_return=True)
        return mse_reg_model, target_M
    else:
        do_part_b(train_X=poly_train_X, train_y=train_y, vali_X=poly_vali_X, vali_y=vali_y)


def do_part_d(train_X, train_y, vali_X, vali_y):
    """
       For visualization, plots the following, on a y vs. x_j plot, for the optimal linear model
    from (b), and for the optimal nonlinear model chosen in (c).
       Shows and saves the resulting pictures.
    :param train_X: nonaugmented feature matrix for training.
    :param train_y: real value vector fro training.
    :param vali_X: nonaugmented feature matrix for validation.
    :param vali_y: real value vector fo validation.
    """
    _,  mse_model = do_part_b(train_X=train_X, train_y=train_y,
                              vali_X=vali_X, vali_y=vali_y, to_return=True)
    opt_mse_model, target_M = do_part_c(train_X=train_X, train_y=train_y,
                                        vali_X=vali_X, vali_y=vali_y, to_return=True)

    x1, y1 = [], []
    x2, y2 = [], []
    for feat_i in range(train_X.shape[0]):
        if -0.1 <= train_X[feat_i][1] <= 0.1:
            x1.append(train_X[feat_i][0])
            y1.append(train_y[feat_i])
        if -0.1 <= train_X[feat_i][0] <= 0.1:
            x2.append(train_X[feat_i][1])
            y2.append(train_y[feat_i])

    # For j = 1
    part_d_plot(x=x1, y=y1, target_M=target_M, mse_model=mse_model,
                opt_mse_model=opt_mse_model, subpart='1')
    # For j = 2
    part_d_plot(x=x2, y=y2, target_M=target_M, mse_model=mse_model,
                opt_mse_model=opt_mse_model, subpart='2')


def part_d_plot(x, y, target_M, mse_model, opt_mse_model, subpart):
    """
       Gets the required plots in two situations j=1 or j=2.
    :param x: relevant feature vector list.
    :param y: relevant real values.
    :param target_M: value of the optimum M.
    :param mse_model: the original model.
    :param opt_mse_model: the optimum model without regularizaion.
    :param subpart: '1' or '2' to denote i or ii
    """
    if subpart == '1':
        pred_x1 = np.linspace(-1, 1, len(x)).reshape(-1, 1)
        pred_x2 = np.zeros(len(x)).reshape(-1, 1)
    elif subpart == '2':
        pred_x1 = np.zeros(len(x)).reshape(-1, 1)
        pred_x2 = np.linspace(-1, 1, len(x)).reshape(-1, 1)
    else:
        return None
    X = np.append(pred_x1, pred_x2, axis=1)  # Gets the fake feature matrix for the predicted curve
    poly_transformation = PolynomialFeatures(target_M)
    pred_X = poly_transformation.fit_transform(X)     # Nolinearly transform the fake feature matrix
    X = np.insert(X, 0, np.ones(X.shape[0]), axis=1)  # Augments the fake feature matrix
    pred_y = mse_model.predict(X)                # Baseline predicted curve
    opt_pred_y = opt_mse_model.predict(pred_X)   # Optimal predicted curve

    x, y = np.array(x), np.array(y)
    fig, (ax1, ax2) = plt.subplots(2, 1)
    fig.suptitle('The results on the y vs. x' + subpart + ' plot')
    ax1.scatter(x, y)
    if subpart == '1':
        ax1.plot(pred_x1, pred_y, color='green')
    else:
        ax1.plot(pred_x2, pred_y, color='green')
    # ax1.set_ylim(np.floor(min(y)), np.ceil(max(y)))
    ax1.set_ylabel('The result of (c)')
    ax2.scatter(x, y)
    if subpart == '1':
        ax2.plot(pred_x1, opt_pred_y, color='green')
    else:
        ax2.plot(pred_x2, opt_pred_y, color='green')
    # ax2.set_ylim(np.floor(min(y)) - 0.5, np.ceil(max(y)))
    ax2.set_ylabel('The result of (d)')
    # fig.tight_layout()
    plt.savefig("The plot ii for part-d-" + subpart)
    fig.show()


def do_part_f(train_X, train_y, vali_X, vali_y):
    """
       Runs Ridge Regression on the training data, and uses model selection to find the best
    values of the parameters M and lambda.
       Reports on the MSE on the training set and on the validation set for baseline values
    of M=1 and lambda=0, as well as for the optimal values M*, lambda* and relevant final
    weight values.
    :param train_X: nonaugmented feature matrix for training.
    :param train_y: real value vector for training.
    :param vali_X: nonaugmented feature matrix for validation.
    :param vali_y: real value vector for validation.
    :return target_M: M for optimum.
            vali_mse_matrix: matrix to draw plots.
            opt_ridge_model: optimum model.
    """

    # For the beseline values
    poly_transformation = PolynomialFeatures(1)
    poly_train_X = poly_transformation.fit_transform(train_X)
    poly_vali_X = poly_transformation.fit_transform(vali_X)
    mse_ridge_model = Ridge(alpha=0)
    mse_ridge_model.fit(X=poly_train_X, y=train_y)
    pred_tr_y = mse_ridge_model.predict(X=poly_train_X)
    baseline_tr_mse = np.average(np.square(pred_tr_y - train_y))
    print("For baseline hyperparameters, the MSE value for training is %.4f." % (baseline_tr_mse))
    pred_vali_y = mse_ridge_model.predict(X=poly_vali_X)
    baseline_val_mse = np.average(np.square(pred_vali_y - vali_y))
    print("For baseline hyperparameters, the MSE value for validation is %.4f." % (baseline_val_mse))

    min_mse = 10
    target_M = 0
    target_alpha = 0
    vali_mse_matrix = np.zeros((10, 108), dtype='float')
    for M in range(1, 11):
        current_alpha = 0.01
        cout_i = 0
        while True:
            poly_transformation = PolynomialFeatures(M)
            poly_train_X = poly_transformation.fit_transform(train_X)
            poly_vali_X = poly_transformation.fit_transform(vali_X)
            mse_ridge_model = Ridge(alpha=current_alpha)
            mse_ridge_model.fit(X=poly_train_X, y=train_y)
            pred_vali_y = mse_ridge_model.predict(X=poly_vali_X)
            current_vali_mse = np.average(np.square(pred_vali_y - vali_y))
            vali_mse_matrix[M - 1, cout_i] = current_vali_mse
            if min_mse > current_vali_mse:
                min_mse = current_vali_mse
                target_M, target_alpha = M, current_alpha
            current_alpha += 0.01
            cout_i += 1
            if 1.09 < current_alpha < 1.2:
                break

    poly_transformation = PolynomialFeatures(target_M)
    poly_train_X = poly_transformation.fit_transform(train_X)  # Nonlinear transformation on training
    poly_vali_X = poly_transformation.fit_transform(vali_X)    # Nonlinear transformation on validation
    opt_ridge_model = Ridge(alpha=target_alpha)                      # Does ridge regression
    opt_ridge_model.fit(X=poly_train_X, y=train_y)
    pred_train_y = opt_ridge_model.predict(X=poly_train_X)         # Predicts training data
    opt_train_mse = np.average(np.square(pred_train_y - train_y))  # MSE for training
    pred_vali_y = opt_ridge_model.predict(X=poly_vali_X)           # Predicts validation data
    opt_vali_mse = np.average(np.square(pred_vali_y - vali_y))     # MSE for validation
    print("The target M is {} and aplha is {}.".format(target_M, target_alpha))
    print("The optimum MSE for training is %.4f." % (opt_train_mse))
    print("The optimum MSE for validation is %.4f." % (opt_vali_mse))
    print("The final coefficients are ", opt_ridge_model.coef_)
    print("The final intercept is ", opt_ridge_model.intercept_)

    return target_M, vali_mse_matrix, opt_ridge_model


def part_f_plot(vali_mse_matrix, target_M):
    """
       Shows and saves on a validation-set-MSE vs. lambda plot, curves for each value of M that I
    tried, each curve labeled accroding to its value of M.
    :param vali_mse_matrix: matrix to draw plots.
    :param target_M: M for optimum.
    """
    for i in range(10):
        plt.figure(i)
        x = np.linspace(0.1, 1.1, 108)
        if i + 1 == target_M:
            plt.plot(x, vali_mse_matrix[i], linestyle='solid', color='green')
        else:
            plt.plot(x, vali_mse_matrix[i], linestyle='solid', color='blue')

        plt.title("The curves of validation-set-MSE vs. lambda for M = " + str(i + 1))
        plt.ylabel("MSE value")
        plt.xlabel("The value of lambda")
        plt.tight_layout()
        plt.savefig("validation-set-MSE " + str(i + 1))
        plt.show()


