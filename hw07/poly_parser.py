#!/usr/bin/python

#################################################
# module: poly_parser.py
# bugs to vladimir dot kulyukin in canvas
#################################################

from functools import reduce
import re

from maker import maker

class poly_parser(object):

    @staticmethod
    def parse_elt(elt):
        # let's make sure that elt is a string.
        assert isinstance(elt, str)

        elt = re.sub(r'\s', '', elt)
        elt = re.sub(r'-\+', r'-', elt)
        elt = re.sub(r'\+-', r'-', elt)

        var = next(c for c in elt if c.isalpha())
        var_i = elt.index(var)

        const = float(elt[:var_i])
        deg = float(elt[var_i + 2:])

        return maker.make_prod(
            maker.make_const(const),
            maker.make_pwr(var, deg))


    @staticmethod
    def parse_sum(poly_str):
        assert isinstance(poly_str, str)

        prod_pat = r"[+-]?\s*-?\d*(\.\d*)?[a-z]\^-?\d*(\.\d*)?"

        return reduce(maker.make_plus,
            map(lambda match: poly_parser.parse_elt(match[0]),
            re.finditer(prod_pat, poly_str)))
