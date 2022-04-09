
#################################################
# module: cs3430_s22_hw03.py
# Carson Fox
# A02251670
##################################################

from itertools import combinations

import numpy as np
import matplotlib.pyplot as plt
from cs3430_s22_hw01 import gje

## =============== Problem 01 ==================

def line_ip(line1, line2):
    A = np.array([line1[:-1], line2[:-1]], dtype=float)
    b = np.array([line1[-1:], line2[-1:]], dtype=float)
    return gje(A, b)

### This is the same as the static method
### cs3430_s22_hw03_uts.check_line_ip(line1, line2, ip, err=0.0001)
### in cs3430_s22_hw03_uts.py. This is for your
### convenience.
def check_line_ip(line1, line2, ip, err=0.0001):
    assert ip is not None
    A1, B1, C1 = line1
    A2, B2, C2 = line2
    x = ip[0, 0]
    y = ip[1, 0]
    assert abs((A1*x + B1*y) - C1) <= err
    assert abs((A2*x + B2*y) - C2) <= err
    return True

## Be careful not to compute the same intersection twice.
## In other words, if l1 and l2 are two lines, the
## intersection point b/w l1 and l2 is the same as the
## intersection point b/w l2 and l1. Computing duplicate
## intersections will not render the required computation
## incorrect, but it will make it more efficient.
def find_line_ips(lines):
    return [line_ip(a, b) for a, b in combinations(lines, 2)]

## For problems 2.1 and 2.2
def max_obj_fun(f, cps):
    """
    maximize obj fun f on corner points cps
    """
    return max(((point, f(*point)) for point in cps), key=lambda pair: pair[1])

## =============== Problem 02 ==================

### Graphing constraints to the Ted's Toys problem we worked
### out in CS3430: S22: Lecture 05.
def plot_teds_constraints():
    ### plastic constraint: 4x + 3y <= 480
    def plastic_constraint(x): return -(4/3.0)*x + 160.0
    ### steel constraints: 3x + 6y <= 720
    def steel_constraint(x): return -0.5*x + 120.0
    xvals  = np.linspace(0, 160, 10000)
    yvals1 = np.array([plastic_constraint(x) for x in xvals])
    yvals2 = np.array([steel_constraint(x) for x in xvals])
    fig1   = plt.figure(1)
    fig1.suptitle('Ted\'s Toys Problem')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([-5, 160])
    plt.xlim([-5, 160])
    ## x = 0
    x1, y1 = [0, 0], [0, 160]
    ## y = 0
    x2, y2 = [0, 160], [0, 0]
    plt.grid()
    plt.plot(xvals, yvals1, label='4x+3y=480', c='red')
    plt.plot(xvals, yvals2, label='3x+6y=720', c='blue')
    plt.plot(x1, y1, label='x=0', c='green')
    plt.plot(x2, y2, label='y=0', c='yellow')
    plt.legend(loc='best')
    plt.show()

def teds_problem():
    red_line    = (4, 3, 480)
    blue_line   = (3, 6, 720)
    green_line  = (1, 0, 0)
    yellow_line = (0, 1, 0)

    cp1 = line_ip(green_line, yellow_line)
    cp2 = line_ip(green_line, blue_line)
    cp3 = line_ip(blue_line, red_line)
    cp4 = line_ip(red_line, yellow_line)

    obj_fun = lambda x, y: 5.0*x + 4.0*y

    rslt = max_obj_fun(obj_fun, [cp1, cp2, cp3, cp4])

    x = rslt[0][0][0]
    y = rslt[0][1][0]
    p = rslt[1]

    print('num cars   = {}'.format(x))
    print('num trucks = {}'.format(y))
    print('profit     = {}'.format(p))

    return x, y, p

def plot_2_1_constraints():
    ### constraint 1: x + y >= 3
    def constraint_1(x): return 3 - x
    ### constraint 2: 3x - y >= -1
    def constraint_2(x): return 3*x + 1

    xvals  = np.linspace(0, 3, 10000)
    yvals1 = np.array([constraint_1(x) for x in xvals])
    yvals2 = np.array([constraint_2(x) for x in xvals])
    fig1   = plt.figure(2)
    fig1.suptitle('Problem 2.1')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([0, 8])
    plt.xlim([0, 3])
    ## x = 2
    x1, y1 = [2, 2], [0, 8]
    plt.grid()
    plt.plot(xvals, yvals1, label='x + y = 3', c='red')
    plt.plot(xvals, yvals2, label='3x - y = -1', c='blue')
    plt.plot(x1, y1, label='x=2', c='green')
    plt.legend(loc='best')
    plt.show()

def problem_2_1():
    lines = [(1, 1, 3),
    (3, -1, -1),
    (1, 0, 2)]

    cps = find_line_ips(lines)

    obj_fun = lambda x, y: 3.0*x + y

    rslt = max_obj_fun(obj_fun, cps)

    x = rslt[0][0][0]
    y = rslt[0][1][0]
    p = rslt[1]

    return x, y, p

def plot_2_2_constraints():
    ### constraint 1: x + 2y = 6
    def constraint_1(x): return (6 - x) / 2
    ### constraint 2: x - y = -4
    def constraint_2(x): return x + 4
    ### constraint 3: 2x + y = 8
    def constraint_3(x): return 8 - 2*x

    xvals  = np.linspace(0, 10, 10000)
    yvals1 = np.array([constraint_1(x) for x in xvals])
    yvals2 = np.array([constraint_2(x) for x in xvals])
    yvals3 = np.array([constraint_3(x) for x in xvals])
    fig1   = plt.figure(3)
    fig1.suptitle('Problem 2.2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([-.1, 10])
    plt.xlim([-.1, 10])
    ## x = 0
    x1, y1 = [0, 0], [0, 10]
    ## y = 0
    x2, y2 = [0, 10], [0, 0]
    plt.grid()
    plt.plot(xvals, yvals1, label='x + 2y = 6', c='red')
    plt.plot(xvals, yvals2, label='x - y = -4', c='blue')
    plt.plot(xvals, yvals3, label='2x + y = 8', c='purple')
    plt.plot(x1, y1, label='x=0', c='green')
    plt.plot(x2, y2, label='y=0', c='yellow')
    plt.legend(loc='best')
    plt.show()

def problem_2_2():
    red_line = (1, 2, 6)
    blue_line = (1, -1, -4)
    purple_line = (2, 1, 8)
    green_line = (1, 0, 0)

    cp1 = line_ip(green_line, red_line)
    cp2 = line_ip(green_line, blue_line)
    cp3 = line_ip(purple_line, red_line)
    cp4 = line_ip(purple_line, blue_line)

    obj_fun = lambda x, y: x + y

    rslt = max_obj_fun(obj_fun, [cp1, cp2, cp3, cp4])

    x = rslt[0][0][0]
    y = rslt[0][1][0]
    p = rslt[1]

    return x, y, p

## For problem 2.3
def min_obj_fun(f, cps):
    """
    minimize obj fun f on corner points cps
    """
    return min(((point, f(*point)) for point in cps), key=lambda pair: pair[1])

def plot_2_3_constraints():
    ### constraint 1: 0.8x + .2y >= 90
    def constraint_1(x): return 450 - 4*x
    ### constraint 2: 3x + 6y >= 600
    def constraint_2(x): return (200 - x) / 2

    xvals  = np.linspace(0, 500, 10000)
    yvals1 = np.array([constraint_1(x) for x in xvals])
    yvals2 = np.array([constraint_2(x) for x in xvals])
    fig1   = plt.figure(4)
    fig1.suptitle('Problem 2.3')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([-10, 460])
    plt.xlim([-10, 120])
    ## x = 0
    x2, y2 = [0, 120], [0, 0]
    ## y = 0
    x1, y1 = [0, 0], [0, 460]
    plt.grid()
    plt.plot(xvals, yvals1, label='0.8x + .2y >= 90', c='red')
    plt.plot(xvals, yvals2, label='3x + 6y >= 600', c='blue')
    plt.plot(x1, y1, label='x=0', c='green')
    plt.plot(x2, y2, label='y=0', c='yellow')
    plt.legend(loc='best')
    plt.show()

def problem_2_3():
    red_line    = (.8, .2, 90)
    blue_line   = (3, 6, 600)
    green_line  = (1, 0, 0)
    yellow_line  = (0, 1, 0)

    cp1 = line_ip(green_line, red_line)
    cp2 = line_ip(yellow_line, blue_line)
    cp3 = line_ip(blue_line, red_line)

    obj_fun = lambda x, y: 4.0*x + 5.0*y

    print([cp1, cp2, cp3])

    rslt = min_obj_fun(obj_fun, [cp1, cp2, cp3])

    x = rslt[0][0][0]
    y = rslt[0][1][0]
    p = rslt[1]

    return x, y, p