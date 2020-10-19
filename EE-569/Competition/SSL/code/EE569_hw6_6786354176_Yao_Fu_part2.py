# EE569 Homework Assignment # 6
# Submission Date: April 26, 2020
# Name: Yao Fu
# USC ID: 6786354176
# Email: yaof@usc.edu


import numpy as np
import time

from keras.datasets import cifar10
from sklearn.model_selection import train_test_split

from pixelhop2 import Pixelhop2
from skimage.util import view_as_windows


# The function to do the max pooling
def max_pooling(output):
    new_output = np.zeros([output.shape[0], output.shape[1] // 2,
                           output.shape[2] // 2, output.shape[3]])

    for i in range(0, output.shape[0]):
        for j in range(0, output.shape[3]):
            for m in range(0, output.shape[1], 2):
                for n in range(0, output.shape[2], 2):
                    pixel_list = [output[i, m, n, j], output[i, m + 1, n, j],
                                  output[i, m, n + 1, j], output[i, m + 1, n + 1, j]]
                    max_pixel = max(pixel_list)
                    new_output[i, m // 2, n // 2, j] = max_pixel

    return new_output


from cross_entropy import Cross_Entropy


# Do the feature selection
def extract_feature(re_output, re_output_test, N, train_label):
    my_CrossEntropy = Cross_Entropy(num_class=10, num_bin=5)
    feat_ce = np.zeros(re_output.shape[-1])
    print("re_output.shape[-1]", re_output.shape[-1])
    print("re_output_test.shape[-1]", re_output_test.shape[-1])

    for k in range(re_output.shape[-1]):
        feat_ce[k] = my_CrossEntropy.compute(re_output[:, k].reshape(-1, 1), train_label)
        # feat_ce[k] = my_CrossEntropy.KMeans_Cross_Entropy(re_output[:, k].reshape(-1, 1), train_label)
        # print(" --> KMeans cross entropy: %s" % str(feat_ce[k]))

    sorted_index = np.argsort(feat_ce)  # increasing
    final_output = np.zeros([re_output.shape[0], N], np.float32)
    print("re_output.shape[0]", re_output.shape[0])
    final_output_test = np.zeros([re_output_test.shape[0], N], np.float32)
    print("re_output_test.shape[0]", re_output_test.shape[0])

    for i in range(0, N):
        final_output[:, i] = re_output[:, sorted_index[i]]
        final_output_test[:, i] = re_output_test[:, sorted_index[i]]

    return final_output, final_output_test


from lag import LAG
from llsr import LLSR as myLLSR


# Do the label-assisted regression
def lag_oper(feature_ce, test_ce, train_label):
    my_LAG = LAG(encode='distance', num_clusters=[5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                 alpha=10, learner=myLLSR(onehot=False))

    my_LAG.fit(feature_ce, train_label)
    X_train_trans = my_LAG.transform(feature_ce)
    X_test_trans = my_LAG.transform(test_ce)

    # X_train_pred_prob = my_LAG.predict_proba(feature_ce)
    # print(" --> train acc: %s" % str(my_LAG.score(feature_ce, train_label)))

    return X_train_trans, X_test_trans


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
                        pixel_list = [X[i, m, n, j], X[i, m+1, n, j],
                                      X[i, m, n+1, j], X[i, m+1, n+1, j]]
                        max_pixel = max(pixel_list)
                        X_new[i, m // 2, n // 2, j] = max_pixel

    ch = X_new.shape[-1]
    X_new = view_as_windows(X_new, (1, win, win, ch), (1, stride, stride, ch))
    return X_new.reshape(X_new.shape[0], X_new.shape[1], X_new.shape[2], -1)


# The function to concatenate features from different hops
def Concat(X, concatArg):
    return X


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


# Load pixel_hop.pickle
from sklearn.externals import joblib
pixel_hop = joblib.load('pixel_hop.pkl')

# 0.5, 0.25, 0.125, 0.0625, 0.03125
# Extract features from the Module 1: outputs are before max-pooling
TrainData1, temp_TrainData, TrainLabel1, temp_TrainLabel = \
    train_test_split(TrainData, TrainLabel, test_size=1-0.5, stratify=TrainLabel)
# TrainData1, TrainLabel1 = TrainData, TrainLabel
print('TrainData1', TrainData1.shape)
print('TrainLabel1', TrainLabel1.shape)

time_start = time.time()
output_temp = pixel_hop.transform(TrainData1[0: 1000, :, :, :])
output0_temp, output1_temp, output2_temp = output_temp[0], output_temp[1], output_temp[2]
print("output_temp", output_temp[0].shape)  # 1000,28,28,42

# The function to do batch processing while doing the pixelhop transform
for i in range(1000, TrainData1.shape[0], 1000):
    print("i", i)
    temp_i = pixel_hop.transform(TrainData1[i: (i+1000), :, :, :])     # Train
    output0_temp = np.vstack((output0_temp, temp_i[0]))
    output1_temp = np.vstack((output1_temp, temp_i[1]))
    output2_temp = np.vstack((output2_temp, temp_i[2]))
    print("output0_temp", output0_temp.shape)

output_test_temp = pixel_hop.transform(TestData[0: 1000, :, :, :])
output0_test_temp, output1_test_temp, output2_test_temp = output_test_temp[0], \
                                                          output_test_temp[1], output_test_temp[2]
print("output_test_temp", output_test_temp[0].shape)

for j in range(1000, TestData.shape[0], 1000):
    print("j", j)
    temp_j = pixel_hop.transform(TestData[j: (j+1000), :, :, :])     # Train
    output0_test_temp = np.vstack((output0_test_temp, temp_j[0]))
    output1_test_temp = np.vstack((output1_test_temp, temp_j[1]))
    output2_test_temp = np.vstack((output2_test_temp, temp_j[2]))
    print("output0_test_temp", output0_test_temp.shape)

time_end = time.time()
print('Running time for the PixelHop transform part: %s Seconds' % (time_end - time_start))

output0, output1, output2 = output0_temp, output1_temp, output2_temp
output0_test, output1_test, output2_test = output0_test_temp, output1_test_temp, output2_test_temp

print("Before max pooling, output:", output0.shape, output1.shape, output2.shape)
print("Before max pooling, output_test:", output0_test.shape, output1_test.shape, output2_test.shape)


# The output of train data
new_output0 = max_pooling(output0)
new_output1 = max_pooling(output1)
new_output2 = output2

print("After max pooling, output:",
      new_output0.shape, new_output1.shape, new_output2.shape)
re_output0 = new_output0.reshape(new_output0.shape[0], -1)
re_output1 = new_output1.reshape(new_output1.shape[0], -1)
re_output2 = new_output2.reshape(new_output2.shape[0], -1)
print("After max pooling, output:",
      re_output0.shape, re_output1.shape, re_output2 .shape)

# The output of test data
time_start = time.time()

new_output0_test = max_pooling(output0_test)
new_output1_test = max_pooling(output1_test)
new_output2_test = output2_test

print("After max pooling, output_test:",
      new_output0_test.shape, new_output1_test.shape, new_output2_test.shape)
re_output0_test = new_output0_test.reshape(new_output0_test.shape[0], -1)
re_output1_test = new_output1_test.reshape(new_output1_test.shape[0], -1)
re_output2_test = new_output2_test.reshape(new_output2_test.shape[0], -1)
print("After max pooling, output:",
      re_output0_test.shape, re_output1_test.shape, re_output2_test.shape)
time_end = time.time()
print('Running time: %s Seconds' % (time_end - time_start))


# Do feature selection
time_start = time.time()
print("Begin feature selection!")

(Final_output0, Final_output_test0) = \
    extract_feature(re_output0, re_output0_test, 3000, TrainLabel1)  # Train label might change 1750
print("Feature_ce0:", Final_output0.shape)
print("Final_output_test0:", Final_output_test0.shape)

(Final_output1, Final_output_test1) = \
    extract_feature(re_output1, re_output1_test, 2000, TrainLabel1)  # Train label might change 1000
print("Feature_ce1:", Final_output1.shape)
print("Final_output_test1:", Final_output_test1.shape)

(Final_output2, Final_output_test2) = \
    extract_feature(re_output2, re_output2_test, 275, TrainLabel1)  # Train label might change 250
print("Feature_ce2:", Final_output2.shape)
print("Final_output_test2:", Final_output_test2.shape)

time_end = time.time()
print('Running time for the feature extraction part: %s Seconds' % (time_end - time_start))

# Do the label-assisted regression
time_start = time.time()
(Train_trans0, Test_trans0) = lag_oper(Final_output0, Final_output_test0, TrainLabel1)
(Train_trans1, Test_trans1) = lag_oper(Final_output1, Final_output_test1, TrainLabel1)
(Train_trans2, Test_trans2) = lag_oper(Final_output2, Final_output_test2, TrainLabel1)

print('Train_trans0', Train_trans0.shape)
print('Train_trans1', Train_trans1.shape)
print('Train_trans2', Train_trans2.shape)
print('Test_trans0', Test_trans0.shape)
print('Test_trans1', Test_trans1.shape)
print('Test_trans2', Test_trans2.shape)

Train_trans = np.hstack((Train_trans0, Train_trans1, Train_trans2))
Test_trans = np.hstack((Test_trans0, Test_trans1, Test_trans2))

print('Train_trans', Train_trans.shape)
print('Test_trans', Test_trans.shape)

time_end = time.time()
print('Running time for the LAG: %s Seconds' % (time_end - time_start))

# Use the random forest algorithm to train the classifier
time_start = time.time()
from sklearn.ensemble import RandomForestClassifier

X = Train_trans
Y = TrainLabel1
clf = RandomForestClassifier(n_estimators=100)
clf = clf.fit(X, np.ravel(Y))

print("Training:"+str(clf.score(X, Y)))
print("Test:"+str(clf.score(Test_trans, TestLabel)))

time_end = time.time()
print("Running time for the Random Forest: %s Seconds" % (time_end - time_start))


# The function to draw the heat maps of the confusion matrices
import matplotlib.pyplot as plt
from sklearn.metrics import plot_confusion_matrix
from matplotlib import cm

np.set_printoptions(precision=2)
# Plot non-normalized confusion matrix
titles_options = [("Confusion matrix, without normalization", None),
                  ("Normalized confusion matrix", 'true')]
i = 3
for title, normalize in titles_options:
    disp = plot_confusion_matrix(clf, Test_trans, TestLabel,
                                 cmap=cm.get_cmap('Blues'),
                                 normalize=normalize)
    disp.ax_.set_title(title)

    print(title)
    print(disp.confusion_matrix)

    plt.savefig("The confusion matrix%s" % i)
    i += 1