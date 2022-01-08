import random

import numpy as np


def get_label_withProb(mu):
    """
       Gets the label with certain probability.
    :param mu: the probability for incorrect drawing
    :return: bool value for incorrect drawing
    """
    x = random.uniform(0, 1)
    if x <= mu:
        return True
    else:
        return False


def do_a_i_exp(sample_size, mu, verbose=False):
    """
       Implements the experiment of the part(a)_i.
    :param sample_size: dataset's size
    :param mu: probability of value to draw an incorrect data point
    :param verbose: whether to print the statement or not
    :return: the resulting error rate
    """
    incorrect_result = np.zeros(sample_size, dtype='float')
    for sample_i in range(sample_size):
        if get_label_withProb(mu=mu):
            incorrect_result[sample_i] = 1
        else:
            incorrect_result[sample_i] = 0
    if verbose:
        print("The error rate is {:.4f} when sample size is {} and mu is {}."
              .format(np.mean(incorrect_result), sample_size, mu))
    return np.mean(incorrect_result)


def do_b_exp(exp_num, sample_size, mu):
    """
       Implements the experiment of the part(b).
    :param exp_num: number of experiments
    :param sample_size: dataset's size
    :param mu: probability of value to draw an incorrect data point
    """
    exp_result = np.zeros(exp_num, dtype='float')
    for exp_i in range(exp_num):
        exp_result[exp_i] = do_a_i_exp(sample_size=sample_size, mu=mu)
    print("When mu is {} and sample size is {}, max error rate is {:.4f}."
          .format(mu, sample_size, np.max(exp_result)))
    print("When mu is {} and sample size is {}, min error rate is {:.4f}."
          .format(mu, sample_size, np.min(exp_result)))
    print("When mu is {} and sample size is {}, mean error rate is {:.4f}."
          .format(mu, sample_size, np.mean(exp_result)))
    print("When mu is {} and sample size is {}, std error rate is {:.4f}."
          .format(mu, sample_size, np.std(exp_result)))
    print("When mu is {} and sample size is {}, the # of differences is {}."
          .format(mu, sample_size, np.sum(exp_result != mu)))
    print("When mu is {} and sample size is {}, the estimate probability is {:.4f}."
          .format(mu, sample_size, np.sum(np.absolute(exp_result - mu) < 0.05) / exp_num))
    print("When mu is {} and sample size is {}, the # learning something is {}."
          .format(mu, sample_size, np.sum(exp_result <= 0.45)))
    print("")


def do_one_comb_exp(sample_size, mu):
    """
       Implements the combination experiment with part(a)_i and part(b).
    :param sample_size: dataset's size
    :param mu: probability of value to draw an incorrect data point
    """
    _ = do_a_i_exp(sample_size=sample_size, mu=mu, verbose=True)
    do_b_exp(exp_num=100, sample_size=sample_size, mu=mu)


def main():
    """
       The main function.
    """
    do_one_comb_exp(sample_size=10, mu=0.2)
    do_one_comb_exp(sample_size=100, mu=0.2)
    do_one_comb_exp(sample_size=10, mu=0.5)
    do_one_comb_exp(sample_size=100, mu=0.5)

    return


if __name__ == '__main__':
    main()