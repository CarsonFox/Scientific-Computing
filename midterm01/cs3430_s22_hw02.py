
#################################################
# Module: cs3430_s22_hw02.py
# Carson Fox
# A02251670
# bugs to vladimir kulyukin via canvas
#################################################

import numpy as np
import pickle
import os

### =============== Problem 1 =============================

def lu_decomp(a, n):
    """
    lu_decomp(a, n) returns u, l such that np.dot(l, u) === a.
    a is an nxn matrix that is reduced to the upper and lower triangular matrices.
    throws exception when there is no pivot in a column or rows must be swapped
    to create a pivot.
    lu_decomp(a, n) is destructive in that a is destructively modified into u.
    """
    L = np.identity(n)

    # Diagonalize
    for i in range(n):
        # Throw if pivot is zero
        if a[i, i] == 0:
            raise f'No pivot in column {i}'

        # Zero below
        pivot = a[i, i]
        for e in range(i + 1, n):
            scalar = a[e, i] / pivot
            L[e, i] = scalar
            a[e, :] -= scalar * a[i, :]

    return a, L


### =============== Problem 2 =============================

def bsubst_single(a, n, b):
    x = list(range(n))
    for i in reversed(range(n)):
        x[i] = 1/a[i, i] * (b[i] - sum(a[i, j] * x[j] for j in range(i + 1, n)))

    return x


def bsubst(a, n, b, m):
    """
    bsubst uses back substitution to solve ax = b1, b2, ..., bm.
    a is an nxn upper-triangular matrix, n is its dimension.
    b is an nxm matrix of vectors b1, b2, ..., bm.
    returns x.
    """
    xs = []
    for i in range(m):
        xs.append(bsubst_single(a, n, b[:, i]))

    return np.transpose(np.array(xs))


def fsubst_single(a, n, b):
    x = list(range(n))
    for i in range(n):
        x[i] = 1/a[i, i] * (b[i] - sum(a[i, j] * x[j] for j in range(i)))

    return x


def fsubst(a, n, b, m):
    """
    fsubst uses forward substitution to solve ax = b1, b2, ..., bm.
    a is an nxn lower-triangular matrix, n is its dimension.
    b is an nxm matrix of vectors b1, b2, ..., bm.
    returns x.
    """
    xs = []
    for i in range(m):
        xs.append(fsubst_single(a, n, b[:, i]))

    return np.transpose(np.array(xs))


def lud_solve(a, n, b, m):
    """
    a is an nxn matrix; b is m nx1 vectors.
    Use forward subst to solve Ly = b for y.
    Use back    subst to solve Ux = y for x.
    Then LUx = Ly = b.
    Returns x.
    """
    u, l = lu_decomp(a.copy(), n)

    y = fsubst(l, n, b, m)
    x = bsubst(u, n, y, m)

    return x


def lud_solve2(u, l, n, b, m):
    """
    Uses L to transform b to c.
    Then backsubst to solve Ux = c for x.
    Returns x.
    """
    c = b.copy()
    for col in range(n):
        for row in range(col + 1, n):
            c[row] -= l[row, col] * c[col]

    x = bsubst(u, n, c, m)
    return x
