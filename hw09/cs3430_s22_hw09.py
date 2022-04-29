#!/usr/bin/python
# -*- coding: utf-8 -*-

######################################
# module: cs3430_s22_hw09.py
# description: cs3430 s22 hw09
# Carson Fox
# A02251670
# bugs to vladimir kulyukin in canvas
######################################


def make_equiv_class_mod_n(a, n):
    """
    make_equiv_class_mod_n(a, n) returns a generator object
    to generate [a]_n (i.e., the equivalence class of a modulo n).
    """
    assert n > 0

    def gen_equiv_class(k):
        kk = k
        while True:
            yield a + kk * n
            if kk == 0:
                kk += 1
            elif kk > 0:
                kk *= -1
            elif kk < 0:
                kk *= -1
                kk += 1

    return gen_equiv_class(0)


def xeuc(a, b):
    """
    extended euclid algo that returns g, x, y such
    g = gcd(a,b) and g = ax + by.
    """
    oldx, x = 1, 0
    oldy, y = 0, 1

    while b != 0:
        q = a//b
        x, oldx = oldx - q*x, x
        y, oldy = oldy - q*y, y
        a, b = b, a % b

    return a, oldx, oldy


def mult_inv_mod_n(a, n):
    """
    compute the multiplicative inverse of a mod n.
    """
    g, x, _ = xeuc(a, n)
    return make_equiv_class_mod_n(x, n) if g == 1 else None


def solve_cong(a, b, m, tmax=10):
    """
    solves the congruence ax <> b (mod m);
    returns at most tmax equivalence classes.
    """
    g, u, _ = xeuc(a, m)
    if b % g != 0: return None
    return [make_equiv_class_mod_n((b//g)*u + t*(m//g), m) for t in range(min(g, tmax))]
