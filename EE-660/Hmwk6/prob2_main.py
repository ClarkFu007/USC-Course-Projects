import matplotlib.pyplot as plt
import numpy as np


def do_a_part(N_t, N_s, alpha, d_hh=0.1, d_vc=10, tolerance=0.1, verbose=False):
    """
       Implements the experiment of the part(a).
    :param N_t: number of target labeled data points
    :param N_s: number of source labeled data points
    :param alpha: alpha value
    :param d_hh: value of symmetric difference hypothesis divergence
    :param d_vc: value of VC dimension
    :param tolerance: tolerance value
    :param verbose: whether to print the statement or not
    :return: the resulting error rate
    """
    # Calculate the interested part of the cross-domain generalization-error bound:
    N_tol = N_t + N_s
    beta = N_t / N_tol
    part_cd_geb_value = (1 - alpha) * d_hh + \
                        4 * np.sqrt(alpha ** 2 / beta + (1 - alpha) ** 2 / (1 - beta)) * \
                        np.sqrt(2 / N_tol * d_vc * np.log(2 * (N_tol + 1)) +
                                2 / N_tol * np.log(8 / tolerance))
    if verbose:
        print("The value of the interested part of the cross-domain generalization-error bound is {:.4f}, "
              "when N_t is {}, N_s is {}, and alpha is {}.".format(part_cd_geb_value, N_t, N_s, alpha))


def plot_bc(mode, d_hh=0.1, d_vc=10, tolerance=0.1):
    """
        Implements the drawing of the part(b) and the part(c).
    :param mode: 'part_b' or 'part_c'
    :param d_hh: value of symmetric difference hypothesis divergence
    :param d_vc: value of VC dimension
    :param tolerance: tolerance value
    """
    # evenly sampled
    alpha_value = np.arange(0.001, 1., 0.001)
    if mode == 'part_b':
        N_s, i = 1000, 0
        N_t = [10, 100, 1000, 10000]
        part_cd_geb_value_list = []
        for N_ti in N_t:
            N_tol = N_ti + N_s
            beta = N_ti / N_tol
            part_cd_geb_value = (1 - alpha_value) * d_hh + \
                                4 * np.sqrt(alpha_value ** 2 / beta + (1 - alpha_value) ** 2 / (1 - beta)) * \
                                np.sqrt(2 / N_tol * d_vc * np.log(2 * (N_tol + 1)) +
                                        2 / N_tol * np.log(8 / tolerance))
            part_cd_geb_value_list.append(part_cd_geb_value)
        plt.figure(0)
        plt.plot(alpha_value, part_cd_geb_value_list[0], 'r', label=r'$N_T$=10')
        plt.plot(alpha_value, part_cd_geb_value_list[1], 'g', label=r'$N_T$=100')
        plt.plot(alpha_value, part_cd_geb_value_list[2], 'b', label=r'$N_T$=1000')
        plt.plot(alpha_value, part_cd_geb_value_list[3], 'c', label=r'$N_T$=10000')
        plt.legend()
        plt.title(r'The plot of $\epsilon_\alpha$$_\beta$ vs. $\alpha$ when $N_s$=1000')
        plt.ylabel(r'$\epsilon_\alpha$$_\beta$ values')
        plt.xlabel(r'$\alpha$ values')
        plt.tight_layout()
        plt.savefig(mode + "_results.png")
        plt.show()

    elif mode == 'part_c':
        N_t, i = 100, 0
        N_s = [10, 100, 1000, 10000]
        part_cd_geb_value_list = []
        for N_si in N_s:
            N_tol = N_t + N_si
            beta = N_t / N_tol
            part_cd_geb_value = (1 - alpha_value) * d_hh + \
                                4 * np.sqrt(alpha_value ** 2 / beta + (1 - alpha_value) ** 2 / (1 - beta)) * \
                                np.sqrt(2 / N_tol * d_vc * np.log(2 * (N_tol + 1)) +
                                        2 / N_tol * np.log(8 / tolerance))
            part_cd_geb_value_list.append(part_cd_geb_value)
        plt.figure(0)
        plt.plot(alpha_value, part_cd_geb_value_list[0], 'r', label=r'$N_S$=10')
        plt.plot(alpha_value, part_cd_geb_value_list[1], 'g', label=r'$N_S$=100')
        plt.plot(alpha_value, part_cd_geb_value_list[2], 'b', label=r'$N_S$=1000')
        plt.plot(alpha_value, part_cd_geb_value_list[3], 'c', label=r'$N_S$=10000')
        plt.legend()
        plt.title(r'The plot of $\epsilon_\alpha$$_\beta$ vs. $\alpha$ when $N_T$=100')
        plt.ylabel(r'$\epsilon_\alpha$$_\beta$ values')
        plt.xlabel(r'$\alpha$ values')
        plt.tight_layout()
        plt.savefig(mode + "_results.png")
        plt.show()


def plot_d(d_hh=0.1, d_vc=10, tolerance=0.1):
    """
        Implements the drawing of the part(d).
    :param d_hh: value of symmetric difference hypothesis divergence
    :param d_vc: value of VC dimension
    :param tolerance: tolerance value
    """
    N_value = np.arange(1000, 100000, 1)
    beta_value1, beta_value2, beta_value3 = 0.01, 0.1, 0.5
    # When alpha is 0.5:
    part_cd_geb_value1 = 0.5 * d_hh + \
                         2 * np.sqrt(1 / beta_value1 + 1 / (1 - beta_value1)) * \
                         np.sqrt(2 / N_value * d_vc * np.log(2 * (N_value + 1)) +
                                 2 / N_value * np.log(8 / tolerance))
    part_cd_geb_value2 = 0.5 * d_hh + \
                         2 * np.sqrt(1 / beta_value2 + 1 / (1 - beta_value2)) * \
                         np.sqrt(2 / N_value * d_vc * np.log(2 * (N_value + 1)) +
                                 2 / N_value * np.log(8 / tolerance))
    part_cd_geb_value3 = 0.5 * d_hh + \
                         2 * np.sqrt(1 / beta_value3 + 1 / (1 - beta_value3)) * \
                         np.sqrt(2 / N_value * d_vc * np.log(2 * (N_value + 1)) +
                                 2 / N_value * np.log(8 / tolerance))
    plt.figure(0)
    #plt.plot(N_value, part_cd_geb_value1, 'r', label=r'$\beta$=0.01')
    #plt.plot(N_value, part_cd_geb_value2, 'g', label=r'$\beta$=0.1')
    #plt.plot(N_value, part_cd_geb_value3, 'b', label=r'$\beta$=0.5')
    plt.semilogx(N_value, part_cd_geb_value1, 'r', label=r'$\beta$=0.01')
    plt.semilogx(N_value, part_cd_geb_value2, 'g', label=r'$\beta$=0.1')
    plt.semilogx(N_value, part_cd_geb_value3, 'b', label=r'$\beta$=0.5')

    plt.legend()
    plt.title(r'The plot of $\epsilon_\alpha$$_\beta$ vs. N when when $\alpha$=0.5')
    plt.ylabel(r'$\epsilon_\alpha$$_\beta$ values')
    plt.xlabel(r'N values')
    plt.tight_layout()
    plt.savefig("The plot of epsilon vs. N when when alpha=0.5.png")
    plt.show()

    # When alpha is equal to beta:
    part_cd_geb_value1 = (1 - beta_value1) * d_hh + \
                         4 * np.sqrt(2 / N_value * d_vc * np.log(2 * (N_value + 1)) +
                                        2 / N_value * np.log(8 / tolerance))
    part_cd_geb_value2 = (1 - beta_value2) * d_hh + \
                         4 * np.sqrt(2 / N_value * d_vc * np.log(2 * (N_value + 1)) +
                                     2 / N_value * np.log(8 / tolerance))
    part_cd_geb_value3 = (1 - beta_value3) * d_hh + \
                         4 * np.sqrt(2 / N_value * d_vc * np.log(2 * (N_value + 1)) +
                                     2 / N_value * np.log(8 / tolerance))
    plt.figure(0)
    plt.semilogx(N_value, part_cd_geb_value1, 'r', label=r'$\beta$=0.01')
    plt.semilogx(N_value, part_cd_geb_value2, 'g', label=r'$\beta$=0.1')
    plt.semilogx(N_value, part_cd_geb_value3, 'b', label=r'$\beta$=0.5')

    plt.legend()
    plt.title(r'The plot of $\epsilon_\alpha$$_\beta$ vs. N when when $\alpha$=$\beta$')
    plt.ylabel(r'$\epsilon_\alpha$$_\beta$ values')
    plt.xlabel(r'N values')
    plt.tight_layout()
    plt.savefig("The plot of epsilon vs. N when when alpha=beta.png")
    plt.show()


def main():
    """
       The main function.
    """
    # For the part(a):
    """
    do_a_part(N_t=1, N_s=100, alpha=0.1, verbose=True)
    do_a_part(N_t=1, N_s=100, alpha=0.5, verbose=True)
    do_a_part(N_t=1, N_s=100, alpha=0.9, verbose=True)
    do_a_part(N_t=10, N_s=1000, alpha=0.1, verbose=True)
    do_a_part(N_t=10, N_s=1000, alpha=0.5, verbose=True)
    do_a_part(N_t=10, N_s=1000, alpha=0.9, verbose=True)
    do_a_part(N_t=100, N_s=10000, alpha=0.1, verbose=True)
    do_a_part(N_t=100, N_s=10000, alpha=0.5, verbose=True)
    do_a_part(N_t=100, N_s=10000, alpha=0.9, verbose=True)
    do_a_part(N_t=1000, N_s=100000, alpha=0.1, verbose=True)
    do_a_part(N_t=1000, N_s=100000, alpha=0.5, verbose=True)
    do_a_part(N_t=1000, N_s=100000, alpha=0.9, verbose=True)
    """
    # For the part(b) and the part(c):
    #plot_bc(mode='part_b')
    #plot_bc(mode='part_c')
    # For the part(d):
    plot_d()

    return


if __name__ == '__main__':
    main()