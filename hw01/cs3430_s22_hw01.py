######################################################
# module: cs3430_s22_hw01.py
# YOUR NAME
# YOUR A-NUMBER
######################################################

from math import prod

import numpy as np
import numpy.linalg
import random


## If you need to define auxiliary functions, you may define them
## in this file.

### ============= Problem 1 (Gauss-Jordan Elimination) ===============

def is_zero(row):
    return all(map(lambda x: x == 0, row))


def swap_rows(A, i, j):
    A[[i, j]] = A[[j, i]]


def gje(a, b):
    """ Gauss-Jordan Elimination to solve Ax = b. """
    # Diagonalize
    r = 0
    for c in range(len(a)):
        # Skip zero columns
        if is_zero(a[:, c]):
            continue

        # Swap if pivot is zero
        if a[r, c] == 0:
            nonzero = next((i for i in range(r + 1, len(a)) if a[i, c] != 0), None)

            # System could be inconsistent
            if nonzero is None: return None

            swap_rows(a, r, nonzero)
            swap_rows(b, r, nonzero)

        # Zero above and below to make backsub easy
        pivot = a[r, c]
        for e in range(len(a)):
            if e == r:
                continue

            scalar = a[e, c] / pivot
            
            a[e, :] -= scalar * a[r, :]
            b[e, :] -= scalar * b[r, :]
        
        # Move to next row
        r += 1
    
    # Back substitute
    x = []
    for i in range(len(a)):
        x.append(b[i, 0] / a[i, i])
    
    return np.transpose(np.array([x]))

## ============== Problem 2 (Determinants) ========================

def random_mat(nr, nc, lower, upper):
    """ Generate an nrxnc matrix of random numbers in [lower, upper]. """
    m = np.zeros((nr, nc))
    for r in range(nr):
        for c in range(nc):
            m[r][c] = random.randint(lower, upper)
    return m

# Kinda inefficient since this copies
def minor(A, i, j):
    return np.delete(np.delete(A, i, 0), j, 1)

def leibnitz_det(a):
    a = np.copy(a)
    
    """ Compute determinant of nxn matrix a with Leibnitz's Formula. """
    if len(a) == 2:
        return a[0, 0] * a[1, 1] - a[0, 1] * a[1, 0]
    
    factors = [(-1)**(i) * a[0, i] * leibnitz_det(minor(a, 0, i)) for i in range(len(a))]
    return sum(factors)
    

def gauss_det(a):
    a = np.copy(a)

    """ Compute determinant of nxn matrix a with Gaussian elimination. """
    swaps = 0

    # Diagonalize
    r = 0
    for c in range(len(a)):
        # Skip zero columns
        if is_zero(a[:, c]):
            continue

        # Swap if pivot is zero
        if a[r, c] == 0:
            nonzero = next((i for i in range(r + 1, len(a)) if a[i, c] != 0), None)

            # System could be inconsistent
            if nonzero is None: return 0

            swap_rows(a, r, nonzero)
            swaps += 1

        # Zero below
        pivot = a[r, c]
        for e in range(r + 1, len(a)):
            if e == r:
                continue

            scalar = a[e, c] / pivot
            
            a[e, :] -= scalar * a[r, :]
        
        # Move to next row
        r += 1
    
    return (-1)**swaps * prod(a[i, i] for i in range(len(a)))

## ============== Problem 3 (Cramer's Rule) ======================

def replace_col(A, b, j):
    A = np.copy(A)
    A[:, j] = b[:, 0]
    return A

def cramer(A, b):
    """ Solve Ax = b with Cramer's Rule. """
    det_a = np.linalg.det(A)
    b_dets = (np.linalg.det(replace_col(A, b, j)) for j in range(len(A)))
    x = [b / det_a for b in b_dets]
    return np.transpose(np.array([x]))

if __name__ == '__main__':
    pass

    
    
              
