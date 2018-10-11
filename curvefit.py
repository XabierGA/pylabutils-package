# Variables have to be x and y, with y = f(x)
# y has to be left alone in the first term of the equation
# Parameters go in CAPS (unfortunately they cannot have numbers
# in their names, like A1, A2. You have to choose different letters, like
# AA, AB, etc.), number constants go between square brackets.
# For example: y = np.exp(TA / x + TB / x) + CP * [np.e]
# here TA, TB and CP are parameters and np.e is obviously a constant.

import re
import copy
import numpy as np
import scipy.optimize as so

def curvefit(func, x, y, dev, *guess):

    parms = re.findall('[A-Z]+', func)
    nums = re.findall('\['+'[^\]]+'+'\]', func)

    if not guess:
        guess = [1] * len(parms)

    def curve(x, *values):

        tempcurve = copy.copy(func)

        for i in range(len(parms)):
            tempcurve = re.sub(parms[i], str(values[i]), tempcurve)
        for i in range(len(nums)):
            tempcurve = re.sub('\\' + nums[i][:-1] + '\\]', nums[i][1:-1], tempcurve)

        if '= ' in tempcurve:
            y = eval(tempcurve[tempcurve.find('=')+1:])
        else:
            y = eval(tempcurve[tempcurve.find('='):])
        return y

    sols = so.curve_fit(curve, x, y, p0 = guess, sigma = dev, absolute_sigma = True)
    return [sols[0], np.sqrt(np.diag(sols[1]))]



# To do:
# Allow more freedom at naming variables and parameters
# and at writing equations
# Introduce graphical representation
