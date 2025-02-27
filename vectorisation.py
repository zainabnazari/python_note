#file name: vectorisation.py
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5.0,5.,1000.0)
def f(x):
    return -x * (2.0 - 8.0 * np.exp(- (x**2)/6.0))
f2= np.vectorize(f)
plt.plot(x, f2(x))
plt.show()
