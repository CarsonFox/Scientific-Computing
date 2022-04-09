###############################################
# module: drv.py
# module: a simple differentiation engine
###############################################

import numpy as np
import math
from maker import maker
from pwr import pwr
from prod import prod
from var import var
from const import const
from plus import plus

class drv(object):

    @staticmethod
    def drv(expr):
        if isinstance(expr, const):
            return drv.drv_const(expr)
        elif isinstance(expr, pwr):
            return drv.drv_pwr(expr)
        elif isinstance(expr, prod):
            return drv.drv_prod(expr)
        elif isinstance(expr, plus):
            return drv.drv_plus(expr)
        else:
            raise Exception('drv:' + str(expr))

    @staticmethod
    def drv_const(expr: const):
        return maker.make_const(0)

    @staticmethod
    def drv_pwr(expr: pwr):
        b = expr.get_base().get_name()
        d = expr.get_deg().get_val()

        if d != 0: d -= 1
        return maker.make_pwr(b, d)

    @staticmethod
    def drv_prod(expr: prod):
        c = expr.get_mult1().get_val()
        p = expr.get_mult2()

        return maker.make_prod(
            maker.make_const(c * p.get_deg().get_val()),
            drv.drv(p))


    @staticmethod
    def drv_plus(expr: plus):
        m1 = expr.get_elt1()
        m2 = expr.get_elt2()

        return maker.make_plus(drv.drv(m1), drv.drv(m2))
