
###################################
## module: cs3430_s22_exam03.py
# Carson Fox
# A02251670
#####################################

import math
import numpy as np
from math import prod

# YOUR IMPORTS

from cs3430_s22_hw09 import xeuc, mult_inv_mod_n, make_equiv_class_mod_n

# ========= Problem 1 ========================

'''
Type your solutions to Problem 1 as a multi-line
comment. Your solutions should be in the form of
equivalence class such as [1]_60, which means
the equivalence class of 1 modulo 60.

'''

# ========== Problem 2 ========================


def solve_cong_system_with_crt(mvals, avals):
    m = prod(mvals)
    bvals = (next(mult_inv_mod_n(m//mj, mj)) for mj in mvals)
    x0 = sum(m//mj * aj * bj for mj, aj, bj in zip(mvals, avals, bvals))
    return make_equiv_class_mod_n(x0, m)

# ========== Problem 3 ========================


def solve_cong_with_xeuc(a, b, m):
    # your code here
    pass

# ========= Problem 4 ========================


def rand_lcg(a, b, m, n, x0=0):
    # your code here
    pass

# ========= Problem 5 ========================


def rand_xorshift(a, b, c, n, x0=1):
    # your code here
    pass

# ========= Problem 6 ========================


def equidistrib_test(seq, n, lower_bound, upper_bound):
    # your code here
    pass

# ========= Problem 7 ========================


'''
Type your answer to this problem here.


'''

# ========= Problem 8 ========================

'''
Type your answers to this problem here.

a)

b)

c)

d)

'''

# ========= Problem 9 ========================


def learn_bin_id3_dt_from_csv_file(csv_fp, target_attrib):
    # your code here
    pass


def classify_csv_file_with_bin_id3_dt(dt_root, csv_fp, target_attrib):
    # your code here
    pass

# ========= Problem 10 ========================


def build_huffman_tree_from_text(txtstr):
    # your code here
    pass


'''
Remember to state the number of saved bytes.
'''


def encode_moby_dick_ch03():
    # your code here
    pass


# ========= Problem 11 ========================

'''
Type your solution here.

'''
