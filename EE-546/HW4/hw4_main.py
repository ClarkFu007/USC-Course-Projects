import numpy as np
import scipy.io as sio

# Step1: Read the data from "aca2.mat" and "aca5.mat"
from hw4_utils import input_data
Data_X1, Data_y1 = input_data(datafile_w='aca2.mat')
Data_X2, Data_y2 = input_data(datafile_w='aca5.mat')
print("Data_X1.shape", Data_X1.shape)
print("Data_y1.shape", Data_y1.shape)
print("Data_X2.shape", Data_X2.shape)
print("Data_y2.shape", Data_y2.shape)
save_s1, save_s2 = 'aca2_labels.mat', 'aca5_labels.mat'
save_array_s1, save_array_s2 = Data_y1, Data_y2
sio.savemat(save_s1, {'array': save_array_s1})
sio.savemat(save_s2, {'array': save_array_s2})
# Step2: Normalize our data
from hw4_utils import normalize_data
Data_x1 = normalize_data(Data_X1)
Data_x2 = normalize_data(Data_X2)
print("Data_x1.shape", Data_x1.shape)
print("Data_x2.shape", Data_x2.shape)

# Step3: Implement the spectral clustering
from hw4_utils import hw4_specClustering


total_num = 109 * 49
# For the dataset "aca2.mat"
total_results1 = np.zeros((total_num, Data_x1.shape[0]), dtype='int')
label_num1 = int(max(Data_y1))
iter_i1 = 0
for r in range(1, 9 + 1):
    hw4_solver1 = hw4_specClustering(Data_x=Data_x1, r=r/10)
    for k in range(2, 50 + 1):
        pre_labels1 = hw4_solver1.get_labels(k=k, label_num=label_num1)
        total_results1[iter_i1] = pre_labels1 + 1
        print("For the dataset 'aca2.mat', the iteration is %04d/%04d," % (iter_i1+1, total_num))
        iter_i1 += 1
for r in range(1, 100 + 1):
    hw4_solver1 = hw4_specClustering(Data_x=Data_x1, r=r)
    for k in range(2, 50 + 1):
        pre_labels1 = hw4_solver1.get_labels(k=k, label_num=label_num1)
        total_results1[iter_i1] = pre_labels1 + 1
        print("For the dataset 'aca2.mat', the iteration is %04d/%04d," % (iter_i1+1, total_num))
        iter_i1 += 1
save_fn1 = 'total_results1.mat'
save_array1 = total_results1
sio.savemat(save_fn1, {'array': save_array1})
print("The operation of dataset 'aca2.mat' is finished!")


# For the dataset "aca5.mat"
total_results2 = np.zeros((total_num, Data_x2.shape[0]), dtype='int')
label_num2 = int(max(Data_y2))
iter_i2 = 0
for r in range(1, 9 + 1):
    hw4_solver2 = hw4_specClustering(Data_x=Data_x2, r=r/10)
    for k in range(2, 50 + 1):
        pre_labels2 = hw4_solver2.get_labels(k=k, label_num=label_num2)
        total_results2[iter_i2] = pre_labels2 + 1
        print("For the dataset 'aca5.mat', the iteration is %04d/%04d," % (iter_i2+1, total_num))
        iter_i2 += 1
for r in range(1, 100 + 1):
    hw4_solver2 = hw4_specClustering(Data_x=Data_x2, r=r)
    for k in range(2, 50 + 1):
        pre_labels2 = hw4_solver2.get_labels(k=k, label_num=label_num2)
        total_results2[iter_i2] = pre_labels2 + 1
        print("For the dataset 'aca5.mat', the iteration is %04d/%04d," % (iter_i2+1, total_num))
        iter_i2 += 1
save_fn2 = 'total_results2.mat'
save_array2 = total_results2
sio.savemat(save_fn2, {'array': save_array2})
print("The operation of dataset 'aca5.mat' is finished!")

