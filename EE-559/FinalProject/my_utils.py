import pandas as pd


def read_csv(list_path):
    """
       Reads the data from csv files.
    :param list_path: the file path.
    :return: the Pandas dataframe type.
    """
    lines = []
    with open(list_path, 'rb') as f:
        lines = pd.read_csv(list_path, header=0, encoding='unicode_escape')
    return lines


def toNumpy(data_frame_X, data_frame_y):
    """
       Converts the Pandas dataframe type to Numpy array type.
    :param data_frame_X: feature dataframe.
    :param data_frame_y: label dataframe.
    :return: feature matirx and label vector.
    """

    X_data = data_frame_X.to_numpy()

    y_data = data_frame_y.to_numpy().ravel()
    return X_data, y_data