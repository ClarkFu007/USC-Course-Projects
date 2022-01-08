import copy
import pickle

import numpy as np

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split


def handle_raw_data(data):
    """
       Converts the raw data's feature into numeric values.
    :param data: raw data
    :return: new data
    """
    manner_of_death = {'shot': 0, 'shot and Tasered': 1}  # 3
    gender = {'F': 0, 'M': 1}  # 6
    race = {'Asian': 0, 'Black': 1, 'Hispanic': 2, 'Native': 3, 'Other': 4, 'White': 5}  # 7
    state = {'AK': 0, 'AL': 1, 'AR': 2, 'AZ': 3, 'CA': 4, 'CO': 5, 'CT': 6, 'DC': 7,
             'DE': 8, 'FL': 9, 'GA': 10, 'HI': 11, 'IA': 12, 'ID': 13, 'IL': 14,
             'IN': 15, 'KS': 16, 'KY': 17, 'LA': 18, 'MA': 19, 'MD': 20, 'ME': 21,
             'MI': 22, 'MN': 23, 'MO': 24, 'MS': 25, 'MT': 26, 'NC': 27, 'ND': 28,
             'NE': 29, 'NH': 30, 'NJ': 31, 'NM': 32, 'NV': 33, 'NY': 34, 'OH': 35,
             'OK': 36, 'OR': 37, 'PA': 38, 'RI': 39, 'SC': 40, 'SD': 41, 'TN': 42,
             'TX': 43, 'UT': 44, 'VA': 45, 'VT': 46, 'WA': 47, 'WI': 48, 'WV': 49, 'WY': 50}
    signs_of_mental_illness = {'False': 0, 'True': 1}  # 10
    threat_level = {'attack': 0, 'other': 1, 'undetermined': 2}  # 11
    flee = {'Car': 0, 'Foot': 1, 'Not fleeing': 2, 'Other': 3}  # 12
    body_camera = {'False': 0, 'True': 1}  # 13
    arms_category = {'Blunt instruments': 0, 'Electrical devices': 1, 'Explosives': 2,
                     'Guns': 3, 'Hand tools': 4, 'Multiple': 5, 'Other unusual objects': 6,
                     'Piercing objects': 7, 'Sharp objects': 8, 'Unarmed': 9, 'Unknown': 10,
                     'Vehicles': 11}  # 14
    cat_feat_list = [manner_of_death, gender, race, signs_of_mental_illness,
                     threat_level, flee, body_camera, arms_category]
    cat_feat_dict = {3: 0, 6: 1, 7: 2, 10: 3, 11: 4, 12: 5, 13: 6, 14: 7}
    new_data = np.zeros((data.shape[0], data.shape[1]), dtype='float')
    new_data[:, 5] = data[:, 5]
    for sample_i in range(data.shape[0]):
        for feat_i in range(data.shape[1]):
            if feat_i in cat_feat_dict:
                cat_feat_index = cat_feat_dict[feat_i]
                new_data[sample_i, feat_i] = \
                    cat_feat_list[cat_feat_index][str(data[sample_i, feat_i])]

    return new_data


def split_feat_and_label(data, label_index, feat_indices):
    """
       Splits the data into the feature matrix and the label vector.
    :param data: original data
    :param label_index: label index
    :param feat_indices: feature indices
    :return: data_X, data_y
    """

    data_X, data_y = copy.deepcopy(data[:, feat_indices]), copy.deepcopy(data[:, label_index])
    print("data_X.shape", data_X.shape)
    print("data_y.shape", data_y.shape)
    label_names = np.unique(data_y)
    print("The number of {} is {}".format(label_names[0], np.sum(data_y == label_names[0])))
    print("The number of {} is {}".format(label_names[1], np.sum(data_y == label_names[1])))

    return data_X, data_y


def one_hot_preprocess_sl(data_X, one_hot_cols, min_max_cols):
    """
       Preprocesses the data with one-hot encoding for supervised learning.
    :param data_X: feature matrix X (4895, 8)
    :param one_hot_cols: columns for one-hot encoding
    :param min_max_cols: columns for min-max scaling
    :return: preprocessed data.
    """
    prepro_data_X = np.zeros((data_X.shape[0], 32), dtype='float')
    # One-hot encodes some features:
    enc = OneHotEncoder(handle_unknown='ignore')
    prepro_data_X[:, 0:31] = enc.fit_transform(data_X[:, one_hot_cols]).toarray()
    # Add the age feature:
    prepro_data_X[:, 31] = copy.deepcopy(data_X[:, min_max_cols])

    return prepro_data_X


def get_tr_te_set(data_X, data_y, test_size):
    """
       Gets training data and test data for supervised learning.
    :param data_X: feature matrix
    :param data_y: label vector
    :param test_size: size of test data
    :return: train_X, train_y, test_X, test_y
    """
    train_X, test_X, train_y, test_y = train_test_split(data_X, data_y, test_size=test_size,
                                                        random_state=660)
    # MinMax scale the age feature:
    minmax_scaler = MinMaxScaler()
    minmax_scaler.fit(np.expand_dims(train_X[:, 31], axis=1))
    train_X[:, 31] = np.squeeze(minmax_scaler.transform(np.expand_dims(train_X[:, 31], axis=1)))
    test_X[:, 31] = np.squeeze(minmax_scaler.transform(np.expand_dims(test_X[:, 31], axis=1)))

    return train_X, train_y, test_X, test_y


def one_hot_preprocess_tl(data_X, data_y, split_col, one_hot_cols, min_max_cols):
    """
       Preprocesses the data with one-hot encoding for transfer learning.
    :param data_X: feature matrix X (4895, 8)
    :param data_y: label vector y
    :param split_col: column to be split for transfer learning
    :param one_hot_cols: columns for one-hot encoding
    :param min_max_cols: columns for min-max scaling
    :return: prepro_source_X, source_data_y, prepro_target_X, target_data_y
    """
    source_data_X = copy.deepcopy(data_X[data_X[:, split_col] == 0])
    source_data_y = copy.deepcopy(data_y[data_X[:, split_col] == 0])
    target_data_X = copy.deepcopy(data_X[data_X[:, split_col] == 1])
    target_data_y = copy.deepcopy(data_y[data_X[:, split_col] == 1])
    # print("source_data_X", source_data_X.shape)
    # print("target_data_X", target_data_X.shape)
    # print("one_hot_cols", one_hot_cols)
    np.set_printoptions(threshold=np.inf)

    prepro_source_X = np.zeros((source_data_X.shape[0], 19), dtype='float')
    prepro_target_X = np.zeros((target_data_X.shape[0], 19), dtype='float')
    # One-hot encodes some features:
    enc = OneHotEncoder(handle_unknown='ignore')
    prepro_source_X[:, 0:18] = enc.fit_transform(source_data_X[:, one_hot_cols]).toarray()
    prepro_target_X[:, 0:18] = enc.fit_transform(target_data_X[:, one_hot_cols]).toarray()
    # Add the age feature:
    prepro_source_X[:, 18] = copy.deepcopy(source_data_X[:, min_max_cols])
    prepro_target_X[:, 18] = copy.deepcopy(target_data_X[:, min_max_cols])

    return prepro_source_X, source_data_y, prepro_target_X, target_data_y


def get_so_ta_set(prepro_source_X, source_data_y, prepro_target_X, target_data_y, test_size):
    """
       Gets source data and target data for transfer learning.
    :param prepro_source_X: feature matrix for source data
    :param source_data_y: label vector for source data
    :param prepro_target_X: feature matrix for target data
    :param target_data_y: label vector for target data
    :param test_size: size of test data
    :return: train_X, train_y, test_X, test_y
    """
    target_tr_X, target_te_X, target_tr_y, target_te_y = \
        train_test_split(prepro_target_X, target_data_y, test_size=test_size, random_state=660)
    # MinMax scale the age feature:
    minmax_scaler = MinMaxScaler()
    minmax_scaler.fit(np.expand_dims(prepro_source_X[:, 18], axis=1))
    prepro_source_X[:, 18] = np.squeeze(minmax_scaler.transform(np.expand_dims(prepro_source_X[:, 18], axis=1)))
    target_tr_X[:, 18] = np.squeeze(minmax_scaler.transform(np.expand_dims(target_tr_X[:, 18], axis=1)))
    target_te_X[:, 18] = np.squeeze(minmax_scaler.transform(np.expand_dims(target_te_X[:, 18], axis=1)))

    return prepro_source_X, source_data_y, target_tr_X, target_tr_y, target_te_X, target_te_y


def save_model(filename,  model):
    """
       Saves the trained model.
    :param filename: name of the file.
    :param model: model to be saved.
    """
    with open(filename + '.pkl', 'wb') as (pickle_file):
        pickle.dump(model, pickle_file)
    pickle_file.close()
    print("A model has been saved as {}".format(filename))