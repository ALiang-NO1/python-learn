import numpy as np
from matplotlib import pyplot as plt

x = np.array([0, 6])
y = np.array([0, 100])

plt.subplot(2, 2, 1)
plt.title("plot 1")
plt.plot(x, y)

x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])
plt.subplot(2, 2, 2)
plt.title('plot 2')
plt.plot(x, y)

x = np.array([1, 2, 3, 4])
y = np.array([3, 5, 7, 9])
plt.subplot(2, 2, 3)
plt.title('plot 3')
plt.plot(x, y)

x = np.array([1, 2, 3, 4])
y = np.array([4, 5, 6, 7])
plt.subplot(2, 2, 4)
plt.title('plot 4')
plt.plot(x, y)

plt.suptitle('multi-pic test')
plt.show()
