import numpy as np

from sklearn.linear_model import LinearRegression


class MSE_Binary(LinearRegression):
    def __init__(self):
        super(MSE_Binary, self).__init__()
        print("Calling newly created MSE binary function . . . ")

    def predict(self, X):
        threshold_value = 0.5  # may vary depending on Xw = b
        y = self._decision_function(X)
        y_binary = np.where(y > threshold_value, 1, 0)

        return y_binary
