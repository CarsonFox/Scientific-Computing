
#############################################
# Module: nra.py
# Description: Newton-Raphson Algorithm
#############################################

import numpy as np
import math
from maker import maker
from pwr import pwr
from prod import prod
from var import var
from const import const
from plus import plus
from drv import drv
from poly_parser import poly_parser
from tof import tof

class nra(object):

    @staticmethod
    def zr1(fstr, x0, num_iters=3):
        f: plus = poly_parser.parse_sum(fstr)
        df: plus = drv.drv(f)
        f, df = tof.tof(f), tof.tof(df)

        guess = 1
        for _ in range(num_iters):
            guess = guess - f(guess)/df(guess)
        return guess

    @staticmethod
    def zr2(fstr, x0, delta=0.0001):
        f: plus = poly_parser.parse_sum(fstr)
        df: plus = drv.drv(f)
        f, df = tof.tof(f), tof.tof(df)

        guess = 1
        difference = 2*delta
        iterations = 0

        while difference > delta:
            new_guess = guess - f(guess)/df(guess)
            difference = abs(guess - new_guess)

            guess = new_guess
            iterations += 1

        return guess, iterations

    @staticmethod
    def check_zr(fstr, zr, err=0.0001):
        return abs(tof.tof(poly_parser.parse_sum(fstr))(zr) - 0.0) <= err 
