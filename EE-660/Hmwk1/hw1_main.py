import numpy
import numpy as np
import sklearn

from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.model_selection import KFold

from hw1_utils import display


def get_MSE(pred_y, true_y):
    """
       Gets MSE.
    :param pred_y: predicted y values.
    :param true_y: real y values.
    :return: mse.
    """
    return np.average(np.square(pred_y - true_y))


def select_model(reg_name, log_lambda):
    """
       Selects the specific model.
    :param reg_name: regression name.
    :param log_lambda: value of log lambda.
    :return:
    """
    if reg_name == 'l1':
        return Lasso(alpha=2 ** log_lambda)
    elif reg_name == 'l2':
        return Ridge(alpha=2 ** log_lambda)
    else:
        raise SystemExit("No such model name!")


def get_results(model, train_X, train_y, test_X, test_y, reg_name, dataset_name, do_display):
    """
       Gets performance.
    :param model: the trained model.
    :param train_X: training data.
    :param train_y: training labels.
    :param test_X: test data.
    :param test_y: test labels.
    :param reg_name: regression name.
    :param dataset_name: dataset name.
    :param do_display: whether to display.
    """
    model.fit(X=train_X, y=train_y)  # Trains the model with all training data
    pred_train_y = model.predict(X=train_X)  # Predicts the training data
    mse_train_y = get_MSE(pred_y=pred_train_y, true_y=train_y)  # MSE for training data
    print("For the {} regularization of {}, the MSE on train is {}."
          .format(reg_name, dataset_name, mse_train_y))
    pred_test_y = model.predict(X=test_X)  # Predicts test data
    mse_test_y = get_MSE(pred_y=pred_test_y, true_y=test_y)  # MSE for test data
    print("For the {} regularization of {}, the MSE on test is {}."
          .format(reg_name, dataset_name, mse_test_y))

    aug_feat_num = train_X.shape[1] + 1
    aug_weights = np.zeros(aug_feat_num)
    aug_weights[0] = model.intercept_
    aug_weights[1: aug_feat_num + 1] = model.coef_
    print("For the {} regularization of {}, the final augmented weights are {}."
          .format(reg_name, dataset_name, aug_weights))
    print("For the {} regularization of {}, the l1 norm of the final augmented weights is {}."
          .format(reg_name, dataset_name, np.sum(np.absolute(aug_weights))))
    print("For the {} regularization of {}, the l2 norm of the final augmented weights is {}."
          .format(reg_name, dataset_name, np.sqrt(np.sum(np.square(aug_weights)))))
    print("For the {} regularization of {}, the sparsity of the final augmented weights is {}."
          .format(reg_name, dataset_name, aug_feat_num - np.count_nonzero(aug_weights)))
    print()

    aug_train_X = np.concatenate((np.ones((len(train_X), 1)), train_X), axis=1)
    if (reg_name == 'l1' or reg_name == 'l2') and do_display:
        if dataset_name == 'dataset4':
            display(w=aug_weights.tolist(), Xtest=aug_train_X, Ytest=train_y,
                    norm=reg_name, saved_name=dataset_name+reg_name,
                    w1_range=(-15.0, 12.0, 500), w2_range=(-10.0, 25.0, 500))
        elif dataset_name == 'dataset7':
            display(w=aug_weights.tolist(), Xtest=aug_train_X, Ytest=train_y,
                    norm=reg_name, saved_name=dataset_name + reg_name,
                    w1_range=(-5.0, 10.0, 500), w2_range=(-10.0, 5.0, 500))
        else:
            display(w=aug_weights.tolist(), Xtest=aug_train_X, Ytest=train_y,
                    norm=reg_name, saved_name=dataset_name + reg_name)


def do_part_LS(dataset_name, dim, train_num, do_display):
    """
        Finishes the least-square regression.
    :param dataset_name: the name of the dataset.
    :param dim: feature dimension.
    :param train_num: the number of training data.
    :param do_display: whether to display.
    """
    filename = 'hmwk1_p2_material/' + dataset_name + '_dim' + str(dim) \
               + '_Ntr' + str(train_num) + '.npz'
    dataset = np.load(filename)
    train_X, train_y, test_X, test_y = dataset['X_train'], dataset['y_train'], \
                                       dataset['X_test'], dataset['y_test']
    # print("Before augmentation, train_X.shape", train_X.shape)
    # print("train_y.shape", train_y.shape)
    # print("Before augmentation,test_X.shape", test_X.shape)
    # print("test_y.shape", test_y.shape)

    mse_LS_model = LinearRegression().fit(X=train_X, y=train_y)  # Does least square regression
    get_results(model=mse_LS_model, train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y,
                reg_name='no', dataset_name=dataset_name, do_display=do_display)


def do_part_rest(dataset_name, dim, train_num, reg_name, do_display):
    """
       Finishes the rest parts.
    :param dataset_name: the name of the dataset.
    :param dim: feature dimension.
    :param train_num: the number of training data.
    :param reg_name: the regression name.
    :param do_display: whether to display.
    """
    filename = 'hmwk1_p2_material/' + dataset_name + '_dim' + str(dim) + '_Ntr' + str(train_num) + '.npz'
    dataset = np.load(filename)
    train_X, train_y, test_X, test_y = dataset['X_train'], dataset['y_train'], \
                                       dataset['X_test'], dataset['y_test']
    #print("Before augmentation, train_X.shape", train_X.shape)
    #print("train_y.shape", train_y.shape)
    #print("Before augmentation,test_X.shape", test_X.shape)
    #print("test_y.shape", test_y.shape)

    fold_num = 5
    stfied_k_fold = KFold(n_splits=fold_num, shuffle=True, random_state=660)
    k_fold_tr_X, k_fold_tr_y = [], []
    k_fold_te_X, k_fold_te_y = [], []
    for train_index, test_index in stfied_k_fold.split(X=train_X, y=train_y):
        k_fold_tr_X.append(train_X[train_index])
        k_fold_tr_y.append(train_y[train_index])
        k_fold_te_X.append(train_X[test_index])
        k_fold_te_y.append(train_y[test_index])

    lambda_num = int((10 - (-10)) / 0.5 + 1)
    cross_vali_acc = np.zeros((fold_num, lambda_num), dtype='float')
    for fold_i in range(fold_num):
        lambda_index, log_lambda = 0, -10
        while log_lambda <= 10:
            mse_model = select_model(reg_name=reg_name, log_lambda=log_lambda)
            mse_model.fit(X=k_fold_tr_X[fold_i], y=k_fold_tr_y[fold_i])  # Trains the model
            pred_vali_y = mse_model.predict(X=k_fold_te_X[fold_i])       # Predicts validation data
            cross_vali_acc[fold_i, lambda_index] = get_MSE(pred_y=pred_vali_y, true_y=k_fold_te_y[fold_i])

            lambda_index += 1
            log_lambda += 0.5

    mean_vali_acc = np.average(cross_vali_acc, axis=0)
    std_vali_acc = np.std(cross_vali_acc, axis=0)
    target_index = numpy.argmin(mean_vali_acc)
    target_log_lambda = -10 + 0.5 * target_index

    print("For the {} regularization of {}, the mean of MST is {}."
          .format(reg_name, dataset_name, mean_vali_acc[target_index]))
    print("For the {} regularization of {}, the standard deviation of MST is {}."
          .format(reg_name, dataset_name, std_vali_acc[target_index]))
    print("For the {} regularization of {}, the best log(2, lambda) is {}."
          .format(reg_name, dataset_name, target_log_lambda))

    mse_model = select_model(reg_name=reg_name, log_lambda=target_log_lambda)
    get_results(model=mse_model, train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y,
                reg_name=reg_name, dataset_name=dataset_name, do_display=do_display)


def do_part_a_i(dataset_name, dim, train_num, do_display=False):
    """
       Finishes the part (a) i.
    :param dataset_name: the name of the dataset.
    :param dim: feature dimension.
    :param train_num: the number of training data.
    :param do_display: whether to display.
    """
    do_part_LS(dataset_name=dataset_name, dim=dim, train_num=train_num, do_display=False)
    do_part_rest(dataset_name=dataset_name, dim=dim, train_num=train_num, reg_name='l1', do_display=do_display)
    do_part_rest(dataset_name=dataset_name, dim=dim, train_num=train_num, reg_name='l2', do_display=do_display)


def main():
    print("My Sklearn version is {}.".format(sklearn.__version__))
    do_part_a_i(dataset_name="dataset1", dim=9, train_num=10)
    do_part_a_i(dataset_name="dataset2", dim=9, train_num=100)
    do_part_a_i(dataset_name="dataset3", dim=9, train_num=1000)
    do_part_a_i(dataset_name="dataset4", dim=2, train_num=10, do_display=True)
    do_part_a_i(dataset_name="dataset5", dim=2, train_num=30, do_display=True)
    do_part_a_i(dataset_name="dataset6", dim=2, train_num=100, do_display=True)
    do_part_a_i(dataset_name="dataset7", dim=2, train_num=10, do_display=True)
    do_part_a_i(dataset_name="dataset8", dim=2, train_num=30, do_display=True)
    do_part_a_i(dataset_name="dataset9", dim=2, train_num=100, do_display=True)

    return


if __name__ == '__main__':
    main()