####################################
# module: rmb.py
# Carson Fox
# A02251670
####################################

from functools import cache

import numpy as np


class rmb(object):
    @cache
    @staticmethod
    def rjl(f, a, b, j, l):
        if l == 1:
            n = 2 ** (j - 1)
            h = (b - a) / n
            a, b, h = map(np.longdouble, (a, b, h))
            return h / 2 * (f(a) + 2 * sum(f(a + i * h) for i in range(1, n)) + f(b))
        else:
            return rmb.rjl(f, a, b, j, l - 1) + (
                rmb.rjl(f, a, b, j, l - 1) - rmb.rjl(f, a, b, j - 1, l - 1)
            ) / (4 ** (l - 1) - 1)
