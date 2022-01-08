import numpy as np
import matplotlib.pyplot as plt


def display(w, Xtest, Ytest, norm, saved_name, levels=None,
            w1_range=(-4.0, 6.1, 100), w2_range=(-4.0, 6.1, 100)):
    w = np.array(w)

    w1list = np.linspace(w1_range[0], w1_range[1], num=w1_range[2])
    w2list = np.linspace(w2_range[0], w2_range[1], num=w2_range[2])
    W1, W2 = np.meshgrid(w1list, w2list)
    # print(W1.shape)(100, 100)
    # print(W2.shape)(100, 100)

    Z = np.stack((w[0] * np.ones(W1.shape), W1, W2), axis=0)

    # print(Z.shape)(3, 100, 100)
    Z = Z.reshape((Z.shape[0], -1))
    # print(Z.shape)(3, 10000)
    Z = np.matmul(Xtest, Z) - Ytest.reshape((len(Ytest), 1))
    Z = np.square(Z)
    Z = np.sum(Z, axis=0, keepdims=False) / Xtest.shape[0]
    Z = Z.reshape(W1.shape)

    if norm == 'l2':
        W_norm = np.square(W1) + np.square(W2)
    elif norm == 'l1':
        W_norm = np.abs(W1) + np.abs(W2)
    else:
        raise RuntimeError('Unimplemented norm. Please enter "l1" or "l2".')

    plt.figure()

    mse_ori = np.mean(np.square(np.dot(Xtest, w) - Ytest))

    levels = [mse_ori, mse_ori + 10]
    contour = plt.contour(W1, W2, Z, levels, colors='k')
    plt.clabel(contour, colors='k', fmt='%2.1f', fontsize=12)

    if norm == 'l2':
        levels = [np.sum(np.square(w[1:]))]
    elif norm == 'l1':
        levels = [np.sum(abs(w[1:]))]
    else:
        raise RuntimeError('Unimplemented norm. Please enter "l1" or "l2".')

    contour = plt.contour(W1, W2, W_norm, levels, colors='r')
    plt.clabel(contour, colors='r', fmt='%2.1f', fontsize=12)
    plt.plot(w[1], w[2], marker=".", markersize=8)

    plt.title('Plot for 2D case')
    plt.xlabel('$w_1$')
    plt.ylabel('$w_2$')
    plt.axis('square')
    plt.tight_layout()
    plt.savefig(saved_name)
    plt.show()
    return