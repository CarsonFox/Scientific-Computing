#!/usr/bin/python

#################################################
# module: tof.py
# bugs to vladimir kulyukin in canvas.
#################################################

from var import var
from pwr import pwr
from const import const
from plus import plus
from prod import prod

class tof(object):

    @staticmethod
    def const_tof(fr):
        """convert a const object to Py function."""
        assert isinstance(fr, const)

        return lambda _: fr.get_val()


    @staticmethod
    def var_tof(fr):
        """convert a var object to Py function."""
        assert isinstance(fr, var)

        return lambda x: x


    @staticmethod
    def prod_tof(fr):
        """convert a prod object to Py function."""
        assert isinstance(fr, prod)

        lhs = tof.tof(fr.get_mult1())
        rhs = tof.tof(fr.get_mult2())
        return lambda x: lhs(x) * rhs(x)


    @staticmethod
    def plus_tof(fr):
        """convert a plus object to a Py function."""
        assert isinstance(fr, plus)

        lhs = tof.tof(fr.get_elt1())
        rhs = tof.tof(fr.get_elt2())
        return lambda x: lhs(x) + rhs(x)


    @staticmethod
    def pwr_tof(fr):
        """convert a pwr object to a Py function."""
        assert isinstance(fr, pwr)

        deg = fr.get_deg().get_val()
        assert(isinstance(deg, float))

        return lambda x: x**deg


    @staticmethod
    def tof(fr):
        """convert a const/var/prod/plus/pwr/ object to a Py function."""
        if isinstance(fr, const):
            return tof.const_tof(fr)
        elif isinstance(fr, var):
            return tof.var_tof(fr)
        elif isinstance(fr, prod):
            return tof.prod_tof(fr)
        elif isinstance(fr, plus):
            return tof.plus_tof(fr)
        elif isinstance(fr, pwr):
            return tof.pwr_tof(fr)
        else:
            raise Exception(f"Unknown FR type: {type(fr)}")
