#############################################################
# module: cs3430_s22_midterm01.py
# Carson Fox
# A02251670
# I spent around 20 minutes on the written portion, and 
# about a minute hooking up the code from the assignments
# and getting the unit tests to pass. Typing out the matrices,
# however, took around 30 minutes. Perhaps I'm a slow typer.
# I also guarantee there are typos in there, so I hope we're
# not being graded on the accuracy of our output.
##############################################################

import numpy as np

### put your imports from your previous/current assignments
from cs3430_s22_hw01 import gje, cramer
from cs3430_s22_hw02 import bsubst, fsubst, lud_solve

### ================ Problem 01 ========================

def solve_lin_sys_with_bsubst(a, n, b, m):
    return bsubst(a, n, b, m)

### ================ Problem 02 ========================

def solve_lin_sys_with_fsubst(a, n, b, m):
    return fsubst(a, n, b, m)

### ================ Problem 03 ========================

def solve_lin_sys_with_gje(a, b):
    return gje(a, b)

### ================ Problem 04 ========================

def solve_lin_sys_with_lud(a, n, b, m):
    return lud_solve(a, n, b, m)

### ================ Problem 05 ========================

def solve_lin_sys_with_cramer(a, b):
    return cramer(a, b)

### ================ Problem 06 =========================

'''
"""
Type your answer to Problem 06 here. Don't be wordy. Each
of these questions should be answered with a short (no more
than 2-5 sentences) answer. I don't want you to write essays.
"""

1. A Standard Maximization Problem is one in which there is a
linear function that we seek to maximize (or minimize), subject
to constraints which are linear inequalities. These inequalities
must be of the form ax + by + cz... <= X, where X is a positive
number.

2. In an SMP, the Objective Function is the function being maximized.

3. A Corner Point is a point in the feasible set, such that any line
segment in the feasible set which contains that point, contains it as an endpoint.

4. The Feasible Set is the set of all points that satisfy every constraint.

5. The simplex algorithm stops when either an entering or departing variable
cannot be chosen; this happens when all entries in the p-row are non-negative,
or when there are no positive entries in the entering variable's column, respectively.

6. Bounded Feasible set. A Feasible Set is bounded if there exists a circle of finite
radius which contains the entire Feasible Set.

7. An Unbounded Feasible Set is one which cannot be contained by a circle of finite
radius.

### ================ Problem 07 =========================

"""
Type your answer to Problem 07 here. Cleary state your
slack variables and the initial tableau.
"""

1. Let our slack variables be named u, v, and w.
Then we can rewrite our nontrivial constraints with these variables:

6x + z + u = 122
2y + 5z + v = 502
9x - 7y + 6z + w = 902

2. The initial tableau will be as follows:
____________________________________
|   | x | y | z | u | v | w | B.S. |
------------------------------------
| x | 6 | 0 | 1 | 1 | 0 | 0 | 122  |
------------------------------------
| y | 0 | 2 | 5 | 0 | 1 | 0 | 502  |
------------------------------------
| z | 9 |-7 | 6 | 0 | 0 | 1 | 902  |
------------------------------------
| p |-13|-7 |-5 | 0 | 0 | 0 |   0  |
------------------------------------

### ================ Problem 08 =========================

"""
Type your answer to Problem 08 here. Cleary state how
you've identified the pivot, the pivot's location (row, column)
and its value.
"""

The most negative element of the p-row is -22, corresponding
to x1. Thus x1 is chosen as our entering variable. Computing
the quotients of the elements of the x1 column and the B.S.
column yields 190/6 = 31.6, 510/7 = 72.9, and 810/10 = 81.
The smallest of those, 190/6, corresponds to the x3 row.
Thus x3 is the departing variable. Therefore the pivot is in
the x1 column and x3 row, which is 6.

'''

if __name__ == '__main__':
    print('------------ Problem 1 ------------')
    A = np.array([
        [4, 7, -10],
        [0, 25, 61],
        [0, 0, -32]])
    b = np.array([
        [-6, 15, 31],
        [11, 14, -50],
        [-54, 39, 114]])
    print(solve_lin_sys_with_bsubst(A, len(A), b, len(b)))

    A = np.array([
        [1, 3, -1, 11],
        [0, 2, 6, 12],
        [0, 0, -15, 13],
        [0, 0, 0, 35]])
    b = np.array([
        [-5, 22, 23.5, 798.45, 1, 0, 11],
        [112, 49, 12.25, 69.43, 1, 0, 12],
        [-63, 20, 356.78, -34.97, 1, 0, 13],
        [51, 13, -12, 10, 1, 0, 14]])
    print(solve_lin_sys_with_bsubst(A, len(A), b, len(b)))

    print('------------ Problem 2 ------------')
    A = np.array([
        [11, 0, 0],
        [202, 21, 0],
        [-125, 34, 35]])
    b = np.array([
        [-6, 11, 1],
        [8, 123, 1],
        [12, 217, 1]])
    print(solve_lin_sys_with_fsubst(A, len(A), b, len(b)))

    A = np.array([
        [123, 0, 0, 0],
        [256, 217, 0, 0],
        [-17, 303, 168, 0],
        [890, 456, 2789, 13]])
    b = np.array([
        [-41, 101, 202, 1000],
        [22, 123, 491, 786],
        [4, 21, 7123, 473],
        [567, 3, 87, 257]])
    print(solve_lin_sys_with_fsubst(A, len(A), b, len(b)))

    print('------------ Problem 3 ------------')
    A = np.array([
        [21, 31, -301],
        [4, 7, -8],
        [40, 51, -25]], dtype=float)
    b = np.array([
        [-52],
        [710],
        [11]], dtype=float)
    print(solve_lin_sys_with_gje(A, b))

    A = np.array([
        [7, -5, 10, 100],
        [12, 3, 6, 36],
        [-14, 13, 44, 20],
        [126, 37, 80, 11]], dtype=float)
    b = np.array([
        [42],
        [54],
        [66],
        [130]], dtype=float)
    print(solve_lin_sys_with_gje(A, b))

    print('------------ Problem 4 ------------')
    A = np.array([
        [173, 2136, 3173, 4112],
        [561, 6165, 7146, 814],
        [6137, 743, 8183, 973],
        [5196, 940, 7144, 931]], dtype=float)
    b = np.array([
        [54, 11],
        [-12, 25],
        [35, 37],
        [52, 48]], dtype=float)
    print(solve_lin_sys_with_lud(A, len(A), b, 2))

    A = np.array([
        [737, 1365, 8173, 9112, 89],
        [761, 7165, 7146, 9014, 765],
        [3137, 243, 4183, 573, 876],
        [1965, 340, 5144, 831, 1234],
        [87, 65, 21, 234, 897]], dtype=float)
    b = np.array([
        [14, 11, 20],
        [-17, 24, 151],
        [389, 34, 142],
        [523, 14, 153],
        [389, 141, 2531]], dtype=float)
    print(solve_lin_sys_with_lud(A, len(A), b, 3))

    print('------------ Problem 5 ------------')
    A = np.array([
        [0, 13, -37],
        [24, 36, -13],
        [42, 52, -23]], dtype=float)
    b = np.array([
        [-17],
        [74],
        [103]], dtype=float)
    print(solve_lin_sys_with_cramer(A, b))

    A = np.array([
        [737, 1365, 8173, 9112, 89],
        [761, 7165, 7146, 9014, 765],
        [3137, 243, 4183, 573, 876],
        [1965, 340, 5144, 831, 1234],
        [87, 65, 21, 234, 897]], dtype=float)
    b = np.array([
        [14],
        [-17],
        [389],
        [523],
        [389]], dtype=float)
    print(solve_lin_sys_with_cramer(A, b))