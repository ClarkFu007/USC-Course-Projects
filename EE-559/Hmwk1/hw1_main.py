import csv
import random
import time
import numpy as np


from hw1_utils import input_data
# Read the data from two synthetic datasets.
syn1_tr_X, syn1_tr_y = input_data(datafile_w='synthetic1_train.csv', data_m=100, data_n=3, lable_col=3)
syn1_te_X, syn1_te_y = input_data(datafile_w='synthetic1_test.csv', data_m=100, data_n=3, lable_col=3)

syn2_tr_X, syn2_tr_y = input_data(datafile_w='synthetic2_train.csv', data_m=100, data_n=3, lable_col=3)
syn2_te_X, syn2_te_y = input_data(datafile_w='synthetic2_test.csv', data_m=100, data_n=3, lable_col=3)

wine_tr_X, wine_tr_y = input_data(datafile_w='wine_train.csv', data_m=89, data_n=14, lable_col=14)
wine_te_X, wine_te_y = input_data(datafile_w='wine_test.csv', data_m=89, data_n=14, lable_col=14)


from hw1_utils import NearestMeansClassify
from hw1_utils import get_error_rate
# Train a nearest-means classifier.
my_model_syn1 = NearestMeansClassify(train_X=syn1_tr_X, train_y=syn1_tr_y)
my_model_syn1 .fit()
pred_y_syn_tr1 = my_model_syn1 .transform(data_X=syn1_tr_X)
get_error_rate(data_y=syn1_tr_y, predict_y=pred_y_syn_tr1, log_word='syn1_training')
pred_y_syn_te1 = my_model_syn1 .transform(data_X=syn1_te_X)
get_error_rate(data_y=syn1_te_y, predict_y=pred_y_syn_te1, log_word='syn1_test')
my_model_syn1 .plotDecBoundaries(figure_name='syn1_training.png')

my_model_syn2 = NearestMeansClassify(train_X=syn2_tr_X, train_y=syn2_tr_y)
my_model_syn2.fit()
pred_y_syn_tr2 = my_model_syn2 .transform(data_X=syn2_tr_X)
get_error_rate(data_y=syn2_tr_y, predict_y=pred_y_syn_tr2, log_word='syn2_training')
pred_y_syn_te2 = my_model_syn2 .transform(data_X=syn2_te_X)
get_error_rate(data_y=syn2_te_y, predict_y=pred_y_syn_te2, log_word='syn2_test')
my_model_syn2.plotDecBoundaries(figure_name='syn2_training.png')


# Pick the first two features:
select_wine_tr = wine_tr_X[:, 0:2]
select_wine_te = wine_te_X[:, 0:2]

my_model_wine0 = NearestMeansClassify(train_X=select_wine_tr, train_y=wine_tr_y)
my_model_wine0.fit()
pred_y_wine_tr0 = my_model_wine0 .transform(data_X=select_wine_tr)
get_error_rate(data_y=wine_tr_y, predict_y=pred_y_wine_tr0, log_word='wine0_training')
pred_y_wine_te0 = my_model_wine0 .transform(data_X=select_wine_te)
get_error_rate(data_y=wine_te_y, predict_y=pred_y_wine_te0, log_word='wine0_test')
my_model_wine0.plotDecBoundaries(figure_name='wine0_training.png')


# Pick two features to achieve the minimum error rate on the training data.
select_wine_tr_temp = np.zeros((wine_tr_X.shape[0], 2), dtype='float')
select_wine_te_temp = np.zeros((wine_te_X.shape[0], 2), dtype='float')
error_rate_array_tr = np.zeros(int(13*12/2), dtype='float')
error_rate_array_te = np.zeros(int(13*12/2), dtype='float')
min_error_rate_tr, index = 1, 0
object_i, object_j = 0, 0
for first_i in range(0, 12):
    for second_j in range(first_i+1, 13):
        select_wine_tr_temp = np.hstack((np.expand_dims(wine_tr_X[:, first_i], axis=1),
                                         np.expand_dims(wine_tr_X[:, second_j], axis=1)))
        my_model_wine = NearestMeansClassify(train_X=select_wine_tr_temp, train_y=wine_tr_y)
        my_model_wine.fit()
        pred_y_wine_tr = my_model_wine.transform(data_X=select_wine_tr_temp)
        temp_error_rate_tr = get_error_rate(data_y=wine_tr_y, predict_y=pred_y_wine_tr, to_return=True)
        error_rate_array_tr[index] = temp_error_rate_tr
        if temp_error_rate_tr < min_error_rate_tr:
            min_error_rate_tr = temp_error_rate_tr
            object_i, object_j = first_i, second_j

        select_wine_te_temp = np.hstack((np.expand_dims(wine_te_X[:, first_i], axis=1),
                                         np.expand_dims(wine_te_X[:, second_j], axis=1)))
        pred_y_wine_te = my_model_wine.transform(data_X=select_wine_te_temp)
        temp_error_rate_te = get_error_rate(data_y=wine_te_y, predict_y=pred_y_wine_te, to_return=True)
        error_rate_array_te[index] = temp_error_rate_te

        index += 1

from numpy import mean, std
print("The min error rate is {:5.3f} for the two features {} and {}".format(min_error_rate_tr, object_i, object_j))
print("For taining, the mean error rate is {:4.2f} and standard deviation is {:4.2f}".format(mean(error_rate_array_tr),
                                                                                             std(error_rate_array_tr)))
print("For testng, the mean error rate is {:4.2f} and standard deviation is {:4.2f}".format(mean(error_rate_array_te),
                                                                                             std(error_rate_array_te)))
select_wine_tr_final = np.hstack((np.expand_dims(wine_tr_X[:, object_i], axis=1),
                                  np.expand_dims(wine_tr_X[:, object_j], axis=1)))
select_wine_te_final = np.hstack((np.expand_dims(wine_te_X[:, object_i], axis=1),
                                  np.expand_dims(wine_te_X[:, object_j], axis=1)))
my_model_wine_final = NearestMeansClassify(train_X=select_wine_tr_final, train_y=wine_tr_y)
my_model_wine_final.fit()
pred_y_wine_final = my_model_wine_final.transform(data_X=select_wine_te_final)
get_error_rate(data_y=wine_te_y, predict_y=pred_y_wine_final, log_word='wine_test with 2 best features')
my_model_wine_final.plotDecBoundaries(figure_name='wine_training.png')


