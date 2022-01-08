import numpy as np

from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor


def get_performance(pred_val, pred_test, val_y, test_y, mode=None):
    """
       Gets the mean absolute errors of three set.
    :param pred_val: predictions of validation data
    :param pred_test: predictions of test data
    :param val_y: real values of validation data
    :param test_y: real values of test data
    :param mode: crucial words to print
    """
    assert pred_val.shape[0] == val_y.shape[0]
    mean_SE_val = np.sum(np.square(pred_val - val_y)) / pred_val.shape[0]
    print("The mean squared error (MSE) on validation for " + mode + " is %.4f." % mean_SE_val)
    assert pred_test.shape[0] == test_y.shape[0]
    mean_SE_test = np.sum(np.square(pred_test - test_y)) / pred_test.shape[0]
    print("The mean squared error (MSE) on test for " + mode + " is %.4f." % mean_SE_test)
    print()


def do_part_a(train_y, val_y, test_y):
    """
       For the baseline regression that simply outputs the
    mean value of the training set.
    :param train_y: real values of training data
    :param val_y: real values of validation data
    :param test_y: real values of validation data
    """
    pred_value = np.average(train_y)
    pred_val = np.full(val_y.shape[0], pred_value)
    pred_test = np.full(test_y.shape[0], pred_value)
    get_performance(pred_val=pred_val, pred_test=pred_test, val_y=val_y, test_y=test_y,
                    mode='baseline')


def do_part_b_select_model(log_lambda, reg_name):
    """
       Selects the l1 or l2 model for the part(b).
    :param log_lambda: log value of lambda
    :param reg_name: regularization name
    """
    if reg_name == 'l1':
        return Lasso(alpha=2 ** log_lambda)
    elif reg_name == 'l2':
        return Ridge(alpha=2 ** log_lambda)
    else:
        raise SystemExit("No such regularization name " + reg_name + "!")


def do_part_b_regularization(train_X, train_y, val_X, val_y, test_X, test_y, reg_name):
    """
       For three regularization techniques in the part(b).
    :param train_X: features of training data
    :param train_y: real values of training data
    :param val_X: features of validation data
    :param val_y: real values of validation data
    :param test_X: features of test data
    :param test_y: real values of validation data
    :param reg_name: regularization name
    """
    log_lambda_seq = np.arange(-10, 11, 1).astype(float)
    min_val_mse = np.inf
    opt_log_lambda = 0
    for log_lambda_i in range(log_lambda_seq.shape[0]):
        log_lambda = log_lambda_seq[log_lambda_i]
        model = do_part_b_select_model(log_lambda=log_lambda, reg_name=reg_name)
        model.fit(X=train_X, y=train_y)
        temp_pred_val = model.predict(X=val_X)
        temp_val_mse = np.average(np.square(temp_pred_val - val_y))
        if temp_val_mse < min_val_mse:
            opt_log_lambda = log_lambda
            min_val_mse = temp_val_mse
    print("The best lambda value for {} regularization is {}".format(reg_name, 2 ** opt_log_lambda))
    best_model = do_part_b_select_model(log_lambda=opt_log_lambda, reg_name=reg_name)
    best_model.fit(X=train_X, y=train_y)
    pred_val = best_model.predict(X=val_X)
    pred_test = best_model.predict(X=test_X)
    get_performance(pred_val=pred_val, pred_test=pred_test, val_y=val_y, test_y=test_y,
                    mode='linear regression with ' + reg_name + '-regularization')
    aug_feat_num = train_X.shape[1] + 1
    aug_weights = np.zeros(aug_feat_num, dtype='float')
    aug_weights[0] = best_model.intercept_
    aug_weights[1: aug_feat_num + 1] = best_model.coef_
    print("For the {} regularization, the final augmented weights are {}."
          .format(reg_name, aug_weights))
    print("For the {} regularization, the final l2 norm is {}."
          .format(reg_name, np.sqrt(np.sum(np.square(aug_weights)))))


def do_part_b(train_X, train_y, val_X, val_y, test_X, test_y):
    """
       Tries linear regression model with three regularization settings: no regularization,
    l1-regularization, and l2-regularization.
    :param train_X: features of training data
    :param train_y: real values of training data
    :param val_X: features of validation data
    :param val_y: real values of validation data
    :param test_X: features of test data
    :param test_y: real values of validation data
    """
    mse_LS_model = LinearRegression().fit(X=train_X, y=train_y)
    pred_val = mse_LS_model.predict(X=val_X)
    pred_test = mse_LS_model.predict(X=test_X)
    aug_feat_num = train_X.shape[1] + 1
    aug_weights = np.zeros(aug_feat_num, dtype='float')
    aug_weights[0] = mse_LS_model.intercept_
    aug_weights[1: aug_feat_num + 1] = mse_LS_model.coef_
    print("For the linear regression, the final augmented weights are {}."
          .format(aug_weights))
    print("For the linear regression, the final l2 norm is {}."
          .format(np.sqrt(np.sum(np.square(aug_weights)))))

    get_performance(pred_val=pred_val, pred_test=pred_test, val_y=val_y, test_y=test_y,
                    mode='linear regression without regularization')
    do_part_b_regularization(train_X=train_X, train_y=train_y, val_X=val_X, val_y=val_y,
                             test_X=test_X, test_y=test_y, reg_name='l1')
    do_part_b_regularization(train_X=train_X, train_y=train_y, val_X=val_X, val_y=val_y,
                             test_X=test_X, test_y=test_y, reg_name='l2')


def do_part_c(train_X, train_y, val_X, val_y, test_X, test_y):
    """
       Tries linear regression model with three regularization settings: no regularization,
    l1-regularization, and l2-regularization with standardizing data.
    :param train_X: features of training data
    :param train_y: real values of training data
    :param val_X: features of validation data
    :param val_y: real values of validation data
    :param test_X: features of test data
    :param test_y: real values of validation data
    """
    z_score_scaler = StandardScaler()
    z_score_scaler.fit(train_X)
    prepro_train_X = z_score_scaler.transform(train_X)
    prepro_val_X = z_score_scaler.transform(val_X)
    prepro_test_X = z_score_scaler.transform(test_X)
    do_part_b(train_X=prepro_train_X, train_y=train_y,
              val_X=prepro_val_X, val_y=val_y,
              test_X=prepro_test_X, test_y=test_y)


def do_part_d(train_X, train_y, val_X, val_y, test_X, test_y):
    """
       Tries CART.
    :param train_X: features of training data
    :param train_y: real values of training data
    :param val_X: features of validation data
    :param val_y: real values of validation data
    :param test_X: features of test data
    :param test_y: real values of validation data
    :return: optimum depth
    """
    depth_seq = np.arange(1, 11, 1).astype(int)
    min_val_mse = np.inf
    opt_depth = 0
    for depth_i in range(depth_seq.shape[0]):
        depth_value = depth_seq[depth_i]
        model = DecisionTreeRegressor(criterion='mse', max_depth=depth_value,
                                      max_features=None, random_state=0)
        model.fit(X=train_X, y=train_y)
        temp_pred_val = model.predict(X=val_X)
        temp_val_mse = np.average(np.square(temp_pred_val - val_y))
        if temp_val_mse < min_val_mse:
            opt_depth = depth_value
            min_val_mse = temp_val_mse
    print("The best depth value for CART is {}".format(opt_depth))
    best_model = DecisionTreeRegressor(criterion='mse', max_depth=opt_depth,
                                       max_features=None, random_state=0)
    best_model.fit(X=train_X, y=train_y)
    pred_val = best_model.predict(X=val_X)
    pred_test = best_model.predict(X=test_X)
    get_performance(pred_val=pred_val, pred_test=pred_test,
                    val_y=val_y, test_y=test_y, mode='CART')
    return opt_depth


def do_part_e(train_X, train_y, val_X, val_y, test_X, test_y, opt_depth):
    """
       Tries random forest.
    :param train_X: features of training data
    :param train_y: real values of training data
    :param val_X: features of validation data
    :param val_y: real values of validation data
    :param test_X: features of test data
    :param test_y: real values of validation data
    :param opt_depth: optimum depth value
    :return: optimum estimator-number
    """
    estimators_seq = np.arange(2, 31, 1).astype(int)
    min_val_mse = np.inf
    opt_estimators_num = 0
    for estimators_i in range(estimators_seq.shape[0]):
        estimators_value = estimators_seq[estimators_i]
        model = RandomForestRegressor(n_estimators=estimators_value, max_depth=opt_depth, random_state=0)
        model.fit(X=train_X, y=train_y)
        temp_pred_val = model.predict(X=val_X)
        temp_val_mse = np.average(np.square(temp_pred_val - val_y))
        if temp_val_mse < min_val_mse:
            opt_estimators_num = estimators_value
            min_val_mse = temp_val_mse
    print("The best estimator-num for random forest is {}".format(opt_estimators_num))
    best_model = RandomForestRegressor(n_estimators=opt_estimators_num, max_depth=opt_depth, random_state=0)
    best_model.fit(X=train_X, y=train_y)
    pred_val = best_model.predict(X=val_X)
    pred_test = best_model.predict(X=test_X)
    get_performance(pred_val=pred_val, pred_test=pred_test,
                    val_y=val_y, test_y=test_y, mode='random forest')
    return opt_estimators_num


def do_part_f(train_X, train_y, val_X, val_y, test_X, test_y, opt_depth, opt_estimators_num):
    """
       Tries Adaboost.
    :param train_X: features of training data
    :param train_y: real values of training data
    :param val_X: features of validation data
    :param val_y: real values of validation data
    :param test_X: features of test data
    :param test_y: real values of validation data
    :param opt_depth: optimum depth value
    :param opt_estimators_num: optimum estimator-number
    """
    lr_seq = np.arange(0.001, 0.103, 0.002).astype(float)
    min_val_mse = np.inf
    opt_lr = 0
    for lr_i in range(lr_seq.shape[0]):
        lr_value = lr_seq[lr_i]
        estimator = DecisionTreeRegressor(criterion='mse', max_depth=opt_depth, max_features=None, random_state=0)
        model = AdaBoostRegressor(base_estimator=estimator, n_estimators=opt_estimators_num,
                                  learning_rate=lr_value,
                                  random_state=0)
        model.fit(X=train_X, y=train_y)
        temp_pred_val = model.predict(X=val_X)
        temp_val_mse = np.average(np.square(temp_pred_val - val_y))
        if temp_val_mse < min_val_mse:
            opt_lr = lr_value
            min_val_mse = temp_val_mse
    print("The best learning rate for Adaboost is {}".format(opt_lr))
    estimator = DecisionTreeRegressor(criterion='mse', max_depth=opt_depth, max_features=None, random_state=0)
    best_model = AdaBoostRegressor(base_estimator=estimator, n_estimators=opt_estimators_num,
                                   learning_rate=opt_lr,
                                   random_state=0)
    best_model.fit(X=train_X, y=train_y)
    pred_val = best_model.predict(X=val_X)
    pred_test = best_model.predict(X=test_X)
    get_performance(pred_val=pred_val, pred_test=pred_test,
                    val_y=val_y, test_y=test_y, mode='ADABOOST')


def do_prob3():
    """
       Finishes the problem3.
    """
    dat = np.load('dataset/prob3/P3_data.npz')
    train_X, train_y = dat['X_train'], dat['y_train']  # (27435, 53), (27435,)
    val_X, val_y = dat['X_val'], dat['y_val']          # (13514, 53), (13514,)
    test_X, test_y = dat['X_test'], dat['y_test']      # (10044, 53), (10044,)
    do_part_a(train_y=train_y, val_y=val_y, test_y=test_y)
    do_part_b(train_X=train_X, train_y=train_y, val_X=val_X, val_y=val_y, test_X=test_X, test_y=test_y)
    do_part_c(train_X=train_X, train_y=train_y, val_X=val_X, val_y=val_y, test_X=test_X, test_y=test_y)
    opt_depth = do_part_d(train_X=train_X, train_y=train_y, val_X=val_X, val_y=val_y, test_X=test_X, test_y=test_y)
    opt_estimators_num = do_part_e(train_X=train_X, train_y=train_y, val_X=val_X, val_y=val_y,
                                   test_X=test_X, test_y=test_y, opt_depth=opt_depth)
    do_part_f(train_X=train_X, train_y=train_y, val_X=val_X, val_y=val_y,
              test_X=test_X, test_y=test_y, opt_depth=opt_depth,
              opt_estimators_num=opt_estimators_num)


def main():
    """
       The main function.
    """
    do_prob3()

    return


if __name__ == '__main__':
    main()
