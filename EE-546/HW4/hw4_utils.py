import numpy as np
import copy
from numpy import exp, sum, square, sqrt
from numpy import multiply, dot, expand_dims, true_divide
from numpy.linalg import inv
from scipy.io import loadmat
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def input_data(datafile_w):
    """
    Inputs:
        the location of the data file.
    Outputs:
        feature matrix X.
        label vector y.
    """
    aca = loadmat(datafile_w)
    aca_X = [[row.flat[0] for row in line] for line in aca['X']]
    aca_s = [[row.flat[0] for row in line] for line in aca['s']]
    Data_X = np.array(aca_X)
    Data_y = np.array(aca_s)
    Data_X = Data_X[:, ::2]
    Data_y = Data_y[:, ::2]

    return Data_X.T, Data_y.T


def normalize_data(Data_X):
    """
    Inputs:
        the feature matrix X.
    Outputs:
        normalized feature matrix X.
    """
    Data_L2 = expand_dims(sqrt(sum(square(Data_X), axis=1)), axis=1)
    Data_L2[Data_L2 == 0] = 1
    Data_X = true_divide(Data_X, Data_L2)

    return Data_X


def plot_scatter3D(datafile, array_name, figure_name1, figure_name2):
    """
        Inputs:
            the name of the MATLAB file.
            the name of array name in the MATLAB struture.
            the figure1 name to be saved.
            the figure2 name to be saved.
        Outputs:
            the figure.
        """
    miss_rate = loadmat(datafile)
    miss_rate_aca = [[row.flat[0] for row in line] for line in miss_rate[array_name]]
    miss_rate_aca = np.squeeze(np.array(miss_rate_aca))
    miss_rate_aca = np.reshape(miss_rate_aca, (109, 49))

    x1 = np.hstack((np.linspace(0.1, 0.9, num=9), np.linspace(1, 100, num=100)))
    y1 = np.linspace(2, 50, num=49)
    X, Y = np.meshgrid(x1, y1)  # Return coordinate matrices from coordinate vectors
    data = miss_rate_aca
    fig = plt.figure(1)
    ax = plt.axes(projection='3d')
    ax.scatter3D(X.T, Y.T, data, c='green', marker='o', s=10)
    ax.set_xlabel('The value of r')
    ax.set_ylabel('The value of k')
    ax.set_zlabel('The value of missclassification rate')
    fig.tight_layout()
    plt.show()
    fig.savefig(figure_name1)

    x2 = np.linspace(2, 50, num=49)
    y2 = np.amin(miss_rate_aca, axis=0)
    fig = plt.figure(2)
    plt.plot(x2, y2, linestyle='solid', color='green')
    plt.title("The minimum misclassification rate among r for each k")
    plt.ylabel("The value of misclassfication rate")
    plt.xlabel("The values of k from 2 to 50")
    fig.tight_layout()
    plt.show()
    fig.savefig(figure_name2)



class hw4_specClustering(object):
    def __init__(self, Data_x, r):
        self.Data_x = Data_x    # The feature matrix

        self.K = np.zeros((Data_x.shape[0], Data_x.shape[0]), dtype='float')
        for m in range(Data_x.shape[0]):
            for n in range(Data_x.shape[0]):
                if m == n:
                    self.K[m, n] = 1
                else:
                    self.K[m, n] = exp(- r * sum(square(Data_x[m] - Data_x[n])))

    def get_labels(self, k, label_num):
        """
            Get predicted labels after spectral clustering.
        :param k: The value of k to denote how many entries to choose.
        :param label_num: The number of clusters to do K-means.
        :return: The labels for each data point after spectral clustering.
        """
        """
           Build the weight matrix
        """
        W = copy.deepcopy(self.K)
        for row_i in range(self.K.shape[0]):
            sorted_array = np.sort(self.K[row_i])
            kth_value = sorted_array[self.K.shape[0] - k]
            W[row_i][W[row_i] < kth_value] = 0
        # index = np.argsort(self.K, axis=0)
        # index[index < self.Data_x.shape[0] - k] = 0
        # index[index >= self.Data_x.shape[0] - k] = 1
        # W = multiply(self.K, index)
        W = (W + W.T) / 2
        # print("W.shape", W.shape)

        """
           Get the diagonal matrix
        """
        D = np.zeros((self.Data_x.shape[0], self.Data_x.shape[0]), dtype='float')
        for i in range(self.Data_x.shape[0]):
            D[i, i] = sum(W[i])

        """
           Construct the L matrix
        """
        # identity_matrix = np.identity(self.Data_x.shape[0])
        # L = identity_matrix - dot(dot(inv(sqrt(D)), W), inv(sqrt(D)))
        L = dot(dot(inv(sqrt(D)), W), inv(sqrt(D)))
        # print("L.shape", L.shape)

        """
           Find the k largest eigenvectors of L
        """
        _, V = np.linalg.eigh(L)
        X = V[:, L.shape[0] - label_num:L.shape[0]]
        # X = V[:, 0:label_num]
        # print("The shape of the label_num largest eigenvectors X is", X.shape)
        # print("The value of k is", k)

        """
           Form the matrix Y by renormalizing each of X's rows to have unit length
        """
        Y = normalize_data(X)
        # print("The shape of the normalized matrix X is", Y.shape)

        """
           Do K-means clustering to the matix Y
        """
        from sklearn.cluster import KMeans
        my_kmeans = KMeans(n_clusters=label_num, init='k-means++', max_iter=500, tol=0.00001)
        my_kmeans.fit(Y)

        return my_kmeans.labels_






