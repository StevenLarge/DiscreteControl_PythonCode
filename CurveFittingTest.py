#This is a test script for the scipy optimization functions
#
#Steven Large
#February 5th 2018

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x,a,b,c):

	return a*np.exp(-b*x) + c

xdata = np.linspace(0,4,50)

y = func(xdata,2.5,1.3,0.5)

np.random.seed(1729)

y_noise = 0.2 * np.random.normal(size=xdata.size)

ydata  = y + y_noise

plt.plot(xdata, ydata, 'b-', label='data')

popt,pcov = curve_fit(func, xdata, ydata, bounds=(0,[3., 1.5, 0.5]))

print popt[0]
print popt[1]
print popt[2]

plt.plot(xdata,func(xdata, *popt), 'r-', label='fit')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.show()


