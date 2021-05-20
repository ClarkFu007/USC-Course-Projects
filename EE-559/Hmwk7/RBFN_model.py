import copy
import numpy as np

from sklearn import linear_model
from sklearn.cluster import KMeans


class RBNF(object):
    def __init__(self, v_value=None, k_value=None, select_method=''):
        """
           Radial basis function network.
        # Arguments:
           :param v_value: value of percentage of training-set samples.
           :param select_method: method to selecting centers.
        """
        self.v_value = v_value
        self.k_value = k_value
        self.select_method = select_method
        self.centers = None
        self.linear_regr_model = None
        self.train_num = None
        self.feat_num = None
        self.m_value = None
        self.scale_factor = None

    def _kernel_function(self, gamma, data_point, center):
        """
           Calculates the nonlinear mapping feature for each data point in different centers.
        # Arguments:
        :param gamma: gamma value.
        :param data_point: each data point.
        :param center: each selected center.
        :return: the nonlinear mapping feature.
        """
        return np.exp(- gamma * np.linalg.norm(data_point - center) ** 2)

    def _calculate_interpolation_matrix(self, X):
        """
           Calculates interpolation matrix using a kernel_function.
        # Arguments:
           :param X: training data.
           :return G: interpolation matrix.
        """
        average_space = (np.prod(np.max(X, axis=0) - np.min(X, axis=0)) / self.m_value) ** (1.0 / self.feat_num)
        sigma = 2 * average_space
        gamma = 1.0 * self.scale_factor / (2 * sigma ** 2)
        G = np.zeros((len(X), self.m_value))
        for data_point_i, data_point in enumerate(X):
            for center_i, center in enumerate(self.centers):
                G[data_point_i, center_i] = self._kernel_function(gamma, data_point, center)

        return G

    def _select_centers(self, X):
        """
           Selects several centers for hidden radial basis functions.
        # Arguments:
           :param X: training data.
           :return centers: selected centers.
        """
        if self.select_method == 'all select':
            centers = copy.deepcopy(X)
            return centers

        elif self.select_method == 'random select':
            random_i = np.random.choice(self.train_num, self.m_value)
            centers = X[random_i]
            return centers

        elif self.select_method == 'k-means clustering':
            kmeans_model = KMeans(n_clusters=self.k_value, init='random',  max_iter=1000).fit(X)
            centers = kmeans_model.cluster_centers_
            return centers
        else:
            print("Please select the correct method!")
            return None

    def fit(self, X, y, scale_factor):
        """
           Fits weights using MSE linear regression.
        # Arguments:
           :param X: training data.
           :param y: target values.
           :param scale_factor: factor value to scale gamma.
        """
        self.train_num, self.feat_num = X.shape[:]
        if self.select_method == 'all select':
            self.m_value = self.train_num
        elif self.select_method == 'random select':
            self.m_value = int(self.train_num * self.v_value)
        elif self.select_method == 'k-means clustering':
            self.m_value = self.k_value
        else:
            print("Please select the correct method!")
        self.centers = self._select_centers(X)
        self.scale_factor = scale_factor
        G = self._calculate_interpolation_matrix(X)
        self.linear_regr_model = linear_model.LinearRegression()
        self.linear_regr_model.fit(G, y)

    def predict(self, X):
        """
           Predicts regression values of the given data.
        # Arguments:
           :param X: training data.
           :return y_pred: predicted y values.
        """
        G = self._calculate_interpolation_matrix(X)
        y_pred = self.linear_regr_model.predict(G)

        return y_pred
