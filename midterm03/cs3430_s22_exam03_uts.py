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

# these are the imports of the modules we used
# in hw12. HuffmanTreeNode.py, CharFreqMap.py, and
# BinHuffmanTree.py are included in midterm03.zip.
# Recall that in hw12, you implemented encodeText(),
# decode(), encodeSymbol(), and fromListOfHuffmanTreeNodes()
# in HuffmanTree.py
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

    # =============== Problem 2 ================================

    # def test_prob02_exam03_ut01(self, num_tests=10):
    #     print('\n********Exam03: Problem 2: UT 01...')
    #     m_ary = [3, 5, 7]
    #     a_ary = [2, 3, 2]
    #     eq_class = solve_cong_system_with_crt(m_ary, a_ary)
    #     for nt in range(num_tests):
    #         print('\ntest {} ...'.format(nt))
    #         x = next(eq_class)
    #         print('x = {}'.format(x))
    #         assert self.__is_in_equiv_class(x, 23, 105)
    #         for a_i, m_i in zip(a_ary, m_ary):
    #             assert (x - a_i) % m_i == 0
    #             print('{} <> {} (mod {})'.format(x, a_i, m_i))
    #     print('\n********Exam03: Problem 2: UT 01 passed...')

    # def test_prob02_exam03_ut02(self, num_tests=10):
    #     print('\n********Exam03: Problem 2: UT 02...')
    #     m_ary = [3, 4, 5]
    #     a_ary = [1, 1, 2]
    #     eq_class = solve_cong_system_with_crt(m_ary, a_ary)
    #     for nt in range(num_tests):
    #         print('\ntest {} ...'.format(nt))
    #         x = next(eq_class)
    #         print('x = {}'.format(x))
    #         assert self.__is_in_equiv_class(x, 37, 60)
    #         for a_i, m_i in zip(a_ary, m_ary):
    #             assert (x - a_i) % m_i == 0
    #             print('{} <> {} (mod {})'.format(x, a_i, m_i))
    #     print('\n********Exam03: Problem 2: UT 02 passed...')

    # def test_prob02_exam03_ut03(self, num_tests=10):
    #     print('\n********Exam03: Problem 2: UT 03...')
    #     m_ary = [3, 4, 5]
    #     a_ary = [2, 1, 2]
    #     eq_class = solve_cong_system_with_crt(m_ary, a_ary)
    #     for nt in range(num_tests):
    #         print('\ntest {} ...'.format(nt))
    #         x = next(eq_class)
    #         print('x = {}'.format(x))
    #         assert self.__is_in_equiv_class(x, 17, 60)
    #         for a_i, m_i in zip(a_ary, m_ary):
    #             assert (x - a_i) % m_i == 0
    #             print('{} <> {} (mod {})'.format(x, a_i, m_i))
    #     print('\n********Exam03: Problem 2: UT 03 passed...')

    # def test_prob02_exam03_ut04(self, num_tests=100):
    #     print('\n********Exam03: Problem 2: UT 04...')
    #     m_ary = [3*3, 41*41*41, 17*17*17*17, 5*5, 7*7*7]
    #     lwr, uppr = 1, 100000000000
    #     for nt in range(num_tests):
    #         a_ary = []
    #         for _ in range(len(m_ary)):
    #             a = random.randint(lwr, uppr)
    #             sign = random.randint(0, 1)
    #             if sign == 0:
    #                 a *= -1
    #             a_ary.append(a)
    #         eq_class = solve_cong_system_with_crt(m_ary, a_ary)
    #         print('\ntest {} ...'.format(nt))
    #         x = next(eq_class)
    #         for a_i, m_i in zip(a_ary, m_ary):
    #             assert (x - a_i) % m_i == 0
    #             print('{} <> {} (mod {})'.format(x, a_i, m_i))
    #     print('\n********Exam03: Problem 2: UT 04 passed...')

    # def test_prob02_exam03_ut05(self, num_tests=100):
    #     print('\n********Exam03: Problem 2: UT 05...')
    #     m_ary = [13*13, 41*41*41, 17*17*17*17, 5*5, 11*11]
    #     lwr, uppr = 1, 100000000000000000000000000000000
    #     for nt in range(num_tests):
    #         a_ary = []
    #         for _ in range(len(m_ary)):
    #             a = random.randint(lwr, uppr)
    #             sign = random.randint(0, 1)
    #             if sign == 0:
    #                 a *= -1
    #             a_ary.append(a)
    #         eq_class = solve_cong_system_with_crt(m_ary, a_ary)
    #         print('\ntest {} ...'.format(nt))
    #         x = next(eq_class)
    #         for a_i, m_i in zip(a_ary, m_ary):
    #             assert (x - a_i) % m_i == 0
    #             print('{} <> {} (mod {})'.format(x, a_i, m_i))
    #     print('\n********Exam03: Problem 2: UT 05 passed...')

    # # =============== Problem 3 ================================

    # def test_prob03_exam03_ut01(self, num_tests=100):
    #     print('\n********Exam03: Problem 3: UT 01...')
    #     a, b, m = 222, 50, 253
    #     eq_class = solve_cong_with_xeuc(a, b, m)
    #     for nt in range(num_tests):
    #         print('\ntest {} ...'.format(nt))
    #         x = next(eq_class)
    #         assert (a*x - b) % m == 0
    #         print('{}*{} <> {} (mod {})'.format(a, x, b, m))
    #     print('\n********Exam03: Problem 3: UT 01 passed...')

    # def test_prob03_exam03_ut02(self, num_tests=100):
    #     print('\n********Exam03: Problem 3: UT 02...')
    #     a, b, m = 8706, 7788, 3125
    #     eq_class = solve_cong_with_xeuc(a, b, m)
    #     for nt in range(num_tests):
    #         print('\ntest {} ...'.format(nt))
    #         x = next(eq_class)
    #         assert (a*x - b) % m == 0
    #         print('{}*{} <> {} (mod {})'.format(a, x, b, m))
    #     print('\n********Exam03: Problem 3: UT 02 passed...')

    # def test_prob03_exam03_ut03(self, num_tests=100):
    #     print('\n********Exam03: Problem 3: UT 03...')
    #     a, b, m = 9412, 3774, 5890
    #     eq_class = solve_cong_with_xeuc(a, b, m)
    #     for nt in range(num_tests):
    #         print('\ntest {} ...'.format(nt))
    #         x = next(eq_class)
    #         assert (a*x - b) % m == 0
    #         print('{}*{} <> {} (mod {})'.format(a, x, b, m))
    #     print('\n********Exam03: Problem 3: UT 03 passed...')

    # def test_prob03_exam03_ut04(self, num_tests=100):
    #     print('\n********Exam03: Problem 3: UT 04...')
    #     a, b, m = 1198, 3043, 9581
    #     eq_class = solve_cong_with_xeuc(a, b, m)
    #     for nt in range(num_tests):
    #         print('\ntest {} ...'.format(nt))
    #         x = next(eq_class)
    #         assert (a*x - b) % m == 0
    #         print('{}*{} <> {} (mod {})'.format(a, x, b, m))
    #     print('\n********Exam03: Problem 3: UT 04 passed...')

    # def test_prob03_exam03_ut05(self, num_tests=100):
    #     print('\n********Exam03: Problem 3: UT 05...')
    #     a, b, m = 4767,	8373, 534
    #     eq_class = solve_cong_with_xeuc(a, b, m)
    #     for nt in range(num_tests):
    #         print('\ntest {} ...'.format(nt))
    #         x = next(eq_class)
    #         assert (a*x - b) % m == 0
    #         print('{}*{} <> {} (mod {})'.format(a, x, b, m))
    #     print('\n********Exam03: Problem 3: UT 05 passed...')

    # # # =============== Problem 4 ================================
    # # # A few students told me that they had to remove ()
    # # # in expressions like lcgg = rand_lcg(a, b, m, n, x0=seed)(),
    # # # because otherwise the python generators didn't work in
    # # # their python version. If that's the case in your version
    # # # of python remove ().

    # def test_prob04_exam03_ut01(self):
    #     print('\n******** Exam 03: Problem 04: UT 01...')
    #     a, b, m, n, seed = 214013, 2531011, 4294967296, 10, 1
    #     lcgg = rand_lcg(a, b, m, n, x0=seed)()
    #     rns = [next(lcgg) for _ in range(n)]
    #     print('LCG random numbers: {}'.format(rns))
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')
    #     print('\n******** Exam 03: Problem 04: UT 01 passed...')

    # def test_prob04_exam03_ut02(self):
    #     print('\n******** Exam 03: Problem 04: UT 02...')
    #     a, b, m, n, seed = 214013, 2531013, 4294967296, 10, 213
    #     lcgg = rand_lcg(a, b, m, n, x0=seed)()
    #     rns = [next(lcgg) for _ in range(n)]
    #     print('LCG random numbers: {}'.format(rns))
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')
    #     print('\n******** Exam 03: Problem 04: UT 02 passed...')

    # def test_prob04_exam03_ut03(self):
    #     print('\n******** Exam 03: Problem 04: UT 03...')
    #     a, b, m, n, seed = 214013, 2531017, 4294967296, 20, 11235
    #     lcgg = rand_lcg(a, b, m, n, x0=seed)()
    #     rns = [next(lcgg) for _ in range(n)]
    #     print('LCG random numbers: {}'.format(rns))
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')
    #     print('\n******** Exam 03: Problem 04: UT 03 passed...')

    # def test_prob04_exam03_ut04(self):
    #     print('\n******** Exam 03: Problem 04: UT 04...')
    #     a, b, m, n, seed = 214017, 2531019, 4294967296, 20, 11235
    #     lcgg = rand_lcg(a, b, m, n, x0=seed)()
    #     rns = [next(lcgg) for _ in range(n)]
    #     print('LCG random numbers: {}'.format(rns))
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')
    #     print('\n******** Exam 03: Problem 04: UT 04 passed...')

    # def test_prob04_exam03_ut05(self):
    #     print('\n******** Exam 03: Problem 04: UT 05...')
    #     a, b, m, n, seed = 214019, 2531017, 4294967296, 10000000, 11237
    #     lcgg = rand_lcg(a, b, m, n, x0=seed)()
    #     rns = [next(lcgg) for _ in range(n)]
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')
    #     print('\n******** Exam 03: Problem 04: UT 05 passed...')

    # def test_prob04_exam03_ut06(self):
    #     print('\n******** Exam 03: Problem 04: UT 06...')
    #     a, b, m, n, seed = 438293617, (2**13 + 13), 2**30, 20000000, 58132134
    #     lcgg = rand_lcg(a, b, m, n, x0=seed)()
    #     rns = [next(lcgg) for _ in range(n)]
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')
    #     print('\n******** Exam 03: Problem 04: UT 06 passed...')

    # def test_prob04_exam03_ut07(self):
    #     print('\n******** Exam 03: Problem 04: UT 07...')
    #     a, b, m, n, seed = 12132445, (2**17 + 17), 2**36, 30000000, 11235813
    #     lcgg = rand_lcg(a, b, m, n, x0=seed)()
    #     rns = [next(lcgg) for _ in range(n)]
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')
    #     print('\n******** Exam 03: Problem 04: UT 07 passed...')

    # def test_prob04_exam03_ut08(self):
    #     print('\n******** Exam 03: Problem 04: UT 08...')
    #     a, b, m, n, seed = 181465474592829, (2 **
    #                                          19 + 19), 2**48, 40000000, 3581311224
    #     lcgg = rand_lcg(a, b, m, n, x0=seed)()
    #     rns = [next(lcgg) for _ in range(n)]
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')
    #     print('\n******** Exam 03: Problem 04: UT 08 passed...')

    # def test_prob04_exam03_ut09(self):
    #     print('\n******** Exam 03: Problem 04: UT 09...')
    #     a, b, m, n, seed = 454339144066433781, (2 **
    #                                             23 + 23), 2**60, 50000000, 3582241311
    #     lcgg = rand_lcg(a, b, m, n, x0=seed)()
    #     rns = [next(lcgg) for _ in range(n)]
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')
    #     print('\n******** Exam 03: Problem 04: UT 09 passed...')

    # def test_prob04_exam03_ut10(self):
    #     print('\n******** Exam 03: Problem 04: UT 10...')
    #     a, b, m, n, seed = 454339144066433783, (2 **
    #                                             23 + 23), 2**60, 50000000, 3582241313
    #     lcgg = rand_lcg(a, b, m, n, x0=seed)()
    #     rns = [next(lcgg) for _ in range(n)]
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')
    #     print('\n******** Exam 03: Problem 04: UT 10 passed...')

    # # # =============== Problem 5 ================================
    # # # A few students told me that they had to remove ()
    # # # in expressions like xsg = rand_xorshift(a, b, c, n, x0=seed)()
    # # # because otherwise the python generators didn't work in
    # # # their python version. If that's the case in your version
    # # # of python remove ().

    # def test_prob05_exam03_ut01(self):
    #     print('\n******** Exam 03: Problem 05: UT 01...')
    #     a, b, c, n, seed = 1, 3, 10, 5, 1
    #     xsg = rand_xorshift(a, b, c, n, x0=seed)()
    #     rns = [next(xsg) for _ in range(n)]
    #     print('XORSHIFT random numbers: {}'.format(rns))
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')
    #     print('\n******** Exam 03: Problem 05: UT 01 passed...')

    # def test_prob05_exam03_ut02(self):
    #     print('\n******** Exam 03: Problem 05: UT 02...')
    #     a, b, c, n, seed = 1, 3, 10, 10, 3
    #     xsg = rand_xorshift(a, b, c, n, x0=seed)()
    #     rns = [next(xsg) for _ in range(n)]
    #     print('XORSHIFT random numbers: {}'.format(rns))
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')
    #     print('\n******** Exam 03: Problem 05: UT 02 passed...')

    # def test_prob05_exam03_ut03(self):
    #     print('\n******** Exam 03: Problem 05: UT 03...')
    #     a, b, c, n, seed = 1, 3, 10, 20, 5
    #     xsg = rand_xorshift(a, b, c, n, x0=seed)()
    #     rns = [next(xsg) for _ in range(n)]
    #     print('XORSHIFT random numbers: {}'.format(rns))
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')
    #     print('\n******** Exam 03: Problem 05: UT 03 passed...')

    # def test_prob05_exam03_ut04(self):
    #     print('\n******** Exam 03: Problem 05: UT 04...')
    #     a, b, c, n, seed = 1, 3, 10, 1000000, 7
    #     xsg = rand_xorshift(a, b, c, n, x0=seed)()
    #     rns = [next(xsg) for _ in range(n)]
    #     ### print('XORSHIFT random numbers: {}'.format(rns))
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')
    #     print('\n******** Exam 03: Problem 05: UT 04 passed...')

    # def test_prob05_exam03_ut05(self):
    #     print('\n******** Exam 03: Problem 05: UT 05...')
    #     a, b, c, n, seed = 2, 5, 15, 1000000, 13
    #     xsg = rand_xorshift(a, b, c, n, x0=seed)()
    #     rns = [next(xsg) for _ in range(n)]
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')
    #     print('\n******** Exam 03: Problem 05: UT 05 passed...')

    # def test_prob05_exam03_ut06(self):
    #     print('\n******** Exam 03: Problem 05: UT 06...')
    #     a, b, c, n, seed = 3, 23, 25, 2000000, 17
    #     xsg = rand_xorshift(a, b, c, n, x0=seed)()
    #     rns = [next(xsg) for _ in range(n)]
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')
    #     print('\n******** Exam 03: Problem 05: UT 06 passed...')

    # def test_prob05_exam03_ut07(self):
    #     print('\n******** Exam 03: Problem 05: UT 07...')
    #     a, b, c, n, seed = 5, 9, 28, 20000000, 19
    #     xsg = rand_xorshift(a, b, c, n, x0=seed)()
    #     rns = [next(xsg) for _ in range(n)]
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')
    #     print('\n******** Exam 03: Problem 05: UT 07 passed...')

    # def test_prob05_exam03_ut08(self):
    #     print('\n******** Exam 03: Problem 05: UT 08...')
    #     a, b, c, n, seed = 7, 13, 25, 30000000, 23
    #     xsg = rand_xorshift(a, b, c, n, x0=seed)()
    #     rns = [next(xsg) for _ in range(n)]
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique...')
    #     print('\n******** Exam 03: Problem 05: UT 08 passed...')

    # def test_prob05_exam03_ut09(self):
    #     print('\n******** Exam 03: Problem 05: UT 09...')
    #     a, b, c, n, seed = 13, 3, 27, 50000000, 113
    #     xsg = rand_xorshift(a, b, c, n, x0=seed)()
    #     rns = [next(xsg) for _ in range(n)]
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique...')
    #     print('\n******** Exam 03: Problem 05: UT 09 passed...')

    # def test_prob05_exam03_ut10(self):
    #     print('\n******** Exam 03: Problem 05: UT 10...')
    #     a, b, c, n, seed = 13, 3, 27, 50000000, 117
    #     xsg = rand_xorshift(a, b, c, n, x0=seed)()
    #     rns = [next(xsg) for _ in range(n)]
    #     assert len(rns) == n
    #     assert self.__check_uniqueness(rns)
    #     print('\n******** Exam 03: Problem 05: UT 10 passed...')

    # # =============== Problem 6 ================================

    # def test_prob06_exam03_ut01(self):
    #     print('\n******** Exam 03: Problem 06: UT 01...')
    #     seq = [1, 5, 7, 8, 5, 1, 3, 4, 3, 3, 2, 2, 0, 7, 9, 8, 7, 4, 3, 1, 3]
    #     n, lower_bound, upper_bound = 21, 0, 9
    #     v_stat, p_val = equidistrib_test(seq, n, lower_bound, upper_bound)
    #     assert 8.0 <= v_stat <= 8.2
    #     assert 0.5 <= p_val <= 0.55
    #     print('seq   = {}'.format(seq))
    #     print('V     = {}'.format(v_stat))
    #     print('p val = {}'.format(p_val))
    #     print('\n******** Exam 03: Problem 06: UT 01 passed...')

    # def test_prob06_exam03_ut02(self):
    #     print('\n******** Exam 03: Problem 06: UT 02...')
    #     a, b, m, n, seed = 214013, 2531011, 113, 5, 1
    #     lcgg = rand_lcg(a, b, m, n, x0=seed)()
    #     rns = [next(lcgg) for _ in range(n)]
    #     v_stat, p_val = equidistrib_test(rns, n, 0, m-1)
    #     assert 107.0 <= v_stat <= 109.0
    #     assert 0.49 <= p_val <= 0.6
    #     print('seq   = {}'.format(rns))
    #     print('V     = {}'.format(v_stat))
    #     print('p val = {}'.format(p_val))
    #     print('\n******** Exam 03: Problem 06: UT 02 passed...')

    # def test_prob06_exam03_ut03(self):
    #     print('\n******** Exam 03: Problem 06: UT 03...')
    #     a, b, m, n, seed = 214013, 2531011, 4294967296, 10, 0
    #     lcgg = rand_lcg(a, b, m, n, x0=seed)()
    #     start, stop = 0, 100
    #     rns = cs3430_s22_exam03_uts.__scale(
    #         [next(lcgg) for _ in range(n)], start, stop)
    #     # V     = 90.99999999999997
    #     # p val = 0.7287482821588177
    #     v_stat, p_val = equidistrib_test(rns, n, start, stop)
    #     assert 89.0 <= v_stat <= 91.0
    #     assert 0.71 <= p_val <= 0.74
    #     print('seq   = {}'.format(rns))
    #     print('V     = {}'.format(v_stat))
    #     print('p val = {}'.format(p_val))
    #     print('\n******** Exam 03: Problem 06: UT 03 passed...')

    # def test_prob06_exam03_ut04(self):
    #     print('\n******** Exam 03: Problem 06: UT 04...')
    #     a, b, m, n, seed = 214013, 2531011, 4294967296, 20, 13
    #     lcgg = rand_lcg(a, b, m, n, x0=seed)()
    #     start, stop = 0, 200
    #     rns = cs3430_s22_exam03_uts.__scale(
    #         [next(lcgg) for _ in range(n)], start, stop)
    #     v_stat, p_val = equidistrib_test(rns, n, start, stop)
    #     assert 180.0 <= v_stat <= 182.0
    #     assert 0.81 <= p_val <= 0.84
    #     print('seq   = {}'.format(rns))
    #     print('V     = {}'.format(v_stat))
    #     print('p val = {}'.format(p_val))
    #     print('\n******** Exam 03: Problem 06: UT 04 passed...')

    # def test_prob06_exam03_ut05(self):
    #     print('\n******** Exam 03: Problem 06: UT 05...')
    #     a, b, m, n, seed = 214013, 2531011, 4294967296, 100, 13
    #     lcgg = rand_lcg(a, b, m, n, x0=seed)()
    #     start, stop = 0, 300
    #     rns = cs3430_s22_exam03_uts.__scale(
    #         [next(lcgg) for _ in range(n)], start, stop)
    #     v_stat, p_val = equidistrib_test(rns, n, start, stop)
    #     assert 326.0 <= v_stat <= 328.0
    #     assert 0.11 <= p_val <= 0.15
    #     print('seq   = {}'.format(rns))
    #     print('V     = {}'.format(v_stat))
    #     print('p val = {}'.format(p_val))
    #     print('\n******** Exam 03: Problem 06: UT 05 passed...')

    # def test_prob06_exam03_ut06(self):
    #     print('\n******** Exam 03: Problem 06: UT 06...')
    #     a, b, c, n, seed = 1, 3, 10, 5, 1
    #     xsg = rand_xorshift(a, b, c, n, x0=seed)()
    #     start, stop = 0, 10
    #     rns = cs3430_s22_exam03_uts.__scale(
    #         [next(xsg) for _ in range(n)], start, stop)
    #     v_stat, p_val = equidistrib_test(rns, n, start, stop)
    #     assert 18.0 <= v_stat <= 21.0
    #     assert 0.02 <= p_val <= 0.05
    #     print('seq   = {}'.format(rns))
    #     print('V     = {}'.format(v_stat))
    #     print('p val = {}'.format(p_val))
    #     print('\n******** Exam 03: Problem 06: UT 06 passed...')

    # def test_prob06_exam03_ut07(self):
    #     print('\n******** Exam 03: Problem 06: UT 07...')
    #     a, b, m, n, seed = 214013, 2531011, 4294967296, 200, 13
    #     lcgg = rand_lcg(a, b, m, n, x0=seed)()
    #     start, stop = 0, 300
    #     rns = cs3430_s22_exam03_uts.__scale(
    #         [next(lcgg) for _ in range(n)], start, stop)
    #     v_stat, p_val = equidistrib_test(rns, n, start, stop)
    #     assert 283.0 <= v_stat <= 286.0
    #     assert 0.71 <= p_val <= 0.74
    #     print('seq   = {}'.format(rns))
    #     print('V     = {}'.format(v_stat))
    #     print('p val = {}'.format(p_val))
    #     print('\n******** Exam 03: Problem 06: UT 07 passed...')

    # def test_prob06_exam03_ut08(self):
    #     print('\n******** Exam 03: Problem 06: UT 08...')
    #     a, b, c, n, seed = 1, 3, 10, 100, 1
    #     xsg = rand_xorshift(a, b, c, n, x0=seed)()
    #     start, stop = 0, 100
    #     rns = cs3430_s22_exam03_uts.__scale(
    #         [next(xsg) for _ in range(n)], start, stop)
    #     v_stat, p_val = equidistrib_test(rns, n, start, stop)
    #     assert 101.0 <= v_stat <= 104.0
    #     assert 0.41 <= p_val <= 0.43
    #     print('seq   = {}'.format(rns))
    #     print('V     = {}'.format(v_stat))
    #     print('p val = {}'.format(p_val))
    #     print('\n******** Exam 03: Problem 06: UT 08 passed...')

    # def test_prob06_exam03_ut09(self):
    #     print('\n******** Exam 03: Problem 06: UT 09...')
    #     a, b, c, n, seed = 2, 5, 15, 300, 1
    #     xsg = rand_xorshift(a, b, c, n, x0=seed)()
    #     start, stop = 10, 500
    #     rns = cs3430_s22_exam03_uts.__scale(
    #         [next(xsg) for _ in range(n)], start, stop)
    #     v_stat, p_val = equidistrib_test(rns, n, start, stop)
    #     assert 507.0 <= v_stat <= 509.0
    #     assert 0.26 <= p_val <= 0.28
    #     print('seq   = {}'.format(rns))
    #     print('V     = {}'.format(v_stat))
    #     print('p val = {}'.format(p_val))
    #     print('\n******** Exam 03: Problem 06: UT 09 passed...')

    # def test_prob06_exam03_ut10(self):
    #     print('\n******** Exam 03: Problem 06: UT 10...')
    #     a, b, c, n, seed = 2, 5, 17, 300, 7
    #     xsg = rand_xorshift(a, b, c, n, x0=seed)()
    #     start, stop = 10, 500
    #     rns = cs3430_s22_exam03_uts.__scale(
    #         [next(xsg) for _ in range(n)], start, stop)
    #     v_stat, p_val = equidistrib_test(rns, n, start, stop)
    #     assert 572.0 <= v_stat <= 575.0
    #     assert 0.003 <= p_val <= 0.007
    #     print('seq   = {}'.format(rns))
    #     print('V     = {}'.format(v_stat))
    #     print('p val = {}'.format(p_val))
    #     print('\n******** Exam 03: Problem 06: UT 10 passed...')

    # # ================== Problem 09 =====================

    def test_prob09_exam03_ut01(self):
        print('\n******** Exam 03: Problem 09: UT 01...')
        dt_root = learn_bin_id3_dt_from_csv_file('train_data.csv', 'Class')
        assert not dt_root is None
        display_bin_id3_node(dt_root)
        print('\n******** Exam03: Problem 09: UT 01 passed...')

    def test_prob09_exam03_ut02(self):
        print('\n********Exam03: Problem 09: UT 02...')
        dt_root = learn_bin_id3_dt_from_csv_file('train_data.csv', 'Class')
        acc = classify_csv_file_with_bin_id3_dt(
            dt_root, 'test_data.csv', 'Class')
        print('classification accuracy = {}'.format(acc))
        assert acc >= 0.95
        print('\n********Exam03: Problem 09: UT 02 passed...')

    # # ================== Problem 10 =====================

    # def test_prob10_exam03_ut01(self):
    #     print('\n********Exam03: Problem 10: UT 01...')
    #     txt = 'aababbcdefghaaaaa'
    #     ht = build_huffman_tree_from_text(txt)
    #     cdefg = set(['c', 'd', 'e', 'f', 'g', 'h'])
    #     for c in txt:
    #         enc = ht.encodeSymbol(c)
    #         if c == 'a':
    #             assert len(enc) == 1
    #         elif c == 'b':
    #             assert len(enc) == 3
    #         elif c in cdefg:
    #             assert len(enc) == 4
    #         else:
    #             raise Exception('unknown character {}'.format(c))
    #         print('encoding({}) = {}'.format(c, enc))
    #         dec = ht.decode(enc)
    #         assert c == dec
    #         assert enc == ht.encodeSymbol(ht.decode(enc))
    #     print('\n********Exam03: Problem 10: UT 01 passed...')

    # def test_prob10_exam03_ut02(self):
    #     print('\n********Exam03: Problem 10: UT 02...')
    #     encode_moby_dick_ch03()
    #     filename = 'moby_dick_ch03'
    #     ext = '.txt'
    #     filepath = filename + ext
    #     cfm1 = CharFreqMap.computeCharFreqMap(filepath)
    #     nodes = HuffmanTree.freqMapToListOfHuffmanTreeNodes(cfm1)
    #     ht = HuffmanTree.fromListOfHuffmanTreeNodes(nodes)
    #     bht = BinHuffmanTree(root=ht.getRoot())
    #     with open(filepath, 'r', encoding='utf-8') as inf:
    #         data = inf.read()
    #         dec0 = bht.decodeTextFromFile(filename)
    #         assert dec0 == data
    #     print('\n********Exam03: Problem 10: UT 02 passed...')

    def runTest(self):
        pass


if __name__ == '__main__':
    unittest.main()
