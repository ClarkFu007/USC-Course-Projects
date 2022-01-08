import numpy as np
import pandas as pd

from utils import handle_raw_data
from utils import split_feat_and_label
from utils import one_hot_preprocess_sl, one_hot_preprocess_tl
from utils import get_tr_te_set, get_so_ta_set

from sl_core import do_sl_experiments
from tl_core import do_tl_experiments
from ssl_core import do_ssl_experiments


def do_sl_for_one_column(data, label_index, feat_indices, one_hot_cols, min_max_cols):
    """
       Does supervised learning experiments with the selected column as labels.
    :param data: original data.
    :param label_index: label index.
    :param feat_indices: feature indices.
    :param one_hot_cols: columns for one-hot encoding.
    :param min_max_cols: columns for min-max normalization.
    """
    data_X, data_y = split_feat_and_label(data=data, label_index=label_index,
                                          feat_indices=feat_indices)
    data_X = one_hot_preprocess_sl(data_X=data_X, one_hot_cols=one_hot_cols, min_max_cols=min_max_cols)
    train_X, train_y, test_X, test_y = get_tr_te_set(data_X=data_X, data_y=data_y, test_size=895)
    """
       train_X: (4000, 32), train_y: (4000,)
       test_X: (895, 32), test_y: (895,)
    """
    # Normal experiments
    do_sl_experiments(train_X=train_X, train_y=train_y, test_X=test_X, test_y=test_y,
                      label_name=str(label_index))
    # Experiments for deleting the only numerical feature
    do_sl_experiments(train_X=train_X[:, 0:31], train_y=train_y, test_X=test_X[:, 0:31], test_y=test_y,
                      label_name=str(label_index)+'_nm')


def do_tl_for_one_column(data, label_index, feat_indices, split_col, one_hot_cols, min_max_cols, test_size):
    """
        Does transfer learning experiments with the selected column as labels.
    :param data: original data
    :param label_index: label index
    :param feat_indices: feature indices
    :param split_col: column to be split for transfer learning
    :param one_hot_cols: columns for one-hot encoding
    :param min_max_cols: columns for min-max normalization.
    :param test_size: size of test data for target
    """
    data_X, data_y = split_feat_and_label(data=data, label_index=label_index,
                                          feat_indices=feat_indices)
    prepro_source_X, source_data_y, prepro_target_X, target_data_y = \
        one_hot_preprocess_tl(data_X=data_X, data_y=data_y, split_col=split_col,
                              one_hot_cols=one_hot_cols, min_max_cols=min_max_cols)
    source_X, source_y, target_tr_X, target_tr_y, target_te_X, target_te_y = \
        get_so_ta_set(prepro_source_X=prepro_source_X, source_data_y=source_data_y,
                      prepro_target_X=prepro_target_X, target_data_y=target_data_y,
                      test_size=test_size)

    do_tl_experiments(source_X=source_X, source_y=source_y,
                      target_tr_X=target_tr_X, target_tr_y=target_tr_y,
                      target_te_X=target_te_X, target_te_y=target_te_y,
                      label_name=str(label_index), split_name=str(split_col))


def do_ssl_for_one_column(data, label_index, feat_indices, one_hot_cols, min_max_cols, unlabel_num):
    """
       Does semi-supervised learning experiments with the selected column as labels.
    :param data: original data
    :param label_index: label index
    :param feat_indices: feature indices
    :param one_hot_cols: columns for one-hot encoding
    :param min_max_cols: columns for min-max normalization
    :param unlabel_num: number of unlabeled data points
    """
    data_X, data_y = split_feat_and_label(data=data, label_index=label_index,
                                          feat_indices=feat_indices)
    data_X = one_hot_preprocess_sl(data_X=data_X, one_hot_cols=one_hot_cols, min_max_cols=min_max_cols)
    train_X, train_y, test_X, test_y = get_tr_te_set(data_X=data_X, data_y=data_y, test_size=895)
    """
       train_X: (4000, 32), train_y: (4000,)
       test_X: (895, 32), test_y: (895,)
    """
    do_ssl_experiments(train_X=train_X, train_y=train_y, unlabel_num=unlabel_num,
                       test_X=test_X, test_y=test_y, label_name=str(label_index))


def main():
    """
       Input the data.
       Feature names [0: id -- ignore
                      1: name -- ignore
                      2: date -- ignore
                      3: manner_of_death -- ['shot' 'shot and Tasered'] (4627, 248)
                      4: armed -- ignore
                      5: age -- 6 to 91 (not containing all)
                      6: gender -- ['F' 'M'] (222, 4673)
                      7: race -- ['Asian' 'Black' 'Hispanic' 'Native' 'Other' 'White']
                      8: city -- ignore
                      9: state -- ['AK' 'AL' 'AR' 'AZ' 'CA' 'CO' 'CT' 'DC' 'DE' 'FL' 'GA' 'HI' 'IA'
                                   'ID' 'IL' 'IN' 'KS' 'KY' 'LA' 'MA' 'MD' 'ME' 'MI' 'MN' 'MO' 'MS'
                                   'MT' 'NC' 'ND' 'NE' 'NH' 'NJ' 'NM' 'NV' 'NY' 'OH' 'OK' 'OR' 'PA'
                                   'RI' 'SC' 'SD' 'TN' 'TX' 'UT' 'VA' 'VT' 'WA' 'WI' 'WV' 'WY']
                      10: signs_of_mental_illness -- [False True] (3792, 1103)
                      11: threat_level -- ['attack' 'other' 'undetermined']
                      12: flee -- ['Car' 'Foot' 'Not fleeing' 'Other']
                      13: body_camera -- [False True]  (4317, 578)
                      14: arms_category -- ['Blunt instruments' 'Electrical devices' 'Explosives'
                                            'Guns' 'Hand tools' Multiple' 'Other unusual objects'
                                            'Piercing objects' 'Sharp objects' 'Unarmed' 'Unknown'
                                            'Vehicles']
    """
    data_frame = pd.read_csv("dataset/shootings.csv.")
    raw_data = data_frame.values  # (4895, 15)
    data = handle_raw_data(data=raw_data)

    """
       Experiments for supervised learning.
    """
    if False:
        # 3: manner_of_death -- ['shot' 'shot and Tasered'] (4627, 248)
        print("3: manner_of_death -- ['shot' 'shot and Tasered']")
        do_sl_for_one_column(data=data, label_index=3, feat_indices=[5, 6, 7, 10, 11, 12, 13, 14],
                             one_hot_cols=[1, 2, 3, 4, 5, 6, 7], min_max_cols=0)
        print("")

        # 6: gender -- ['F' 'M'] (222, 4673)
        print("gender -- ['F' 'M']")
        do_sl_for_one_column(data=data, label_index=6, feat_indices=[3, 5, 7, 10, 11, 12, 13, 14],
                             one_hot_cols=[0, 2, 3, 4, 5, 6, 7], min_max_cols=1)
        print("")

        # 10: signs_of_mental_illness -- [False True] (3792, 1103)
        print("signs_of_mental_illness -- [False True]")
        do_sl_for_one_column(data=data, label_index=10, feat_indices=[3, 5, 6, 7, 11, 12, 13, 14],
                             one_hot_cols=[0, 2, 3, 4, 5, 6, 7], min_max_cols=1)
        print("")

        # 13: body_camera -- [False True] (4317, 578)
        print("body_camera -- [False True]")
        do_sl_for_one_column(data=data, label_index=13, feat_indices=[3, 5, 6, 7, 10, 11, 12, 14],
                             one_hot_cols=[0, 2, 3, 4, 5, 6, 7], min_max_cols=1)
        print("")

    """
        Experiments for transfer learning.
    """
    if False:
        # 3: manner_of_death -- ['shot' 'shot and Tasered'] (4627, 248)
        do_tl_for_one_column(data=data, label_index=3, feat_indices=[5, 6, 7, 10, 11, 12, 13], split_col=3,
                             one_hot_cols=[1, 2, 3, 4, 5, 6], min_max_cols=0, test_size=1000)

        do_tl_for_one_column(data=data, label_index=3, feat_indices=[5, 6, 7, 10, 11, 12, 13], split_col=6,
                             one_hot_cols=[1, 2, 3, 4, 5, 6], min_max_cols=0, test_size=500)
        # 6: gender -- ['F' 'M'] (222, 4673)
        do_tl_for_one_column(data=data, label_index=6, feat_indices=[3, 5, 7, 10, 11, 12, 13], split_col=3,
                             one_hot_cols=[0, 2, 3, 4, 5, 6], min_max_cols=1, test_size=1000)
        do_tl_for_one_column(data=data, label_index=6, feat_indices=[3, 5, 7, 10, 11, 12, 13], split_col=6,
                             one_hot_cols=[0, 2, 3, 4, 5, 6], min_max_cols=1, test_size=500)

    """
       Experiments for semi-supervised learning.
    """
    if True:
        # 3: manner_of_death -- ['shot' 'shot and Tasered'] (4627, 248)
        do_ssl_for_one_column(data=data, label_index=3, feat_indices=[5, 6, 7, 10, 11, 12, 13, 14],
                              one_hot_cols=[1, 2, 3, 4, 5, 6, 7], min_max_cols=0, unlabel_num=1000)

        # 6: gender -- ['F' 'M'] (222, 4673)
        do_ssl_for_one_column(data=data, label_index=6, feat_indices=[3, 5, 7, 10, 11, 12, 13, 14],
                              one_hot_cols=[0, 2, 3, 4, 5, 6, 7], min_max_cols=1, unlabel_num=1000)

        # 10: signs_of_mental_illness -- [False True] (3792, 1103)
        do_ssl_for_one_column(data=data, label_index=10, feat_indices=[3, 5, 6, 7, 11, 12, 13, 14],
                              one_hot_cols=[0, 2, 3, 4, 5, 6, 7], min_max_cols=1, unlabel_num=1000)
        # 13: body_camera - - [False True] (4317, 578)
        do_ssl_for_one_column(data=data, label_index=13, feat_indices=[3, 5, 6, 7, 10, 11, 12, 14],
                              one_hot_cols=[0, 2, 3, 4, 5, 6, 7], min_max_cols=1, unlabel_num=1000)

    return


if __name__ == '__main__':
    main()