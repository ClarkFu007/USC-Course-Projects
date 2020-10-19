import csv
import random
import time
import numpy as np

# Step1: Read the data from the "wdbc.data.file"
from hw1_utils import input_data
Data_X, Data_y = input_data(datafile_w='wdbc.data', data_m=569, data_n=32)
# print("Data_X", Data_X)
# print("Data_y", Data_y)

# Step2: Normalize our data
from hw1_utils import normalize_data
Data_x = normalize_data(Data_X, sample_num=569)
print("Data_x.shape", Data_x.shape)
# print("Data_x", Data_x)

# Step3: Partition the normalized data into training/test sets at random 100 times
from hw1_utils import split_tr_te
train_x = np.zeros((100, 500, Data_x.shape[1]), dtype='float')
train_y = np.zeros((100, 500, Data_y.shape[1]), dtype='int')
test_x = np.zeros((100, 69, Data_x.shape[1]), dtype='float')
test_y = np.zeros((100, 69, Data_y.shape[1]), dtype='int')
for index_i in range(100):
    train_x[index_i], train_y[index_i], test_x[index_i], test_y[index_i] = \
        split_tr_te(dataset=Data_x, label_set=Data_y, train_num=500, seed_value=index_i)
print("train_x.shape", train_x.shape)
print("train_y.shape", train_y.shape)
print("test_x.shape", test_x.shape)
print("test_y.shape", test_y.shape)

# Step4: Perform 500 iterations to run gradient descent for (c), (d) and (e)
b0 = 0.05
np.random.seed(1)
w0 = np.random.normal(0, 0.5, size=(30, 1))

# Problem c:
from hw1_utils import logi_regre
Hmwk1 = logi_regre(train_x=train_x, train_y=train_y, lr=0.01, lamb_da=0.01)

# Hmwk1.fit_transform(w=w0, b=b0, iter_num=500, test_x=test_x, test_y=test_y)

# Hmwk1.check_iterations(w=w0, b=b0, epsilon=1e-6, eta=0.8, method='gradient descent', verbose=True)
# Hmwk1.check_iterations(w=w0, b=b0, epsilon=1e-6, eta=0.98, method='heavy ball', verbose=False)
# Hmwk1.check_iterations(w=w0, b=b0, epsilon=1e-6, eta=0.98, method='Nesterov', verbose=False)
# Hmwk1.check_iterations(w=w0, b=b0, epsilon=1e-6, eta=0.99, method='heavy ball', verbose=False)
# Hmwk1.check_iterations(w=w0, b=b0, epsilon=1e-6, eta=0.99, method='Nesterov', verbose=False)

Hmwk1.plot_rate_curve(total_iter=500, eta=0.94, trial_i=40)










