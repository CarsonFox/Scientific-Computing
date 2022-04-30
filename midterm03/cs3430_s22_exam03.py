
###################################
## module: cs3430_s22_exam03.py
# Carson Fox
# A02251670
#####################################

import math
import numpy as np
from math import prod
from statistics import mean
from CharFreqMap import CharFreqMap

# YOUR IMPORTS

from cs3430_s22_hw09 import solve_cong, mult_inv_mod_n, make_equiv_class_mod_n
from prng import prng
from bin_id3 import bin_id3, id3_node
from HuffmanTree import HuffmanTree
from BinHuffmanTree import BinHuffmanTree

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
    return solve_cong(a, b, m, tmax=1)[0]

# ========= Problem 4 ========================


def rand_lcg(a, b, m, n, x0=0):
    return prng.lcg(a, b, m, n, x0=x0)

# ========= Problem 5 ========================


def rand_xorshift(a, b, c, n, x0=1):
    return prng.xorshift(a, b, c, n, x0=x0)

# ========= Problem 6 ========================


def equidistrib_test(seq, n, lower_bound, upper_bound):
    return prng.equidistrib_test(seq, n, lower_bound, upper_bound)

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
    examples, attribs = bin_id3.parse_csv_file_into_examples(csv_fp)
    avt = bin_id3.construct_attrib_values_from_examples(examples, attribs)
    return bin_id3.fit(examples, target_attrib, set(attribs), avt, False)


def display_bin_id3_node(node):
    bin_id3.display_id3_node(node)


def classify_csv_file_with_bin_id3_dt(dt_root: id3_node, csv_fp, target_attrib):
    examples, _ = bin_id3.parse_csv_file_into_examples(csv_fp)
    predictions = (bin_id3.predict(dt_root, e) for e in examples)

    correct = sum(p == e[target_attrib] for p, e in zip(predictions, examples))
    return correct / len(examples)

# ========= Problem 10 ========================


def computeFreqMap(txt):
    freq_map = {}
    for c in txt:
        if c in freq_map:
            freq_map[c] += 1
        else:
            freq_map[c] = 1
    return freq_map


def build_huffman_tree_from_text(txtstr):
    freq_map = computeFreqMap(txtstr)
    nodes = HuffmanTree.freqMapToListOfHuffmanTreeNodes(freq_map)
    return HuffmanTree.fromListOfHuffmanTreeNodes(nodes)


'''
Remember to state the number of saved bytes.
'''


def encode_moby_dick_ch03():
    freq_map = CharFreqMap.computeCharFreqMap('moby_dick_ch03.txt')
    nodes = HuffmanTree.freqMapToListOfHuffmanTreeNodes(freq_map)
    tree = HuffmanTree.fromListOfHuffmanTreeNodes(nodes)

    bin_tree = BinHuffmanTree(root=tree.getRoot())
    bin_tree.encodeTextFromFileToFile(
        'moby_dick_ch03.txt', 'moby_dick_ch03')


# ========= Problem 11 ========================

'''
Type your solution here.

'''
