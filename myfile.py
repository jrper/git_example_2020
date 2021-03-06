import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)

plt.plot(x, np.sin(x), ls='r')
plt.plot(x, np.cos(x))
plt.show()
