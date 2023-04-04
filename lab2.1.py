import numpy as np
import matplotlib.pyplot as plt

def y(x):
    return np.sin(x)
    #return np.sin(x**(-1))
    #return np.sign(np.sin(8*x))

def h1(x):
    #return np.where((x>=0) & (x<1), 1, 0)
    #return np.where((x>=-0.5) & (x<0.5), 1, 0)
    #return np.where((x>=-1) & (x<1), 1-abs(x), 0)
    #y = np.sin(x)/x
    #y[np.isnan(y)] = 1  #obsluga bledu: RuntimeWarning: invalid value encountered in divide
    #return y
    x = np.abs(x)
    y = np.zeros_like(x)
    mask1 = x <= 1
    mask2 = (1 < x) & (x <= 2)
    y[mask1] = 3/2 * np.abs(x[mask1])**3 - 5/2 * np.abs(x[mask1])**2 + 1
    y[mask2] = -1/2 * np.abs(x[mask2])**3 + 5/2 * np.abs(x[mask2])**2 + 2
    return y


x = np.linspace(0.05, 2*np.pi, 100)
y_orig = y(x)

xinterp = np.linspace(0.05, 2*np.pi, 100)
period = x[1] - x[0]

kern_grid = np.tile(xinterp, (len(x), 1))
offsets = np.tile(np.expand_dims(x, axis=-1), (1, len(xinterp)))
kern_grid = (kern_grid - offsets) / period

kernels = h1(kern_grid)

y_interp = np.dot(kernels, y_orig) / kernels.sum(axis=1)

rmse = np.sqrt(np.mean((y_interp - y(xinterp))**2))
print(f'RMSE = {rmse:.5f}')

plt.plot(x, y(x),'.',x, y(x),'-',xinterp, y_interp,'--')
plt.legend(['data', 'orginal', 'interpolation'], loc = 'best')
plt.show()
