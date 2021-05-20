import csv
import random
import time
import numpy as np

from numpy import multiply, squeeze, expand_dims

# Read the data from two synthetic datasets.
from hw2_utils import input_data
wine_tr_X, wine_tr_y = input_data(datafile_w='wine_train.csv', data_m=89, data_n=14, lable_col=14)
wine_te_X, wine_te_y = input_data(datafile_w='wine_test.csv', data_m=89, data_n=14, lable_col=14)

# Pick the first two features.
select_wine_tr = wine_tr_X[:, 0:2]  # (89, 2)
select_wine_te = wine_te_X[:, 0:2]  # (89, 2)

# Gnenerate labels for one versus rest.
from hw2_utils import get_one_rest_label
new_wine_tr_y = get_one_rest_label(wine_tr_y)
new_wine_te_y = get_one_rest_label(wine_te_y)

# Train a nearest-means classifier with the one-versues-rest technique.
from hw2_utils import NearestMeansClassify
label_num = len(np.unique(wine_tr_y))
pred_y_wine_tr = np.zeros((wine_tr_X.shape[0], label_num), dtype='int')
pred_y_wine_te = np.zeros((wine_te_X.shape[0], label_num), dtype='int')
sample_mean_matrix = np.zeros((int(2 * label_num), select_wine_tr.shape[1]), dtype='float')
for label_i in range(1, label_num+1):
    temp_wine_tr_y = expand_dims(new_wine_tr_y[:, label_i - 1], axis=1)
    goal_label = max(temp_wine_tr_y)
    non_label = min(temp_wine_tr_y)

    my_model_wine = NearestMeansClassify(train_X=select_wine_tr, train_y=temp_wine_tr_y,
                                         goal_label=goal_label, non_label=non_label)

    index_i, index_j = label_i * 2 - 2, label_i * 2 - 1
    sample_mean_matrix[index_i:index_j + 1] = my_model_wine.fit(to_return=True)

    pred_y_wine_tr[:, label_i - 1] = squeeze(my_model_wine.transform(data_X=select_wine_tr))
    pred_y_wine_te[:, label_i - 1] = squeeze(my_model_wine.transform(data_X=select_wine_te))
    my_model_wine.plotDecBoundaries(figure_name=str(label_i) + "plot.png")

# Get the final predicted labels.
from hw2_utils import get_final_pred
final_pred_y_wine_tr = get_final_pred(pred_y_wine_tr)
final_pred_y_wine_te = get_final_pred(pred_y_wine_te)

# Get the accuracy values on the training set and test set.
from hw2_utils import get_accuracy
get_accuracy(data_y=wine_tr_y, predict_y=final_pred_y_wine_tr, log_word='wine_training')
get_accuracy(data_y=wine_te_y, predict_y=final_pred_y_wine_te, log_word='wine_test')

# Draw a plot showing the final decision boundaries and regions.
from hw2_utils import plotDecBoundaries
plotDecBoundaries(training=select_wine_tr, label_train=wine_tr_y,
                  sample_mean=sample_mean_matrix)






