
####################################
# module: cdd.py
# Carson Fox
# A02251670
####################################

import numpy as np

class cdd(object):

    @staticmethod
    def drv1_ord2(f, x, h):
        x, h = map(np.longdouble, [x, h])
        return (f(x + h) - f(x - h)) / (2*h)

    @staticmethod
    def drv1_ord4(f, x, h):
        x, h = map(np.longdouble, [x, h])
        return (-f(x + 2*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2*h)) / (12*h)

    @staticmethod
    def drv2_ord2(f, x, h):
        x, h = map(np.longdouble, [x, h])
        return (f(x + h) - 2*f(x) + f(x - h)) / h**2

    @staticmethod
    def drv2_ord4(f, x, h):
        x, h = map(np.longdouble, [x, h])
        return (-f(x + 2*h) + 16*f(x + h) - 30*f(x) + 16*f(x - h) - f(x - 2*h)) / (12*h**2)

    

    

    

    
        
    
