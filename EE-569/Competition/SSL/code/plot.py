import matplotlib.pyplot as plt
import numpy as np
x = np.array([[1], [2], [3], [4]])
y = np.array([[0.7924], [0.7578], [0.5417], [0.4622]])
plt.figure()
plt.xlim(0, 6)
plt.ylim(0, 0.9)
plt.plot(x, y, linestyle='solid', color='blue', marker='o',
         markerfacecolor='green', markeredgecolor='green')
plt.title("The test curve of different numbers of train images")
plt.ylabel("The values of test accuracy")
plt.xlabel("The ith situation")
plt.savefig("The test accuracy curve")
plt.show()