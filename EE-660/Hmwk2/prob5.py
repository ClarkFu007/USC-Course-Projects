import numpy as np
import matplotlib.pyplot as plt

# evenly sampled
err_m = np.arange(0.001, 1., 0.001)

# part (a)

y_a = np.log((1 - err_m) / err_m)
plt.figure(0)
plt.plot(err_m, y_a, 'b')
plt.title(r'The plot of $\alpha_m$ vs. $err_m$ for 0 < $err_m$ < 1')
plt.ylabel(r'$\alpha_m$')
plt.xlabel(r'$err_m$')
plt.tight_layout()
plt.savefig("The plot of alpha_m vs. err_m.png")
plt.show()

# part(b)
y_mc = (1 - err_m) / err_m
y_cc = np.ones(err_m.shape[0])
plt.figure(1)
plt.plot(err_m, y_mc, 'b', label='misclassified')
plt.plot(err_m, y_cc , 'g', label='correctly classified')
plt.legend()
plt.title(r'The plot of $g_m$ vs. $err_m$ when classifying correctly or not')
plt.ylabel(r'$g_m$')
plt.xlabel(r'$err_m$')
plt.tight_layout()
plt.savefig("The plot of g_m vs. err_m.png")
plt.show()

