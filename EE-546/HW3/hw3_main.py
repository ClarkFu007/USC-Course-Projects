import random
import numpy as np
from scipy.stats import special_ortho_group

m, n = 1000, 100000
# np.random.seed(seed=546)
X = special_ortho_group.rvs(m)
print("X.shape", X.shape)
Y = np.random.random(size=(n, m))  # Generate a random matrix (n, m)
Y, _ = np.linalg.qr(Y)  # Perform a QR decomposition.
print("Y.shape", Y.shape)

from hw3_utils import hw3_randomizedSVD
hw3_solver = hw3_randomizedSVD(X=X, Y=Y, m=m, n=n)

for i in range(10):
    print("The results of the iteration %d" % (i+1))
    hw3_solver.check_c(r=10, prob="prob_i")
    hw3_solver.check_c(r=2, prob="prob_ii")
    hw3_solver.check_c(r=5, prob="prob_ii")
    hw3_solver.check_c(r=15, prob="prob_ii")
    hw3_solver.check_c(r=20, prob="prob_ii")
    print("  ")

for i in range(10):
    print("The results of the iteration %d" % (i + 1))
    hw3_solver.check_time(c=13, r=10, epsilon=0.1)
    hw3_solver.check_time(c=18, r=10, epsilon=0.05)
    hw3_solver.check_time(c=195, r=10, epsilon=0.01)
    hw3_solver.check_time(c=10, r=2, epsilon=0.05)
    hw3_solver.check_time(c=14, r=5, epsilon=0.05)
    hw3_solver.check_time(c=23, r=15, epsilon=0.05)
    hw3_solver.check_time(c=28, r=20, epsilon=0.05)
    print("  ")

import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(12, 8))
r = [2, 5, 15, 20]
c = [10, 14, 23, 28]
ax.plot(r, c, marker='*', linestyle="solid", markersize=18)
ax.set_xlabel('r')
ax.set_ylabel('c (minimum)')
fig.tight_layout()
fig.savefig('r_vs_c.png')




















