#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: cs3430_s22_exam03_uts.py
# description: unit tests CS3430: S22: Exam 03
##############################################################

import unittest
import numpy as np
import random

from cs3430_s22_exam03 import solve_cong_system_with_crt
from cs3430_s22_exam03 import solve_cong_with_xeuc
from cs3430_s22_exam03 import rand_lcg
from cs3430_s22_exam03 import rand_xorshift
from cs3430_s22_exam03 import equidistrib_test
from cs3430_s22_exam03 import learn_bin_id3_dt_from_csv_file
from cs3430_s22_exam03 import classify_csv_file_with_bin_id3_dt
from cs3430_s22_exam03 import display_bin_id3_node
from cs3430_s22_exam03 import build_huffman_tree_from_text
from cs3430_s22_exam03 import encode_moby_dick_ch03

### these are the imports of the modules we used
### in hw12. HuffmanTreeNode.py, CharFreqMap.py, and
### BinHuffmanTree.py are included in midterm03.zip.
### Recall that in hw12, you implemented encodeText(),
### decode(), encodeSymbol(), and fromListOfHuffmanTreeNodes()
### in HuffmanTree.py
from HuffmanTree import HuffmanTree
from HuffmanTreeNode import HuffmanTreeNode
from CharFreqMap import CharFreqMap
from BinHuffmanTree import BinHuffmanTree

class cs3430_s22_exam03_uts(unittest.TestCase):

    def __is_in_equiv_class(self, x, a, m):
        """ Is x in [a]_m? """
        return (x - a) % m == 0

    def __check_uniqueness(self, rns):
        """
        True if all numbers in rns are unique.
        """
        return len(set(rns)) == len(rns)

    def __scale(data, a, b):
        """
        scale data to be in [a, b]
        """
        assert a < b
        b_a = (b-a)
        min_d, max_d = np.min(data), np.max(data)
        norm = max_d - min_d
        return np.array([int(b_a*((d - min_d)/norm) + a) for d in data])    

    ### =============== Problem 6 ================================

    def test_prob06_exam03_ut01(self):
        print('\n******** Exam 03: Problem 06: UT 01...')            
        seq = [1, 5, 7, 8, 5, 1, 3, 4, 3, 3, 2, 2, 0, 7, 9, 8, 7, 4, 3, 1, 3]
        n, lower_bound, upper_bound = 21, 0, 9
        v_stat, p_val = equidistrib_test(seq, n, lower_bound, upper_bound)
        #print('seq   = {}'.format(seq))
        #print('V     = {}'.format(v_stat))
        #print('p val = {}'.format(p_val))
        assert 7.0 <= v_stat <= 9.0
        assert 0.4 <= p_val <= 0.6
        print('\n******** Exam 03: Problem 06: UT 01 passed...')

    def test_prob06_exam03_ut02(self):
        print('\n******** Exam 03: Problem 06: UT 02...')            
        a, b, m, n, seed = 214013, 2531011, 113, 5, 1
        lcgg = rand_lcg(a, b, m, n, x0=seed)()
        rns = [next(lcgg) for _ in range(n)]        
        v_stat, p_val = equidistrib_test(rns, n, 0, m-1)
        #print('seq   = {}'.format(rns))
        #print('V     = {}'.format(v_stat))
        #print('p val = {}'.format(p_val))
        assert 105.0 <= v_stat <= 110.0
        assert 0.55  <= p_val  <= 0.60
        print('\n******** Exam 03: Problem 06: UT 02 passed...')

    def test_prob06_exam03_ut03(self):
        print('\n******** Exam 03: Problem 06: UT 03...')            
        a, b, m, n, seed = 214013, 2531011, 4294967296, 10, 0        
        lcgg = rand_lcg(a, b, m, n, x0=seed)()
        start, stop = 0, 100
        rns = cs3430_s22_exam03_uts.__scale([next(lcgg) for _ in range(n)], start, stop)
        v_stat, p_val = equidistrib_test(rns, n, start, stop)
        print('seq   = {}'.format(rns))
        print('V     = {}'.format(v_stat))
        print('p val = {}'.format(p_val))
        assert 89.0 <= v_stat <= 91.0
        assert 0.72 <= p_val  <= 0.78
        print('\n******** Exam 03: Problem 06: UT 03 passed...')
        
    def test_prob06_exam03_ut04(self):
        print('\n******** Exam 03: Problem 06: UT 04...')            
        a, b, m, n, seed = 214013, 2531011, 4294967296, 20, 13        
        lcgg = rand_lcg(a, b, m, n, x0=seed)()
        start, stop = 0, 200
        unscaled_rns = [next(lcgg) for _ in range(n)]
        print('unscaled_rns = {}'.format(unscaled_rns))
        rns = cs3430_s22_exam03_uts.__scale(unscaled_rns, start, stop)
        print('scaled_rns   = {}'.format(rns))
        v_stat, p_val = equidistrib_test(rns, n, start, stop)
        print('seq   = {}'.format(rns))
        print('V     = {}'.format(v_stat))
        print('p val = {}'.format(p_val))
        assert 199.0 <= v_stat <= 202.0
        assert 0.45 <= p_val   <= 0.50
        print('\n******** Exam 03: Problem 06: UT 04 passed...')

    def test_prob06_exam03_ut05(self):
        print('\n******** Exam 03: Problem 06: UT 05...')            
        a, b, m, n, seed = 214013, 2531011, 4294967296, 100, 13        
        lcgg = rand_lcg(a, b, m, n, x0=seed)()
        start, stop = 0, 300
        rns = cs3430_s22_exam03_uts.__scale([next(lcgg) for _ in range(n)], start, stop)        
        v_stat, p_val = equidistrib_test(rns, n, start, stop)
        print('seq   = {}'.format(rns))
        print('V     = {}'.format(v_stat))
        print('p val = {}'.format(p_val))
        assert 306.0 <= v_stat <= 310.0
        assert 0.32  <= p_val  <= 0.38
        print('\n******** Exam 03: Problem 06: UT 05 passed...')

    def test_prob06_exam03_ut06(self):
        print('\n******** Exam 03: Problem 06: UT 06...')             
        a, b, c, n, seed = 1, 3, 10, 5, 1
        xsg = rand_xorshift(a, b, c, n, x0=seed)()
        start, stop = 0, 10
        rns = cs3430_s22_exam03_uts.__scale([next(xsg) for _ in range(n)], start, stop)        
        v_stat, p_val = equidistrib_test(rns, n, start, stop)
        print('seq   = {}'.format(rns))
        print('V     = {}'.format(v_stat))
        print('p val = {}'.format(p_val))
        assert 15.0 <= v_stat <= 20.00
        assert 0.02 <= p_val <= 0.07
        print('\n******** Exam 03: Problem 06: UT 06 passed...')

    def test_prob06_exam03_ut07(self):
        print('\n******** Exam 03: Problem 06: UT 07...')             
        a, b, m, n, seed = 214013, 2531011, 4294967296, 200, 13        
        lcgg = rand_lcg(a, b, m, n, x0=seed)()
        start, stop = 0, 300
        rns = cs3430_s22_exam03_uts.__scale([next(lcgg) for _ in range(n)], start, stop)        
        v_stat, p_val = equidistrib_test(rns, n, start, stop)
        print('seq   = {}'.format(rns))
        print('V     = {}'.format(v_stat))
        print('p val = {}'.format(p_val))
        assert 283.0 <= v_stat <= 289.0
        assert 0.68 <= p_val <= 0.72
        print('\n******** Exam 03: Problem 06: UT 07 passed...')

    def test_prob06_exam03_ut08(self):
        print('\n******** Exam 03: Problem 06: UT 08...')             
        a, b, c, n, seed = 1, 3, 10, 100, 1
        xsg = rand_xorshift(a, b, c, n, x0=seed)()
        start, stop = 0, 100
        rns = cs3430_s22_exam03_uts.__scale([next(xsg) for _ in range(n)], start, stop)        
        v_stat, p_val = equidistrib_test(rns, n, start, stop)
        print('seq   = {}'.format(rns))
        print('V     = {}'.format(v_stat))
        print('p val = {}'.format(p_val))
        assert 99.0 <= v_stat <= 103.0
        assert 0.42  <= p_val <= 0.47
        print('\n******** Exam 03: Problem 06: UT 08 passed...')

    def test_prob06_exam03_ut09(self):
        print('\n******** Exam 03: Problem 06: UT 09...')             
        a, b, c, n, seed = 2, 5, 15, 300, 1
        xsg = rand_xorshift(a, b, c, n, x0=seed)()
        start, stop = 10, 500
        rns = cs3430_s22_exam03_uts.__scale([next(xsg) for _ in range(n)], start, stop)        
        v_stat, p_val = equidistrib_test(rns, n, start, stop)
        print('seq   = {}'.format(rns))
        print('V     = {}'.format(v_stat))
        print('p val = {}'.format(p_val))
        assert 505.0 <= v_stat <= 510.0
        assert 0.10  <= p_val <= 0.40
        print('\n******** Exam 03: Problem 06: UT 09 passed...')

    def test_prob06_exam03_ut10(self):
        print('\n******** Exam 03: Problem 06: UT 10...')             
        a, b, c, n, seed = 2, 5, 17, 300, 7
        xsg = rand_xorshift(a, b, c, n, x0=seed)()
        start, stop = 10, 500
        rns = cs3430_s22_exam03_uts.__scale([next(xsg) for _ in range(n)], start, stop)        
        v_stat, p_val = equidistrib_test(rns, n, start, stop)        
        #print('seq   = {}'.format(rns))
        #print('V     = {}'.format(v_stat))
        #print('p val = {}'.format(p_val))
        assert 525.0 <= v_stat <= 535.0
        assert 0.05  <= p_val <= 0.12
        print('\n******** Exam 03: Problem 06: UT 10 passed...')

    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
