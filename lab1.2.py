from matplotlib import pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from sklearn.metrics import mean_squared_error



lst=[]

def kernel(x):
    for i in x:
        if i>=0 and i<1:
            i=1
        else:
            i=0
        lst.append(i)
    print(lst)

x=np.linspace(0.05,2*np.pi,100)
y=np.sin(x)    

y1=np.sin(x**-1)
y2=np.sign(np.sin(8*x))

'''
n=20
x_interp=np.linspace(x[0],x[-1],n)

interp_methods = ['linear', 'nearest', 'zero', 'slinear', 'quadratic', 'cubic']
rmse_values = []

for method in interp_methods:
    f = interp1d(x, y2, kind=method)
    y_interp = f(x_interp)
    rmse = np.sqrt(np.mean((y_interp - np.sign(np.sin(8*x_interp)))**2))
    rmse_values.append(rmse)


for i in range(len(interp_methods)):
    print(f'Metoda interpolacji {interp_methods[i]}: RMSE = {rmse_values[i]:.5f}')

f = interp1d(x, y2, kind='zero')
y_interp = f(x_interp)
plt.plot(x,y2,'.',x,y2,'-',x_interp,y_interp,'--')
plt.legend(['data', 'orginal', 'interpolation'], loc = 'best')
plt.show()

'''

n_values=[10,20,30,40,50,100,200,300,500,700,1000,1000000]
rmse_values = []

for n in n_values:
    x_interp=np.linspace(x[0],x[-1],n)
    f = interp1d(x, y2, kind='linear')
    y_interp = f(x_interp)
    rmse = np.sqrt(np.mean((y_interp - np.sign(np.sin(8*x_interp)))**2))
    rmse_values.append(rmse)

for i in range(len(n_values)):
    print(f'{rmse_values[i]:.5f}')

x_interp=np.linspace(x[0],x[-1],1000)
f = interp1d(x, y1, kind='linear')
y_interp = f(x_interp)
plt.plot(x,y1,'.',x,y1,'-',x_interp,y_interp,'--')
plt.legend(['data', 'orginal', 'interpolation'], loc = 'best')
plt.show()

"""



period=x[1]-x[0]
kernel_grid=np.tile(x_interp,(len(x),1))

offsets=np.tile(np.expand_dims(x, axis=-1), (1,len(x_interp)))

kernel_grid=(kernel_grid-offsets)/period #sekwencja kerneli


#print(kernel_grid)
#print(x_interp)
#print(kernel(x_interp))

#x_interp_convlove=convolve(x_interp, kernel(x_interp), mode='same')

#x_interp_values=x_interp_convlove[:len(x)]
kernel_x=np.apply_over_axes(np.max,kernel_grid, [1,1,0])

#apply over function
#kernels=kernel(kernel_grid)

print(kernel_x)


#plt.plot(x,y2)
#plt.plot(x,y2,'o')
#plt.plot(x_interp,interpolation(x_interp))
#plt.show()
"""
