# EE569 Homework Assignment # 6
# Submission Date: April 26, 2020
# Name: Yao Fu
# USC ID: 6786354176
# Email: yaof@usc.edu

from sklearn.externals import joblib
import time
import numpy as np
from keras.datasets import cifar10
from sklearn.model_selection import train_test_split

from pixelhop2 import Pixelhop2
from skimage.util import view_as_windows


# The function to do the shrank
def Shrink(X, shrinkArg):
    win = shrinkArg['win']
    stride = shrinkArg['stride']
    ith_hop = shrinkArg['ith_hop']

    if ith_hop == 1:
        X_new = X
    else:
        X_new = np.zeros([X.shape[0], X.shape[1] // 2, X.shape[2] // 2, X.shape[3]])
        for i in range(0, X.shape[0]):
            for j in range(0, X.shape[3]):
                for m in range(0, X.shape[1], 2):
                    for n in range(0, X.shape[2], 2):
                        pixel_list = [X[i, m, n, j], X[i, m + 1, n, j],
                                      X[i, m, n + 1, j], X[i, m + 1, n + 1, j]]
                        max_pixel = max(pixel_list)
                        X_new[i, m // 2, n // 2, j] = max_pixel

    ch = X_new.shape[-1]
    X_new = view_as_windows(X_new, (1, win, win, ch), (1, stride, stride, ch))
    return X_new.reshape(X_new.shape[0], X_new.shape[1], X_new.shape[2], -1)


# The function to concatenate features from different hops
def Concat(X, concatArg):
    return X


# Step1: Train the module1
# import training data, training labels, testing data, and testing labels
(TrainData, TrainLabel), (TestData, TestLabel) = cifar10.load_data()
print('Train_data shape', TrainData.shape)    # train_data: (50000, 32, 32, 3)
print('Train_label shape', TrainLabel.shape)  # train_label: (50000, 1)
print('Test_data shape', TestData.shape)      # test_data: (10000, 32, 32, 3)
print('Test_label shape', TestLabel.shape)    # test_label: (10000, 1)
TrainData = TrainData.astype('float32')
TrainData /= 255
TestData = TestData.astype('float32')
TestData /= 255

NewTrainData, NewTrainData0, NewTrainLabel, NewTrainLabel0 = \
    train_test_split(TrainData, TrainLabel, test_size=0.8, stratify=TrainLabel)
print('New train data shape', NewTrainData.shape)        # train_data: (10000, 32, 32, 3)
print('New train label shape', NewTrainLabel.shape)      # train_label: (10000, 1)
print('New train data0 shape', NewTrainData0.shape)      # test_data: (40000, 32, 32, 3)
print('New train label0 shape', NewTrainLabel0.shape)    # test_label: (40000, 1)

# Set the necessary arguments
SaabArgs = [{'num_AC_kernels': -1, 'needBias': False, 'useDC': True, 'batch': None, 'cw': False},
            {'num_AC_kernels': -1, 'needBias': True, 'useDC': True, 'batch': None, 'cw': True},
            {'num_AC_kernels': -1, 'needBias': True, 'useDC': True, 'batch': None, 'cw': True}]
shrinkArgs = [{'func': Shrink, 'win': 5, 'stride': 1, 'ith_hop': 1},
              {'func': Shrink, 'win': 5, 'stride': 1, 'ith_hop': 2},
              {'func': Shrink, 'win': 5, 'stride': 1, 'ith_hop': 3}]
concatArg = {'func': Concat}


pixel_hop = Pixelhop2(depth=3, TH1=0.001, TH2=0.0001, SaabArgs=SaabArgs,
                      shrinkArgs=shrinkArgs, concatArg=concatArg)

# Train the model
print(NewTrainData.shape[1])
time_start = time.time()
pixel_hop.fit(NewTrainData)
time_end = time.time()
print("Running time for the PixelHop's fitting part is %s Seconds" % (time_end - time_start))

# Save the model as pixel_hop.pickle
joblib.dump(pixel_hop, 'pixel_hop.pkl')

print('The program is over successfully!')