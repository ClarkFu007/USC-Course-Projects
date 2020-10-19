import matplotlib.pyplot as plt
import numpy as np
x = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([[0.6512], [0.6281], [0.5915], [0.5205], [0.4028], [0.1302]])
plt.figure()
plt.xlim(0, 7)
plt.ylim(0, 0.7)
plt.plot(x, y, linestyle='solid', color='blue', marker='o',
         markerfacecolor='green', markeredgecolor='green')
plt.title("The test curve of different numbers of train images in Module2&3")
plt.ylabel("The values of test accuracy")
plt.xlabel("The ith situation")
plt.savefig("The test accuracy curve")
plt.show()