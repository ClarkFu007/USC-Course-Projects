import pickle

import numpy as np
import sklearn

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import roc_auc_score, accuracy_score
from sklearn.base import clone
from sklearn.utils.validation import check_array
from utils import save_model


class TrAdaBoost(object):
    """
    EE660
    Python implementation of TrAdaBoost
    Adapted from the following sources:
    https://github.com/loyalzc/transfer_learning
    https://github.com/surajiyer/Transfer-learning-with-TrAdaBoost
    """
    def __init__(self, N=10, base_estimator=DecisionTreeClassifier(), score=roc_auc_score):
        self.N = N
        self.base_estimator = base_estimator
        self.score = score
        self.beta_all = None
        self.estimators = []

    def _calculate_weights(self, weights):
        weights = weights.ravel()
        total = np.sum(weights)
        print(total, np.min(weights), np.max(weights))
        return np.asarray(weights / total, order='C')

    def _calculate_error_rate(self, y_true, y_pred, weight):
        weight = weight.ravel()
        total = np.sum(weight)
        print(total, np.min(weight), np.max(weight))
        return np.sum(weight / total * np.abs(y_true - y_pred))

    def fit(self, source, target, source_label, target_label):
        source_shape = source.shape[0]
        target_shape = target.shape[0]
        trans_data = np.concatenate((source, target), axis=0)
        trans_label = np.concatenate((source_label, target_label), axis=0)
        weights_source = np.ones([source_shape, 1]) / source_shape
        weights_target = np.ones([target_shape, 1]) / target_shape
        weights = np.concatenate((weights_source, weights_target), axis=0)

        bata = 1 / (1 + np.sqrt(2 * np.log(source_shape) / self.N))
        self.beta_all = np.zeros([1, self.N])
        result_label = np.ones([source_shape + target_shape, self.N])

        trans_data = np.asarray(trans_data, order='C')
        trans_label = np.asarray(trans_label, order='C')

        best_round = 0
        score = 0
        flag = 0

        for i in range(self.N):
            P = self._calculate_weights(weights)
            est = clone(self.base_estimator).fit(trans_data, trans_label, sample_weight=P.ravel())
            self.estimators.append(est)
            y_preds = est.predict(trans_data)
            result_label[:, i] = y_preds

            y_target_pred = est.predict(target)
            error_rate = self._calculate_error_rate(target_label, y_target_pred,
                                                    weights[source_shape:source_shape + target_shape, :])

            if error_rate >= 0.5 or error_rate == 0:
                self.N = i
                print('early stop! due to error_rate=%.2f' % error_rate)
                break

            self.beta_all[0, i] = error_rate / (1 - error_rate)

            for j in range(target_shape):
                weights[source_shape + j] = weights[source_shape + j] * \
                                            np.power(self.beta_all[0, i],
                                                     (-np.abs(result_label[source_shape + j, i] - target_label[j])))

            for j in range(source_shape):
                weights[j] = weights[j] * np.power(bata, np.abs(result_label[j, i] - source_label[j]))

            tp = self.score(target_label, y_target_pred)
            print('The ' + str(i) + ' rounds score is ' + str(tp))

    def _predict_one(self, x):
        """
        Output the hypothesis for a single instance
        :param x: array-like
            target label of a single instance from each iteration in order
        :return: 0 or 1
        """
        x, N = check_array(x, ensure_2d=False), self.N
        # replace 0 by 1 to avoid zero division and remove it from the product
        beta = [self.beta_all[0, t] if self.beta_all[0, t] != 0 else 1 for t in range(int(np.ceil(N / 2)), N)]
        cond = np.prod([b ** -x for b in beta]) >= np.prod([b ** -0.5 for b in beta])
        return int(cond)

    def predict(self, x_test):
        y_pred_list = np.array([est.predict(x_test) for est in self.estimators]).T
        y_pred = np.array(list(map(self._predict_one, y_pred_list)))
        return y_pred


def do_tl_experiments(source_X, source_y, target_tr_X, target_tr_y, target_te_X, target_te_y,
                      label_name, split_name):
    """
       Implements experiments based on transfer learning.
    :param source_X: feature matrix for source
    :param source_y: label vector for source
    :param target_tr_X: feature matrix for target training
    :param target_tr_y: label vector for target training
    :param target_te_X: feature matrix for target test
    :param target_te_y: label vector for target test
    :param label_name: label name to save models
    :param split_name: split name to save models
    """
    base_estimator = DecisionTreeClassifier(max_depth=1)
    clf = TrAdaBoost(N=3, base_estimator=base_estimator, score=accuracy_score)
    clf.fit(source=source_X, target=target_tr_X, source_label=source_y, target_label=target_tr_y)
    ys_pred = clf.predict(source_X)
    yt_pred = clf.predict(target_tr_X)
    yt_test_pred = clf.predict(target_te_X)

    print("source_X", source_X.shape)
    print("target_tr_X", target_tr_X.shape)
    print("target_te_X", target_te_X.shape)
    print('TrAdaBoost: train acc:', accuracy_score(source_y, ys_pred))
    print('TrAdaBoost: target acc:', accuracy_score(target_tr_y, yt_pred))
    print('TrAdaBoost: target_test acc:', accuracy_score(target_te_y, yt_test_pred))
    save_model(filename='TrAdaBoost ' + label_name + split_name, model=clf)

    baseline = AdaBoostClassifier(base_estimator=base_estimator, n_estimators=3)
    baseline.fit(source_X, source_y)
    print('AdaBoost: train acc:', accuracy_score(source_y, baseline.predict(source_X)))
    print('AdaBoost: target acc:', accuracy_score(target_tr_y, baseline.predict(target_tr_X)))
    print('AdaBoost: target_test acc:', accuracy_score(target_te_y, baseline.predict(target_te_X)))
    save_model(filename='AdaBoost baseline ' + label_name + split_name, model=baseline)


def get_tl_results(source_X, source_y, target_tr_X, target_tr_y, target_te_X, target_te_y,
                   label_name, split_name):
    """
       Gets results of experiments on transfer learning.
    :param source_X: feature matrix for source
    :param source_y: label vector for source
    :param target_tr_X: feature matrix for target training
    :param target_tr_y: label vector for target training
    :param target_te_X: feature matrix for target test
    :param target_te_y: label vector for target test
    :param label_name: label name to save models
    :param split_name: split name to save models
    """
    tradb_filename = 'saved_models/tl/TrAdaBoost ' + str(label_name) + str(split_name) + '.pkl'
    with open(tradb_filename, 'rb') as tradb_pickle_file:
        tradb_model = pickle.load(tradb_pickle_file)
    tradb_pickle_file.close()

    ys_pred = tradb_model.predict(source_X)
    yt_pred = tradb_model.predict(target_tr_X)
    yt_test_pred = tradb_model.predict(target_te_X)

    print('TrAdaBoost ' + str(label_name) + str(split_name) + ': train acc:',
          accuracy_score(source_y, ys_pred))
    print('TrAdaBoost ' + str(label_name) + str(split_name) + ': target acc:',
          accuracy_score(target_tr_y, yt_pred))
    print('TrAdaBoost ' + str(label_name) + str(split_name) + ': target_test acc:',
          accuracy_score(target_te_y, yt_test_pred))

    adb_filename = 'saved_models/tl/AdaBoost baseline ' + str(label_name) + str(split_name) + '.pkl'
    with open(adb_filename, 'rb') as adb_pickle_file:
        baseline_adb_model = pickle.load(adb_pickle_file)
    adb_pickle_file.close()
    print('AdaBoost ' + str(label_name) + str(split_name) + ': train acc:',
          accuracy_score(source_y, baseline_adb_model.predict(source_X)))
    print('AdaBoost ' + str(label_name) + str(split_name) + ': target acc:',
          accuracy_score(target_tr_y, baseline_adb_model.predict(target_tr_X)))
    print('AdaBoost ' + str(label_name) + str(split_name) + ': target_test acc:',
          accuracy_score(target_te_y, baseline_adb_model.predict(target_te_X)))
