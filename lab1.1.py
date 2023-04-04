from matplotlib import pyplot as plt
import numpy as np
import time as t
from scipy import spatial

N=3 #liczba szkrzydeł
#m=1 #predkosc obrotowa
M=64
m=-M/2
'''
def wykres(N,m):
    x=np.linspace(0, 2*np.pi, 1000)
    y=np.sin(N*x+(m*np.pi/10))

    plt.polar(x,y)
    plt.show(block=False)


while m<M/2:
    wykres(N,m)
    plt.pause(0.5)
    plt.close(fig=None)
    m=m+1
'''
xv, yv=np.meshgrid(np.linspace(-np.pi,np.pi,256),np.linspace(-np.pi,np.pi,256))
print(xv)