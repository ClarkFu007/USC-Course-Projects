import csv
import numpy as np
import matplotlib.pyplot as plt

from scipy.spatial.distance import cdist
from numpy import sum, multiply, square, sqrt


def input_data(datafile_w, data_m, data_n, lable_col):
    """
       Input the dataset.
    :param datafile_w: the location of the data file.
    :param data_m: the number of rows.
    :param data_n: the number of columns.
    :param lable_col: the column for the labels.
    :return: feature matrix X, label vector y.
    """
    InputData = np.zeros((data_m, data_n), dtype='float')
    with open(datafile_w, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            data = [float(datum) for datum in row]
            InputData[i] = data
    # print("InputData.shape", InputData.shape)

    Data_X = InputData[0:data_m, 0:lable_col-1]  # Feature matrix X
    Data_y = InputData[0:data_m, lable_col-1]  # Label vector y
    Data_y = Data_y.astype(np.int)
    Data_y = np.expand_dims(Data_y, axis=1)
    print(datafile_w[0:-3] + "shape", Data_X.shape)
    print(datafile_w[0:-3] + "shape", Data_y.shape)

    return Data_X, Data_y


def get_one_rest_label(data_y):
    """
       Gnenerate labels for one versus rest:
    :param data_y: the original label y.
    :return: the new label y.
    """
    label_num = len(np.unique(data_y))
    new_data_y = np.zeros((data_y.shape[0], label_num), dtype='int')
    for label_i in range(1, label_num+1):
        new_data_y[:, label_i - 1] = np.squeeze(multiply(data_y, data_y == label_i))

    return new_data_y


def get_final_pred(pred_y):
    """
       Get the final predicted labels.
    :param pred_y: the labels from the one-v-rest classifier.
    :return: the final label.
    """
    final_pred_y = np.zeros((pred_y.shape[0], 1), dtype='int')

    for row_i in range(0, pred_y.shape[0]):
        uniq_label_num = len(np.unique(pred_y[row_i]))
        if uniq_label_num == 2:
            final_pred_y[row_i, 0] = max(np.unique(pred_y[row_i]))
        else:
            final_pred_y[row_i, 0] = 0

    return final_pred_y


def get_accuracy(data_y, predict_y, log_word=None, to_return=False):
    """
       Draw a plot showing the final decision boundaries and regions.
    :param data_y: The real target set.
    :param predict_y: The predicted target set.
    :param log_word: Whether to print.
    :param to_return: Whether to return.
    :return: The value of classification accuracy.
    """
    accuracy = np.zeros((data_y.shape[0], 1), dtype='int')
    accuracy[data_y == predict_y] = 1
    accuracy_value = np.average(accuracy)
    if to_return:
        return accuracy_value
    else:
        print("For {}, the classification accuracy is {:4.3f}.".format(log_word, accuracy_value))


def intermediate_label_to_final_label(intermediate_label):
    """
       The helper function for drawing the final figure.
    """
    intermediate_label = (intermediate_label == 1)
    final_label = np.argmax(intermediate_label, axis=1) + 1
    final_label[np.sum(intermediate_label, axis=1) != 1] = 0
    return final_label


def plotDecBoundaries(training, label_train, sample_mean, figure_name="final_plot.png"):
    # Plot the decision boundaries and data points for minimum distance to
    # class mean classifier
    #
    # training: traning data
    # label_train: class lables correspond to training data
    # sample_mean: mean vector for each class
    #
    label_train = np.squeeze(label_train)
    # Total number of classes
    nclass = len(np.unique(label_train))

    # Set the feature range for ploting
    max_x = np.ceil(max(training[:, 0])) + 1
    min_x = np.floor(min(training[:, 0])) - 1
    max_y = np.ceil(max(training[:, 1])) + 1
    min_y = np.floor(min(training[:, 1])) - 1

    xrange = (min_x, max_x)
    yrange = (min_y, max_y)

    # step size for how finely you want to visualize the decision boundary.
    inc = 0.005

    # generate grid coordinates. this will be the basis of the decision
    # boundary visualization.
    (x, y) = np.meshgrid(np.arange(xrange[0], xrange[1] + inc / 100, inc),
                         np.arange(yrange[0], yrange[1] + inc / 100, inc))

    # size of the (x, y) image, which will also be the size of the
    # decision boundary image that is used as the plot background.
    image_size = x.shape
    xy = np.hstack((x.reshape(x.shape[0] * x.shape[1], 1, order='F'),
                    y.reshape(y.shape[0] * y.shape[1], 1, order='F')))
    # make (x,y) pairs as a bunch of row vectors.

    # prediction on mesh data
    pred_mesh = np.zeros((xy.shape[0], 3))
    for index_i in range(0, nclass):
        # distance measure evaluations for each (x, y) pair.
        dist_mat = cdist(xy, sample_mean[int(2*index_i):int(2*index_i)+2])
        pred_mesh[:, index_i] = np.argmin(dist_mat, axis=1)

    # reshape the idx (which contains the class label) into an image.
    final_pred_mesh = intermediate_label_to_final_label(pred_mesh)
    decisionmap = final_pred_mesh.reshape(image_size, order='F')

    # show the image, give each coordinate a color according to its class label
    plt.imshow(decisionmap, extent=[xrange[0], xrange[1], yrange[0], yrange[1]], origin='lower')

    # plot the class training data.
    plt.plot(training[label_train == 1, 0], training[label_train == 1, 1], 'mx')
    plt.plot(training[label_train == 2, 0], training[label_train == 2, 1], 'go')
    plt.plot(training[label_train == 3, 0], training[label_train == 3, 1], 'r*')
    # include legend for training data
    l = plt.legend(('Class 1', 'Class 2', 'Class 3'), loc=2)
    # plt.gca().add_artist(l)  # Make it transparent
    plt.tight_layout()
    plt.savefig(figure_name)
    plt.show()


class NearestMeansClassify(object):
    def __init__(self, train_X, train_y, goal_label, non_label):
        """
           Implement the algorithm of nearest-means classification.
        :param train_X: the feature matrix.
        :param train_y: the label vector.
        """
        self.train_X = train_X
        self.train_y = train_y
        self.goal_label = goal_label
        self.non_label = non_label

        self.samp_num = train_X.shape[0]
        self.feat_num = train_X.shape[1]
        self.label_num = len(np.unique(train_y))
        self.sample_mean_matrix = np.zeros((self.label_num, self.feat_num), dtype='float')

    def fit(self, to_return=False):
        """
           Train the model.
        """
        train_index = np.zeros((self.samp_num, self.label_num), dtype='int')
        for label_i in range(0, self.label_num):
            # If meeting the condition, set as 1, else 0.
            if label_i == 0:
                train_index[:, label_i] = np.squeeze(np.where(self.train_y == self.non_label, 1, 0))
            else:
                train_index[:, label_i] = np.squeeze(np.where(self.train_y == self.goal_label, 1, 0))

        for label_i in range(0, self.label_num):
            label_index = train_index[:, label_i]
            label_index = np.expand_dims(label_index, axis=1)
            label_index = np.repeat(a=label_index, repeats=self.feat_num, axis=1)
            self.sample_mean_matrix[label_i] = sum(multiply(self.train_X, label_index), axis=0) / \
                                                   sum(train_index[:, label_i])

        if to_return:
            return self.sample_mean_matrix

    def transform(self, data_X):
        """
           Do the prediction.
        :param data_X: The dataset to be predicted.
        :return: The prediction results.
        """
        new_samp_num = data_X.shape[0]
        sample_mean = np.zeros((self.label_num, new_samp_num, self.feat_num), dtype='float')
        for label_i in range(0, self.label_num):
            sample_mean_value = self.sample_mean_matrix[label_i]
            sample_mean_value = np.expand_dims(sample_mean_value, axis=0)
            sample_mean_value = np.repeat(a=sample_mean_value, repeats=new_samp_num, axis=0)
            sample_mean[label_i] = sample_mean_value

        l2_matrix = np.zeros((new_samp_num, self.label_num), dtype='float')
        for label_i in range(0, self.label_num):
            l2_vector = sqrt(sum(square(data_X - sample_mean[label_i]), axis=1))
            l2_matrix[:, label_i] = l2_vector
        # print("l2_matrix.shape", l2_matrix.shape)

        pred_y = np.argmin(l2_matrix, axis=1)
        pred_y = np.expand_dims(pred_y, axis=1)
        # print("pred_y.shape", pred_y.shape)

        return np.where(pred_y != 1, pred_y, pred_y + self.goal_label - 1)

    def plotDecBoundaries(self, figure_name):
        # Plot the decision boundaries and data points for minimum distance to
        # class mean classifier
        #
        # training: traning data
        # label_train: class lables correspond to training data
        # sample_mean: mean vector for each class
        #
        training = self.train_X
        label_train = np.squeeze(self.train_y)
        sample_mean = self.sample_mean_matrix
        # Total number of classes
        nclass = len(np.unique(label_train))

        # Set the feature range for ploting
        max_x = np.ceil(max(training[:, 0])) + 1
        min_x = np.floor(min(training[:, 0])) - 1
        max_y = np.ceil(max(training[:, 1])) + 1
        min_y = np.floor(min(training[:, 1])) - 1

        xrange = (min_x, max_x)
        yrange = (min_y, max_y)

        # step size for how finely you want to visualize the decision boundary.
        inc = 0.005

        # generate grid coordinates. this will be the basis of the decision
        # boundary visualization.
        (x, y) = np.meshgrid(np.arange(xrange[0], xrange[1] + inc / 100, inc),
                             np.arange(yrange[0], yrange[1] + inc / 100, inc))

        # size of the (x, y) image, which will also be the size of the
        # decision boundary image that is used as the plot background.
        image_size = x.shape
        xy = np.hstack((x.reshape(x.shape[0] * x.shape[1], 1, order='F'),
                        y.reshape(y.shape[0] * y.shape[1], 1, order='F')))
        # make (x,y) pairs as a bunch of row vectors.

        # distance measure evaluations for each (x,y) pair.
        dist_mat = cdist(xy, sample_mean)
        pred_label = np.argmin(dist_mat, axis=1)

        # reshape the idx (which contains the class label) into an image.
        decisionmap = pred_label.reshape(image_size, order='F')

        # show the image, give each coordinate a color according to its class label
        plt.imshow(decisionmap, extent=[xrange[0], xrange[1], yrange[0], yrange[1]], origin='lower')

        # plot the class training data.
        plt.plot(training[label_train == self.non_label, 0], training[label_train == self.non_label, 1], 'rx')
        plt.plot(training[label_train == self.goal_label, 0], training[label_train == self.goal_label, 1], 'go')

        # include legend for training data
        l = plt.legend(('Class_Rest', 'Class' + str(self.goal_label)), loc=2)
        plt.gca().add_artist(l)

        # plot the class mean vector.
        m1, = plt.plot(sample_mean[0, 0], sample_mean[0, 1], 'rd', markersize=12, markerfacecolor='r',
                       markeredgecolor='w')
        m2, = plt.plot(sample_mean[1, 0], sample_mean[1, 1], 'gd', markersize=12, markerfacecolor='g',
                       markeredgecolor='w')

        # include legend for class mean vector
        l1 = plt.legend([m1, m2], ['Class_Rest Mean',
                                       'Class ' + str(self.goal_label) + ' Mean'], loc=4)

        plt.gca().add_artist(l1)
        plt.tight_layout()
        plt.savefig(figure_name)
        plt.show()


