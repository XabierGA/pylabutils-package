# To do:
# Allow more freedom at naming variables and parameters
# Introduce graphical representation

import re
import copy
import numpy as np
import scipy.optimize as so

# Function has to be string
# Function has to start by 'y = []'
# where y (can be any other letter) is the returning variable and
# [] is the rest of the function

def curvefit(func, x, y, dev, *guess):

    parms = re.findall('[A-Z]+', func)
    nums = re.findall('\['+'[^\]]+'+'\]', func)

    if not guess:
        guess = [1] * len(parms)

    def curve(x, *values):

        tempcurve = copy.copy(func)

        for i in range(len(parms)):
            re.sub(parms[i], guess[i], tempcurve)
        for i in range(len(nums)):
            re.sub(nums[i], nums[i][1:-1])

        if '= ' in tempf:
            y = eval(tempf[tempf.find('=')+1:])
        else:
            y = eval(tempf[tempf.find('='):])
        return y

    sols = so.curve_fit(curve, x, y, p0 = guess, sigma = dev, absolute_sigma = True)
    results = [(sol[0][i], np.sqrt(np.diag(sol[1][i]))) for i in (1, 2) for sol in sols]
    return results


myf = 'y = A * x + B'
ydata = (2, 4, 6, 8)
xdata = (3, 4, 5, 6)
ddata = (0.1, 0.1, 0.1, 0.1)

curvefit(myf, xdata, ydata, ddata)
