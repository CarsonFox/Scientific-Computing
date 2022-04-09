###################################
## module: cs3430_s22_midterm02.py
## Carson Fox
## A02251670
#####################################

from math import pi, sin, cos
import numpy as np
import matplotlib.pyplot as plt

from poly_parser import poly_parser
from tof import tof
from drv import drv
from nra import nra
from cdd import cdd
from rmb import rmb

## ========= Problem 1 ========================

def lambdify(s):
    poly = poly_parser.parse_sum(s)
    return tof.tof(poly)

## ========== Problem 2 ========================

def diff(s):
    poly = poly_parser.parse_sum(s)
    derivative = drv.drv(poly)
    return tof.tof(derivative)

## ========== Problem 3 ========================

def nra_approx(s, x, num_iters=5):
    return nra.zr1(s, x, num_iters=num_iters)

## ========== Problem 4 ========================

def cdd_drv1_ord2(f, x, h):
    return cdd.drv1_ord2(f, x, h)

def cdd_drv1_ord4(f, x, h):
    return cdd.drv1_ord4(f, x, h)

def cdd_drv2_ord2(f, x, h):
    return cdd.drv2_ord2(f, x, h)

def cdd_drv2_ord4(f, x, h):
    return cdd.drv2_ord4(f, x, h)

### ========= Problem 5 =========================

'''
              R(4, 4)                   -- Level 4
             /      \
          R(3,3)   R(4, 2)              -- Level 3
         /      \   /    \
    R(2,2)      R(3,2)   R(3, 1)        -- Level 2
    /    \     /    \   /     \
 T(1,1)   T(2,1)   T(3,1)     T(4, 1)   -- Level 1

'''

## ========== Problem 6 ========================

def fourier_nth_partial_sum(f, fstr, num_points, num_coeffs, rn):
    a = lambda n: rmb.rjl(lambda x: f(x)*cos(n*x), -pi, pi, rn, rn)/pi
    b = lambda n: rmb.rjl(lambda x: f(x)*sin(n*x), -pi, pi, rn, rn)/pi
    
    a0 = a(0)
    a_coeffs = [a(k) for k in range(1, num_coeffs + 1)]
    b_coeffs = [b(k) for k in range(1, num_coeffs + 1)]
    return lambda x: a0/2 + sum(a_coeffs[k - 1]*cos(k*x) + b_coeffs[k - 1]*sin(k*x) for k in range(1, num_coeffs + 1))

def plot_fourier_nth_partial_sum(f, fstr, num_points=10000, num_coeffs=3, rn=15):
    sn = fourier_nth_partial_sum(f, fstr, num_points, num_coeffs, rn)

    fig = plt.figure(1)
    fig.suptitle(f'{fstr} on [-pi, pi]; num_coeffs={num_coeffs}, rn={rn}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()

    xvals = np.linspace(-pi, pi, num_points)
    plt.plot(xvals, [f(x) for x in xvals], label=f'{fstr}', c='r')
    plt.plot(xvals, [sn(x) for x in xvals], label='nth partial sum', c='b')

    plt.show()

def plot_fourier_nth_partial_sum_error(f, fstr, num_points=10000, num_coeffs=3, rn=15):
    sn = fourier_nth_partial_sum(f, fstr, num_points, num_coeffs, rn)

    fig = plt.figure(2)
    fig.suptitle(f'True error for {fstr} on [-pi, pi]; num_coeffs={num_coeffs}, rn={rn}')
    plt.xlabel('x')
    plt.ylabel('error')
    plt.grid()

    xvals = np.linspace(-pi, pi, num_points)
    plt.plot(xvals, [f(x) - sn(x) for x in xvals], label=f'{fstr}', c='r')

    plt.show()

### =============== Problem 7 =========================

"""
a) The basic trigonometric system is the system {1, cos(x), sin(x), cos(2x), sin(2x), ...cos(nx), sin(nx)},
and they have common period 2*pi.

b) f(x) and g(x) are orthogonal on an interval [a, b] when
the integral of the product f(x)*g(x) over that interval is zero.
"""

### =============== Problem 8 =========================

"""
f(x) = 2sin(3x + pi/3). Then A = 2, w = 3, and phi = pi/3. So sin(phi) = sqrt(3)/2,
and cos(phi) = 1/2. Thus f(x) = 2(cos(3x) * sqrt(3)/2 + sin(3x) * 1/2), or
f(x) = sqrt(3)*cos(3x) + sin(3x).
"""
