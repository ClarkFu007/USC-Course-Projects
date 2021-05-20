"""
EE559 Spring2021 H7W13 Problem 1 Code Outline (Optional)
** Please note:
(1) Find a good place for regularization (Ridge).
(2) This code outline doesn't contain cross-validation for model selection.
(3) You need to perform cross-validation based on the "RBFN Module", in order to
    do the model selection of gamma*, v*, and K* (and the regularization)
(4) It'll be more convenient for model selection to wrap the "RBFN Module" into one function, or use OOP instead.
(5) See another example in Discussion 11 Week 13.
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.cluster import KMeans


def load_data(datapath):
    x_, y_ = [], []
    return x_, y_


def rbf_layer1(X, mu, gamma):
    """Layer 1: Get transformed phi(x)"""
    phi_x_ = []
    return phi_x_


def rbf_layer2(X, y=None, weight=None):
    """Layer 2: fit/inference the regression"""
    # augmentation
    X = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)

    if weight is None:
        # train (fit)
        weight = []
        return weight
    else:
        # test (predict)
        y_hat_ = []
        return y_hat_


def choose_centers(X, M, mode=1):
    """Three different ways of selecting centers"""
    if mode == 1:  # (c)
        centers_ = []
    elif mode == 2:  # (d)
        centers_ = []
    elif mode == 3:  # (e)
        centers_ = []

    return centers_


def cal_mse(y, y_pred):
    """Calculate MSE"""
    mse = []
    return mse


def calculate_gamma(X, M):
    """Calculate gamma"""
    gamma_ = []
    return gamma_


def cal_avg_spacing(X, M):
    """Calculate average spacing"""
    avg_space = []
    return avg_space


if __name__ == "__main__":
    '''Example structure'''
    MODE = 3  # Example: using K-means for center selection
    K = 500

    # ------------- Load data -------------
    X, y = [], []

    # ============================= Start of "RBFN Module" =============================
    # ------------- Calculate M using v or K -------------
    M = []

    # ------------- Find average spacing and initial gamma -------------
    avg_spacing = []
    gamma = []

    # ------------- Select centers -------------
    centers = []

    # ------------- Start 2 layers of RBF Network -------------
    # Layer 1
    phi_x = []
    # Layer 2
    y_hat = []

    # ------------- Calculate MSE -------------
    MSE = []
    # ============================= End of "RBFN Module" =============================

    print('finished!')
