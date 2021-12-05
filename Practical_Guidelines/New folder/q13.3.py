import numpy as np
import matplotlib.pyplot as plt

a = 5
b = 2
c = 1
x = np.linspace(0, 10, 256, endpoint = True)
y = (a * np.exp(-b*x)) + c

plt.plot(x, y, '-r', label=r'$y = 5e^{-2x} + 1$')

axes = plt.gca()
axes.set_xlim([x.min(), x.max()])
axes.set_ylim([y.min(), y.max()])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Exponential Curve')
plt.legend(loc='upper left')

plt.show()