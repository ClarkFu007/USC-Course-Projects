import numpy as np

from hw4_utils import get_error_rate


class PerceptronModel(object):
    """
       The class to implement the perceptron learning algorithm.
    """
    def __init__(self, learning_rate=0.01, max_iter_num=10000, last_num=100):
        self.learning_rate = learning_rate
        self.max_iter_num = max_iter_num
        self.last_num = last_num
        self.total_iter_num = 0
        self.aug_weights = []
        self.best_aug_weights = []
        self.class_num = 0

    def fit(self, data_X, data_y, sgd_method=None, to_return=False):
        """
           Uses data_X and data_y to train the perceptron model.
        :param data_X: feature matrix for training data.
        :param data_y: label vector for training data.
        :param sgd_method: "SGD1" or "SGD2"
        :param to_return: whether to retuan or out
        :return: returan error rate array if True
        """
        sample_num, feat_num = data_X.shape
        self.class_num = len(np.unique(data_y))
        linear_out = np.zeros(self.class_num, dtype="float")
        aug_data_X = np.insert(data_X, 0, np.ones(sample_num), axis=1)
        for _ in range(self.class_num):
            self.aug_weights.append(np.ones(feat_num + 1))

        error_rate_array = np.zeros((1000), dtype="float")
        if sgd_method == "SGD1":
            epoch_i = 0  # Denote which epoch we are in
            halting_sign = False
            min_error_rate = 1
            while (True):  # Make it have enough epochs
                train_index = np.random.permutation(sample_num)  # Randomly shuffle training data
                update_num = 0
                for data_i in range(sample_num):
                    iter_i = (epoch_i - 1) * sample_num + data_i + 1
                    self.total_iter_num = iter_i
                    if iter_i % 10 == 0:
                        predict_y = self.transform(data_X=data_X, mode="validation")
                        index = int(iter_i / 10)
                        error_rate_array[index - 1] = get_error_rate(data_y=data_y, predict_y=predict_y,
                                                                     to_return=True)
                    if iter_i == self.max_iter_num:
                        halting_sign = True
                        break

                    for class_i in range(self.class_num):
                        linear_out[class_i] = np.dot(self.aug_weights[class_i],
                                                     aug_data_X[train_index[data_i]])
                    # linear_out = np.dot(self.aug_weights, aug_data_X[train_index[data_i]])
                    data_i_class = int(data_y[train_index[data_i]])
                    max_linear_out_pos = int(np.argmax(linear_out))
                    if data_i_class != max_linear_out_pos:
                        aug_weight_update = self.learning_rate * aug_data_X[train_index[data_i]]
                        self.aug_weights[data_i_class] = self.aug_weights[data_i_class] + aug_weight_update
                        self.aug_weights[max_linear_out_pos] = self.aug_weights[max_linear_out_pos] - aug_weight_update
                        update_num += 1

                    if iter_i >= self.max_iter_num - self.last_num:
                        predict_y = self.transform(data_X=data_X, mode="validation")

                        curr_error_rate = get_error_rate(data_y=data_y, predict_y=predict_y,
                                                         to_return=True)
                        if min_error_rate > curr_error_rate:
                            min_error_rate = curr_error_rate
                            self.best_aug_weights = self.aug_weights

                if halting_sign or update_num == 0:
                    break
                epoch_i += 1

            if to_return:
                return error_rate_array

        elif sgd_method == "SGD2":
            min_error_rate = 1
            iter_i = 0
            while (True):  # Make it have enough iterations
                random_data_i = np.random.choice(a=np.arange(sample_num), size=1)[0]  # Randomly choose one data
                nonupdate_num = 0
                iter_i += 1
                self.total_iter_num = iter_i
                if iter_i % 10 == 0:
                    predict_y = self.transform(data_X=data_X, mode="validation")
                    index = int(iter_i / 10)
                    error_rate_array[index - 1] = get_error_rate(data_y=data_y, predict_y=predict_y,
                                                                 to_return=True)
                if iter_i == self.max_iter_num or nonupdate_num == 100:
                    break

                for class_i in range(self.class_num):
                    linear_out[class_i] = np.dot(self.aug_weights[class_i],
                                                 aug_data_X[random_data_i])
                data_i_class = int(data_y[random_data_i])
                max_linear_out_pos = int(np.argmax(linear_out))
                if data_i_class != max_linear_out_pos:
                    aug_weight_update = self.learning_rate * aug_data_X[random_data_i]
                    self.aug_weights[data_i_class] = self.aug_weights[data_i_class] + aug_weight_update
                    self.aug_weights[max_linear_out_pos] = self.aug_weights[max_linear_out_pos] - aug_weight_update
                else:
                    nonupdate_num += 1

                if iter_i >= self.max_iter_num - self.last_num:
                    predict_y = self.transform(data_X=data_X, mode="validation")
                    curr_error_rate = get_error_rate(data_y=data_y, predict_y=predict_y,
                                                     to_return=True)
                    if min_error_rate > curr_error_rate:
                        min_error_rate = curr_error_rate
                        self.best_aug_weights = self.aug_weights

            if to_return:
                return error_rate_array

        else:
            print("Please input the correct method!")
            return None

    def transform(self, data_X, mode="validation"):
        """
           Uses the trained model to do predictions.
        :param data_X: feature mattrix to be predected.
        :param mode: "validation" or "test".
        :return: predicted labels.
        """
        sample_num = data_X.shape[0]
        aug_data_X = np.insert(data_X, 0, np.ones(sample_num), axis=1)
        linear_out = np.zeros((sample_num, self.class_num), dtype="float")
        for sample_i in range(sample_num):
            for class_i in range(self.class_num):
                if mode == "validation":
                    linear_out[sample_i, class_i] = np.dot(self.aug_weights[class_i],
                                                           aug_data_X[sample_i])
                elif mode == "test":
                    if self.total_iter_num == self.max_iter_num:
                        linear_out[sample_i, class_i] = np.dot(self.best_aug_weights[class_i],
                                                               aug_data_X[sample_i])
                    else:
                        linear_out[sample_i, class_i] = np.dot(self.aug_weights[class_i],
                                                               aug_data_X[sample_i])
                else:
                    print("Please input the correct mode!")
                    return None

        predicted_y = self._activation_func(linear_out)
        return predicted_y

    def _activation_func(self, input_data):
        """
           Selects the maximum value from several discriminant functions.
        :param input_data: data to be input.
        :return: data after being activated.
        """
        pred_y = np.argmax(input_data, axis=1)
        pred_y = np.expand_dims(pred_y, axis=1)
        return pred_y
