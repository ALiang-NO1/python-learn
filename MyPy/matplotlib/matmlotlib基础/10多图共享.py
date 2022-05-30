import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x)

# fig, ax = plt.subplots()
# ax.plot(x, y)
# ax.set_title('Simple plot')

# f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
# ax1.plot(x, y)
# ax1.set_title('Sharing y axis')
# ax2.scatter(x, y)

# fig, axs = plt.subplots(2, 2, subplot_kw=dict(projection='polar'))
# axs[0, 0].plot(x, y)
# axs[1, 1].scatter(x, y)

# plt.subplots(3, 2, sharex='col')

# plt.subplots(2, 3, sharey='row')

# plt.subplots(3, 3, sharex='all', sharey='all')

# plt.subplots(2, 2, sharex=True, sharey=True)

fig, ax = plt.subplots(num=10, clear=True)

plt.show()
