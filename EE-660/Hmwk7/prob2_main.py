import matplotlib.pyplot as plt
import numpy as np

from numpy import abs


def get_gaussian_value(x_h, mu_value, sigma_value):
    """
       Gets Gaussian values.
    :param x_h: unlabeled data
    :param mu_value: mean value
    :param sigma_value: sigma value
    :return:
    """
    sigma_value2 = sigma_value ** 2
    value = np.exp(-(x_h-mu_value)**2 / (2*sigma_value2)) / np.sqrt(2 * np.pi * sigma_value2)
    return value


def get_gamma(x_h, pi_vector, mu_vector, sigma_vector, mode, verbose=False, to_return=False):
    """
       For the parts (f).
    :param x_h: unlabeled data
    :param pi_vector: pi(probability) vector
    :param mu_vector: mean vector
    :param sigma_vector: sigma vector
    :param mode: 'gamma1' or 'gamma2'
    :param verbose: whether to show the result
    :param to_return: whether to return the result
    :return: gamma_value
    """
    gaussian_value1 = get_gaussian_value(x_h, mu_vector[0], sigma_vector[0])
    gaussian_value2 = get_gaussian_value(x_h, mu_vector[1], sigma_vector[1])
    gaussian_sum = pi_vector[0] * gaussian_value1 + pi_vector[1] * gaussian_value2
    if mode == 'gamma1':
        gamma_value = pi_vector[0] * gaussian_value1 / gaussian_sum
    elif mode == 'gamma2':
        gamma_value = pi_vector[1] * gaussian_value2 / gaussian_sum
    if verbose:
        print("The " + mode + " value is {:.4f}".format(gamma_value))
    if to_return:
        return gamma_value


def get_mu(gamma_value, x_h, mode, verbose=False, to_return=False):
    """
       For the parts (f).
    :param gamma_value: gamma value
    :param x_h: unlabeled data
    :param mode: 'mu1' or 'mu2'
    :param verbose: whether to show the result
    :param to_return: whether to return the result
    :return: mu_value
    """
    if mode == 'mu1':
        mu_value = (2 * gamma_value * x_h + 1 + 2) / (2 * gamma_value + 2)
    elif mode == 'mu2':
        mu_value = (2 * gamma_value * x_h + 4) / (2 * gamma_value + 1)
    if verbose:
        print("The " + mode + " value is {:.4f}".format(mu_value))
    if to_return:
        return mu_value


def do_part_f():
    """
       Implements the part(f).
    """
    ul_data = 3.0
    pi_vector = [0.5, 0.5]
    mu_vector, sigma_vector = [1.5, 4.0], [1, 1]
    iterm_num = 1
    threshold_value = 0.000001
    gamma1_list, gamma2_list = [], []
    mu1_list, mu2_list = [], []
    while True:
        gamma1 = get_gamma(x_h=ul_data, pi_vector=pi_vector, mu_vector=mu_vector,
                           sigma_vector=sigma_vector, mode='gamma1', to_return=True)
        gamma1_list.append(gamma1)
        gamma2 = get_gamma(x_h=ul_data, pi_vector=pi_vector, mu_vector=mu_vector,
                           sigma_vector=sigma_vector, mode='gamma2', to_return=True)
        gamma2_list.append(gamma2)
        mu1 = get_mu(gamma_value=gamma1, x_h=ul_data, mode='mu1', to_return=True)
        mu1_list.append(mu1)
        mu2 = get_mu(gamma_value=gamma2, x_h=ul_data, mode='mu2', to_return=True)
        mu2_list.append(mu2)
        if iterm_num == 1:
            last_gamma1, last_gamma2 = gamma1, gamma2
            last_mu1, last_mu2 = mu1, mu2
            mu_vector = [mu1, mu2]
            iterm_num += 1
            continue
        else:
            if abs(gamma1 - last_gamma1) <= threshold_value:
                if abs(gamma2 - last_gamma2) <= threshold_value:
                    if abs(mu1 - last_mu1) <= threshold_value:
                        if abs(mu2 - last_mu2) <= threshold_value:
                            break
        last_gamma1, last_gamma2 = gamma1, gamma2
        last_mu1, last_mu2 = mu1, mu2
        mu_vector = [mu1, mu2]
        iterm_num += 1

    print("The final gamma1 value is {:.4f}".format(gamma1_list[iterm_num - 1]))
    print("The final gamma2 value is {:.4f}".format(gamma2_list[iterm_num - 1]))
    print("The final mu1 value is {:.4f}".format(mu1_list[iterm_num - 1]))
    print("The final mu2 value is {:.4f}".format(mu2_list[iterm_num - 1]))

    iterm_seq = np.arange(1, iterm_num + 1, 1)
    plt.figure(0)
    plt.plot(iterm_seq, np.array(gamma1_list), 'b')
    plt.title(r'The plot of $\gamma_1$ values vs. $iteration_i$')
    plt.ylabel(r'$\gamma_1$ values')
    plt.xlabel(r'$iteration_i$')
    plt.tight_layout()
    plt.savefig("gamma1" + "_results.png")
    plt.show()

    plt.figure(1)
    plt.plot(iterm_seq, np.array(gamma2_list), 'b')
    plt.title(r'The plot of $\gamma_2$ values vs. $iteration_i$')
    plt.ylabel(r'$\gamma_2$ values')
    plt.xlabel(r'$iteration_i$')
    plt.tight_layout()
    plt.savefig("gamma2" + "_results.png")
    plt.show()

    plt.figure(2)
    plt.plot(iterm_seq, np.array(mu1_list), 'b')
    plt.title(r'The plot of $\mu_1$ values vs. $iteration_i$')
    plt.ylabel(r'$\mu_1$ values')
    plt.xlabel(r'$iteration_i$')
    plt.tight_layout()
    plt.savefig("mu1" + "_results.png")
    plt.show()

    plt.figure(3)
    plt.plot(iterm_seq, np.array(mu2_list), 'b')
    plt.title(r'The plot of $\mu_2$ values vs. $iteration_i$')
    plt.ylabel(r'$\mu_2$ values')
    plt.xlabel(r'$iteration_i$')
    plt.tight_layout()
    plt.savefig("mu2" + "_results.png")
    plt.show()


def main():
    """
       The main function.
    """
    ul_data = 3.0
    pi_vector = [0.5, 0.5]
    mu_vector, sigma_vector = [1.5, 4.0], [1, 1]
    # Part (e):
    # Part (e).i:
    gamma1 = get_gamma(x_h=ul_data, pi_vector=pi_vector, mu_vector=mu_vector,
                       sigma_vector=sigma_vector, mode='gamma1', verbose=True,
                       to_return=True)
    gamma2 = get_gamma(x_h=ul_data, pi_vector=pi_vector, mu_vector=mu_vector,
                       sigma_vector=sigma_vector, mode='gamma2', verbose=True,
                       to_return=True)
    # Part (e).ii:
    get_mu(gamma_value=gamma1, x_h=ul_data, mode='mu1', verbose=True)
    get_mu(gamma_value=gamma2, x_h=ul_data, mode='mu2', verbose=True)

    # Part (f):
    do_part_f()

    return


if __name__ == '__main__':
    main()