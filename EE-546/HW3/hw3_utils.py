import time
import numpy as np
from numpy import dot, sum, square, sqrt, expand_dims, fabs


def get_D(m, r):
    """
       Get the required diagonal matrix D.
    Inputs:
        the size
        the value of r
    """
    D = np.zeros((m, m), dtype="float")
    for i in range(m):
        if i + 1 <= r:
            D[i, i] = r - (i + 1) + 1
        else:
            D[i, i] = 4e-3

    return D


def generalized_power(A, row_value, r):
    """
       Utilize the generalized power method to find the A_U_r and A_V_r.
    Inputs:
        the input data matrix
        the value of the row
        the number of top eigenvectors
    Outputs:
        the objective eigen-matirx
    """
    Q = np.random.random(size=(row_value, r))  # Generate a random matrix (row_value, r)
    Q, _ = np.linalg.qr(Q)  # Perform a QR decomposition.
    for _ in range(10):
        U = np.dot(A, np.dot(A.T, Q))
        Q, _ = np.linalg.qr(U)

    return Q


def simple_power(A_r, B_r, row_value):
    """
        Utilize the power method to find the spectral norm.
    Inputs:
        the real top r eigen-matrix
        the estimated top r eigen-matrix
        the value of the row
    Outputs:
        the spectrum norm
    """
    x = np.ones((row_value, 1), dtype='float')

    for _ in range(10):
        x = dot(A_r, dot(A_r.T, dot(A_r, dot(A_r.T, x)))) \
            - dot(A_r, dot(A_r.T, dot(B_r, dot(B_r.T, x)))) \
            - dot(B_r, dot(B_r.T, dot(A_r, dot(A_r.T, x)))) \
            + dot(B_r, dot(B_r.T, dot(B_r, dot(B_r.T, x))))

    x = x / np.max(x)

    numer_value = dot(x.T, dot(A_r, dot(A_r.T, dot(A_r, dot(A_r.T, x))))) \
                  - dot(x.T, dot(A_r, dot(A_r.T, dot(B_r, dot(B_r.T, x))))) \
                  - dot(x.T, dot(B_r, dot(B_r.T, dot(A_r, dot(A_r.T, x))))) \
                  + dot(x.T, dot(B_r, dot(B_r.T, dot(B_r, dot(B_r.T, x)))))
    max_eig_value = fabs(numer_value) / dot(x.T, x)

    spec_norm = sqrt(np.squeeze(max_eig_value))

    return spec_norm


class hw3_randomizedSVD(object):
    def __init__(self, X, Y, m, n):
        self.X = X    # The matrix X
        self.Y = Y    # The matrix Y
        self.m = m    # The value of m
        self.n = n    # The value of n

    def check_c(self, r, prob):
        """
            Check how large c has to be to satisfy specifications.
        :param r: The number of top eigenvalues
        :param prob: The ith problem
        :return: The accuracy of testing patients
        """
        D = get_D(m=self.m, r=r)
        A = dot(dot(self.X, D), self.Y.T)  # Generate the matrix A: (m, n)
        A_i2_1, A_i2_2 = sum(square(A), axis=0), sum(square(A.T), axis=0)
        A_F2_1, A_F2_2 = sum(square(A)), sum(square(A.T))
        col_pdf1 = A_i2_1 / A_F2_1
        col_pdf2 = A_i2_2 / A_F2_2
        c = 1
        verbose1, verbose2 = True, True
        while True:
            select_cols1 = np.random.choice(a=self.n, size=c, p=col_pdf1)  # For U
            select_cols2 = np.random.choice(a=self.m, size=c, p=col_pdf2)  # For V
            B1, B2 = 0, 0
            for t in range(c):
                col_index1 = select_cols1[t]
                B_t1 = expand_dims(A[:, col_index1], axis=1) / sqrt(c * col_pdf1[col_index1])
                col_index2 = select_cols2[t]
                B_t2 = expand_dims(A.T[:, col_index2], axis=1) / sqrt(c * col_pdf2[col_index2])
                if t == 0:
                    B1 = B_t1
                    B2 = B_t2
                else:
                    B1 = np.hstack((B1, B_t1))
                    B2 = np.hstack((B2, B_t2))

            B_U_r = generalized_power(A=B1, row_value=self.m, r=r)
            B_V_r = generalized_power(A=B2, row_value=self.n, r=r)

            A_U_r = generalized_power(A=A, row_value=self.m, r=r)
            A_V_r = generalized_power(A=A.T, row_value=self.n, r=r)

            # Utilize the power method to find the spectral norm
            U_spec_norm = simple_power(A_r=A_U_r, B_r=B_U_r, row_value=self.m)
            # print("U_spec_norm", U_spec_norm)
            V_spec_norm = simple_power(A_r=A_V_r, B_r=B_V_r, row_value=self.n)
            # print("V_spec_norm", V_spec_norm)
            if prob == "prob_i":
                if U_spec_norm <= 0.1 and V_spec_norm <= 0.1:
                    if verbose1:
                        print("When epsilon is 0.1, the c is %d" % (c))
                        verbose1 = False
                if U_spec_norm <= 0.05 and V_spec_norm <= 0.05:
                    if verbose2:
                        print("When epsilon is 0.05, the c is %d" % (c))
                        verbose2 = False
                if U_spec_norm <= 0.01 and V_spec_norm <= 0.01:
                    print("When epsilon is 0.01, the c is %d" % (c))
                    return True

            elif prob == "prob_ii":
                if U_spec_norm <= 0.05 and V_spec_norm <= 0.05:
                    print("When r is %d, the c is %d" % (r, c))
                    return True

            else:
                print("Please input the correct problem index!")
                return False

            # print("The c=%d is finished!" % (c))
            c += 1

    def check_time(self, c, r, epsilon):
        """
            Check the running time with specific c, r, and epsilon.
        :param c: The number of drawn columns
        :param r: The number of top eigenvalues
        :param epsilon: The value of epsilon
        :return: The runnig time
        """
        D = get_D(m=self.m, r=r)
        A = dot(dot(self.X, D), self.Y.T)  # Generate the matrix A: (m, n)

        t0 = time.time()
        A_i2_1, A_i2_2 = sum(square(A), axis=0), sum(square(A.T), axis=0)
        A_F2_1, A_F2_2 = sum(square(A)), sum(square(A.T))
        col_pdf1 = A_i2_1 / A_F2_1
        col_pdf2 = A_i2_2 / A_F2_2
        select_cols1 = np.random.choice(a=self.n, size=c, p=col_pdf1)  # For U
        select_cols2 = np.random.choice(a=self.m, size=c, p=col_pdf2)  # For V
        B1, B2 = 0, 0
        for t in range(c):
            col_index1 = select_cols1[t]
            B_t1 = expand_dims(A[:, col_index1], axis=1) / sqrt(c * col_pdf1[col_index1])
            col_index2 = select_cols2[t]
            B_t2 = expand_dims(A.T[:, col_index2], axis=1) / sqrt(c * col_pdf2[col_index2])
            if t == 0:
                B1 = B_t1
                B2 = B_t2
            else:
                B1 = np.hstack((B1, B_t1))
                B2 = np.hstack((B2, B_t2))

        B_U_r = generalized_power(A=B1, row_value=self.m, r=r)
        B_V_r = generalized_power(A=B2, row_value=self.n, r=r)

        A_U_r = generalized_power(A=A, row_value=self.m, r=r)
        A_V_r = generalized_power(A=A.T, row_value=self.n, r=r)

        # Utilize the power method to find the spectral norm
        _ = simple_power(A_r=A_U_r, B_r=B_U_r, row_value=self.m)
        _ = simple_power(A_r=A_V_r, B_r=B_V_r, row_value=self.n)

        t = time.time() - t0
        print("When c is %d, r is %d, and epsilon is %f, the running time is %f" % (c, r, epsilon, t))



















