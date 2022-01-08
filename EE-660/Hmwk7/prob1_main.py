import sklearn

import numpy as np
import pandas as pd

from sklearn.ensemble import AdaBoostClassifier
from scipy.stats import multivariate_normal


def input_data(source_tr_file, source_te_file, l_target_tr_file,
               ul_target_tr_file, target_te_file):
    """
       Inputs the dataset.
    :param source_tr_file: source training data
    :param source_te_file: source test data
    :param l_target_tr_file: labeled target training data
    :param ul_target_tr_file: unlabeled target training data
    :param target_te_file: target test data
    :return: source_tr_X, source_tr_y, source_te_X, source_te_y,
    l_target_tr_X, l_target_tr_y, ul_target_tr_X, target_te_X, target_te_y
    """
    source_tr_frame = pd.read_csv(source_tr_file)
    source_te_frame = pd.read_csv(source_te_file)
    l_target_tr_frame = pd.read_csv(l_target_tr_file)
    ul_target_tr_frame = pd.read_csv(ul_target_tr_file)
    target_te_frame = pd.read_csv(target_te_file)

    return source_tr_frame.values[:, 0:2], source_tr_frame.values[:, 2], \
           source_te_frame.values[:, 0:2], source_te_frame.values[:, 2], \
           l_target_tr_frame.values[:, 0:2], l_target_tr_frame.values[:, 2], \
           ul_target_tr_frame.values[:, 0:2], \
           target_te_frame.values[:, 0:2], target_te_frame.values[:, 2]


def do_part_fg(gm_mean2, gm_covariance2, gm_mean1, gm_covariance1,
               source_tr_X, source_tr_y, l_target_tr_X, l_target_tr_y,
               target_te_X, target_te_y, mode):
    """
       For parts (f)-(g), you will use TL techniques on the TL problem.
    :param gm_mean2: mean vector for target data
    :param gm_covariance2: covariance matrix for target data
    :param gm_mean1: mean vector for source data
    :param gm_covariance1: covariance matrix for source data
    :param source_tr_X: feature matrix of source training data
    :param source_tr_y: label vector of source training data
    :param l_target_tr_X: feature matrix of labeled target training data
    :param l_target_tr_y: label vector of labeled target training data
    :param target_te_X:  feature matrix of target test data
    :param target_te_y:  label vector of target test data
    :param mode: two techniques in f: (g1) or (g2)
    """
    sample_weights = np.array([(multivariate_normal.pdf(x, mean=gm_mean2, cov=gm_covariance2)
                                / multivariate_normal.pdf(x, mean=gm_mean1, cov=gm_covariance1))
                               for x in source_tr_X])
    sample_weights = np.expand_dims(sample_weights, axis=1)
    wei_source_tr_X = np.multiply(np.repeat(sample_weights, repeats=1, axis=0), source_tr_X)
    # Part (g):
    union_tr_X = np.vstack((wei_source_tr_X, l_target_tr_X))
    union_tr_y = np.hstack((source_tr_y, l_target_tr_y))
    adb_model = AdaBoostClassifier()
    adb_model.fit(X=union_tr_X, y=union_tr_y)
    print("For the part" + mode + ", the classification accuracy on target test data is {:.4f}"
          .format(adb_model.score(X=target_te_X, y=target_te_y)))


def main():
    """
       The main function.
    """
    # For the part(a):
    print("My Sklearn version is {}.".format(sklearn.__version__))
    source_tr_X, source_tr_y, \
    source_te_X, source_te_y, \
    l_target_tr_X, l_target_tr_y, ul_target_tr_X,\
    target_te_X, target_te_y = \
        input_data(source_tr_file='Data/TL_data/data_source_train.csv',
                   source_te_file='Data/TL_data/data_source_test.csv',
                   l_target_tr_file='Data/TL_data/data_target_labeled.csv',
                   ul_target_tr_file='Data/TL_data/data_target_unlabeled.csv',
                   target_te_file='Data/TL_data/data_target_test.csv')
    """
    source_tr_X: (100, 2), source_tr_y: (100,)
    source_te_X: (100, 2), source_te_y.shape: (100,)
    l_target_tr_X.shape: (2, 2), l_target_tr_y: (2,)
    ul_target_tr_X: (98, 2)
    target_te_X.shape: (100, 2), target_te_y: (100,)
    """
    # Part (a):
    adb_model_a = AdaBoostClassifier()
    adb_model_a.fit(X=source_tr_X, y=source_tr_y)
    print("For the part (a), the classification accuracy on source test data is {:.4f}"
          .format(adb_model_a.score(X=source_te_X, y=source_te_y)))

    """
       For parts (b)-(d) below, I will use standard SL techniques but applied to the 
    TL problem (3 different approaches)
    """
    # Part (b):
    print("For the part (b), the classification accuracy on target test data is {:.4f}"
          .format(adb_model_a.score(X=target_te_X, y=target_te_y)))
    # Part (c):
    adb_model_c = AdaBoostClassifier()
    adb_model_c.fit(X=l_target_tr_X, y=l_target_tr_y)
    print("For the part (c), the classification accuracy on target test data is {:.4f}"
          .format(adb_model_c.score(X=target_te_X, y=target_te_y)))
    # Part (d):
    union_tr_X = np.vstack((source_tr_X, l_target_tr_X))
    union_tr_y = np.hstack((source_tr_y, l_target_tr_y))
    adb_model_d = AdaBoostClassifier()
    adb_model_d.fit(X=union_tr_X, y=union_tr_y)
    print("For the part (d), the classification accuracy on target test data is {:.4f}"
          .format(adb_model_d.score(X=target_te_X, y=target_te_y)))
    """
       For parts (f)-(g), you will use TL techniques on the TL problem.
    """
    print("")
    # Part (f):
    from sklearn.mixture import GaussianMixture
    # Part (f).(i):
    entire_tr_X = np.vstack((source_tr_X, l_target_tr_X, ul_target_tr_X))
    gm_i = GaussianMixture(n_components=2, random_state=660)
    gm_i.fit(X=entire_tr_X)
    gm_i_mean1, gm_i_mean2 = gm_i.means_[0], gm_i.means_[1]
    print("For the part(f).(i), gm_i_mean1, gm_i_mean2", gm_i_mean1, gm_i_mean2)
    gm_i_covariance1, gm_i_covariance2 = gm_i.covariances_[0], gm_i.covariances_[1]
    print("For the part(f).(i), gm_i_covariance1, gm_i_covariance2",
          gm_i_covariance1, gm_i_covariance2)
    # Part (f).(ii):
    entire_target_tr_X = np.vstack((l_target_tr_X, ul_target_tr_X))
    gm_ii1 = GaussianMixture(n_components=1, random_state=660).fit(X=source_tr_X)
    gm_ii_mean1 = np.squeeze(gm_ii1.means_, axis=0)
    gm_ii_covariance1 = np.squeeze(gm_ii1.covariances_, axis=0)
    gm_ii2 = GaussianMixture(n_components=1, random_state=660).fit(X=entire_target_tr_X)
    gm_ii_mean2 = np.squeeze(gm_ii2.means_, axis=0)
    gm_ii_covariance2 = np.squeeze(gm_ii2.covariances_, axis=0)
    print("For the part(f).(ii), gm_ii_mean1, gm_ii_mean2", gm_ii_mean1, gm_ii_mean2)
    print("For the part(f).(ii), gm_ii_covariance1, gm_ii_covariance2",
          gm_ii_covariance1, gm_ii_covariance2)

    do_part_fg(gm_mean2=gm_i_mean2, gm_covariance2=gm_i_covariance2,
               gm_mean1=gm_i_mean1, gm_covariance1=gm_i_covariance1,
               source_tr_X=source_tr_X, source_tr_y=source_tr_y,
               l_target_tr_X=l_target_tr_X, l_target_tr_y=l_target_tr_y,
               target_te_X=target_te_X, target_te_y=target_te_y, mode='(g1)')

    do_part_fg(gm_mean2=gm_ii_mean2, gm_covariance2=gm_ii_covariance2,
               gm_mean1=gm_ii_mean1, gm_covariance1=gm_ii_covariance1,
               source_tr_X=source_tr_X, source_tr_y=source_tr_y,
               l_target_tr_X=l_target_tr_X, l_target_tr_y=l_target_tr_y,
               target_te_X=target_te_X, target_te_y=target_te_y, mode='(g2)')

    return


if __name__ == '__main__':
    main()