from matplotlib import pyplot as plt
import numpy as np

x = np.arange(1, 11)
y = 2 * x + 5

plt.title("Matplotlib demo")
plt.xlabel("x axis caption", loc="left")
plt.ylabel("y axis caption", loc="top")
plt.plot(x, y)
plt.show()