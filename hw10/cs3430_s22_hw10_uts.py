#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: cs3430_s22_hw10_uts.py
# description: unit tests for CS 3430: S22: Assignment 10
# bugs to vladimir kulyukin in canvas
##############################################################

import unittest
from prng import prng
import numpy as np


class cs3430_s22_hw10_uts(unittest.TestCase):

    ### ================ Problem 1: Unit Tests =====================

    def __check_uniqueness(self, rns):
        """
        True if all numbers in rns are unique.
        """
        return len(set(rns)) == len(rns)

    @staticmethod
    def __scale(data, a, b):
        """
        scale data to be in [a, b]
        """
        assert a < b
        b_a = b - a
        min_d, max_d = np.min(data), np.max(data)
        norm = max_d - min_d
        return np.array([int(b_a * ((d - min_d) / norm) + a) for d in data])

    def test_hw10_prob01_ut01(self):
        print("\n***** CS3430: S22: HW10: Problem 01: Unit Test 01 ************")
        a, b, m, n, seed = 214013, 2531011, 4294967296, 5, 0
        lcgg = prng.lcg(a, b, m, n, x0=seed)()
        rns = [next(lcgg) for _ in range(n)]
        print("LCG random numbers: {}".format(rns))
        assert len(rns) == n
        if self.__check_uniqueness(rns):
            print("all random numbers are unique")
        print("CS 3430: S22: HW10: Problem 01: Unit Test 01: pass...")

    def test_hw10_prob01_ut02(self):
        print("\n***** CS3430: S22: HW10: Problem 01: Unit Test 02 ************")
        a, b, m, n, seed = 214013, 2531011, 4294967296, 10, 1
        lcgg = prng.lcg(a, b, m, n, x0=seed)()
        rns = [next(lcgg) for _ in range(n)]
        print("LCG random numbers: {}".format(rns))
        assert len(rns) == n
        if self.__check_uniqueness(rns):
            print("all random numbers are unique")
        print("CS 3430: S22: HW10: Problem 01: Unit Test 02: pass...")

    def test_hw10_prob01_ut03(self):
        print("\n***** CS3430: S22: HW10: Problem 01: Unit Test 03 ************")
        a, b, m, n, seed = 214013, 2531011, 4294967296, 20, 11235
        lcgg = prng.lcg(a, b, m, n, x0=seed)()
        rns = [next(lcgg) for _ in range(n)]
        print("LCG random numbers: {}".format(rns))
        assert len(rns) == n
        if self.__check_uniqueness(rns):
            print("all random numbers are unique")
        print("CS 3430: S22: HW10: Problem 01: Unit Test 03: pass...")

    def test_hw10_prob01_ut04(self):
        print("\n***** CS3430: S22: HW10: Problem 01: Unit Test 04 ************")
        a, b, m, n, seed = 214013, 2531011, 4294967296, 20, 11235
        lcgg = prng.lcg(a, b, m, n, x0=seed)()
        rns = [next(lcgg) for _ in range(n)]
        print("LCG random numbers: {}".format(rns))
        assert len(rns) == n
        if self.__check_uniqueness(rns):
            print("all random numbers are unique")
        print("CS 3430: S22: HW10: Problem 01: Unit Test 04: pass...")

    def test_hw10_prob01_ut05(self):
        print("\n***** CS3430: S22: HW10: Problem 01: Unit Test 05 ************")
        a, b, m, n, seed = 214013, 2531011, 4294967296, 10000000, 11235
        lcgg = prng.lcg(a, b, m, n, x0=seed)()
        rns = [next(lcgg) for _ in range(n)]
        ### printing 10 000 000 random numbers is not a great experience so I commented the
        ### print statement out.
        ### print('LCG random numbers: {}'.format(rns))
        assert len(rns) == n
        if self.__check_uniqueness(rns):
            print("all random numbers are unique")
        print("CS 3430: S22: HW10: Problem 01: Unit Test 05: pass...")

    def test_hw10_prob01_ut06(self):
        print("\n***** CS3430: S22: HW10: Problem 01: Unit Test 06 ************")
        a, b, m, n, seed = 438293613, (2 ** 13 + 13), 2 ** 30, 20000000, 58132134
        lcgg = prng.lcg(a, b, m, n, x0=seed)()
        rns = [next(lcgg) for _ in range(n)]
        ### printing 20 000 000 random numbers is not a great experience so I commented the
        ### print statement out.
        ### print('LCG random numbers: {}'.format(rns))
        assert len(rns) == n
        if self.__check_uniqueness(rns):
            print("all random numbers are unique")
        print("CS 3430: S22: HW10: Problem 01: Unit Test 06: pass...")

    def test_hw10_prob01_ut07(self):
        print("\n***** CS3430: S22: HW10: Problem 01: Unit Test 07 ************")
        a, b, m, n, seed = 12132445, (2 ** 17 + 17), 2 ** 36, 30000000, 11235813
        lcgg = prng.lcg(a, b, m, n, x0=seed)()
        rns = [next(lcgg) for _ in range(n)]
        ### printing 30 000 000 random numbers is not a great experience so I commented the
        ### print statement out.
        ### print('LCG random numbers: {}'.format(rns))
        assert len(rns) == n
        if self.__check_uniqueness(rns):
            print("all random numbers are unique")
        print("CS 3430: S22: HW10: Problem 01: Unit Test 07: pass...")

    def test_hw10_prob01_ut08(self):
        print("\n***** CS3430: S22: HW10: Problem 01: Unit Test 08 ************")
        a, b, m, n, seed = (
            181465474592829,
            (2 ** 19 + 19),
            2 ** 48,
            40000000,
            3581311224,
        )
        lcgg = prng.lcg(a, b, m, n, x0=seed)()
        rns = [next(lcgg) for _ in range(n)]
        ### printing 40 000 000 random numbers is not a great experience so I commented the
        ### print statement out.
        ### print('LCG random numbers: {}'.format(rns))
        assert len(rns) == n
        if self.__check_uniqueness(rns):
            print("all random numbers are unique")
        print("CS 3430: S22: HW10: Problem 01: Unit Test 08: pass...")

    def test_hw10_prob01_ut09(self):
        print("\n***** CS3430: S22: HW10: Problem 01: Unit Test 09 ************")
        a, b, m, n, seed = (
            454339144066433781,
            (2 ** 23 + 23),
            2 ** 60,
            50000000,
            3582241311,
        )
        lcgg = prng.lcg(a, b, m, n, x0=seed)()
        rns = [next(lcgg) for _ in range(n)]
        ### printing 50 000 000 random numbers is not a great experience so I commented the
        ### print statement out.
        ### print('LCG random numbers: {}'.format(rns))
        assert len(rns) == n
        if self.__check_uniqueness(rns):
            print("all random numbers are unique")
        print("CS 3430: S22: HW10: Problem 01: Unit Test 09: pass...")

    def test_hw10_prob01_ut10(self):
        print("\n***** CS3430: S22: HW10: Problem 01: Unit Test 10 ************")
        a, b, c, n, seed = 1, 3, 10, 5, 1
        xsg = prng.xorshift(a, b, c, n, x0=seed)()
        rns = [next(xsg) for _ in range(n)]
        print("XORSHIFT random numbers: {}".format(rns))
        assert len(rns) == n
        if self.__check_uniqueness(rns):
            print("all random numbers are unique")
        print("CS 3430: S22: HW10: Problem 01: Unit Test 10: pass...")

    def test_hw10_prob01_ut11(self):
        print("\n***** CS3430: S22: HW10: Problem 01: Unit Test 11 ************")
        a, b, c, n, seed = 1, 3, 10, 10, 3
        xsg = prng.xorshift(a, b, c, n, x0=seed)()
        rns = [next(xsg) for _ in range(n)]
        print("XORSHIFT random numbers: {}".format(rns))
        assert len(rns) == n
        if self.__check_uniqueness(rns):
            print("all random numbers are unique")
        print("CS 3430: S22: HW10: Problem 01: Unit Test 11: pass...")

    def test_hw10_prob01_ut12(self):
        print("\n***** CS3430: S22: HW10: Problem 01: Unit Test 12 ************")
        a, b, c, n, seed = 1, 3, 10, 20, 5
        xsg = prng.xorshift(a, b, c, n, x0=seed)()
        rns = [next(xsg) for _ in range(n)]
        print("XORSHIFT random numbers: {}".format(rns))
        assert len(rns) == n
        if self.__check_uniqueness(rns):
            print("all random numbers are unique")
        print("CS 3430: S22: HW10: Problem 01: Unit Test 12: pass...")

    def test_hw10_prob01_ut13(self):
        print("\n***** CS3430: S22: HW10: Problem 01: Unit Test 13 ************")
        a, b, c, n, seed = 1, 3, 10, 1000000, 7
        xsg = prng.xorshift(a, b, c, n, x0=seed)()
        rns = [next(xsg) for _ in range(n)]
        ### print('XORSHIFT random numbers: {}'.format(rns))
        assert len(rns) == n
        if self.__check_uniqueness(rns):
            print("all random numbers are unique")
        print("CS 3430: S22: HW10: Problem 01: Unit Test 13: pass...")

    def test_hw10_prob01_ut14(self):
        print("\n***** CS3430: S22: HW10: Problem 01: Unit Test 14 ************")
        a, b, c, n, seed = 2, 5, 15, 1000000, 13
        xsg = prng.xorshift(a, b, c, n, x0=seed)()
        rns = [next(xsg) for _ in range(n)]
        ### print('XORSHIFT random numbers: {}'.format(rns))
        assert len(rns) == n
        if self.__check_uniqueness(rns):
            print("all random numbers are unique")
        print("CS 3430: S22: HW10: Problem 01: Unit Test 14: pass...")

    def test_hw10_prob01_ut15(self):
        print("\n***** CS3430: S22: HW10: Problem 01: Unit Test 15 ************")
        a, b, c, n, seed = 3, 23, 25, 2000000, 17
        xsg = prng.xorshift(a, b, c, n, x0=seed)()
        rns = [next(xsg) for _ in range(n)]
        ### print('XORSHIFT random numbers: {}'.format(rns))
        assert len(rns) == n
        if self.__check_uniqueness(rns):
            print("all random numbers are unique")
        print("CS 3430: S22: HW10: Problem 01: Unit Test 15: pass...")

    def test_hw10_prob01_ut16(self):
        print("\n***** CS3430: S22: HW10: Problem 01: Unit Test 16 ************")
        a, b, c, n, seed = 5, 9, 28, 20000000, 19
        xsg = prng.xorshift(a, b, c, n, x0=seed)()
        rns = [next(xsg) for _ in range(n)]
        ### print('XORSHIFT random numbers: {}'.format(rns))
        assert len(rns) == n
        if self.__check_uniqueness(rns):
            print("all random numbers are unique")
        print("CS 3430: S22: HW10: Problem 01: Unit Test 16: pass...")

    def test_hw10_prob01_ut17(self):
        print("\n***** CS3430: S22: HW10: Problem 01: Unit Test 17 ************")
        a, b, c, n, seed = 7, 13, 25, 30000000, 23
        xsg = prng.xorshift(a, b, c, n, x0=seed)()
        rns = [next(xsg) for _ in range(n)]
        ### print('XORSHIFT random numbers: {}'.format(rns))
        assert len(rns) == n
        if self.__check_uniqueness(rns):
            print("all random numbers are unique...")
        print("CS 3430: S22: HW10: Problem 01: Unit Test 17: pass...")

    def test_hw10_prob01_ut18(self):
        print("\n***** CS3430: S22: HW10: Problem 01: Unit Test 18 ************")
        a, b, c, n, seed = 13, 3, 27, 50000000, 113
        xsg = prng.xorshift(a, b, c, n, x0=seed)()
        rns = [next(xsg) for _ in range(n)]
        ### print('XORSHIFT random numbers: {}'.format(rns))
        assert len(rns) == n
        if self.__check_uniqueness(rns):
            print("all random numbers are unique...")
        print("CS 3430: S22: HW10: Problem 01: Unit Test 18: pass...")

    def test_hw10_prob01_ut19(self):
        print("\n***** CS3430: S22: HW10: Problem 01: Unit Test 19 ************")
        a, b, c, n, seed = 13, 3, 27, 50000000, 117
        xsg = prng.xorshift(a, b, c, n, x0=seed)()
        rns = [next(xsg) for _ in range(n)]
        ### print('XORSHIFT random numbers: {}'.format(rns))
        assert len(rns) == n
        assert self.__check_uniqueness(rns)
        print("CS 3430: S22: HW10: Problem 01: Unit Test 19: pass...")

    def test_hw10_prob01_ut20(self):
        print("\n***** CS3430: S22: HW10: Problem 01: Unit Test 20 ************")
        seed, start, stop, n = 1, 0, 1000, 5
        mtw = prng.mersenne_twister(n, x0=seed, start=start, stop=stop)()
        rns = [next(mtw) for _ in range(n)]
        print("Mersenne Twister random numbers: {}".format(rns))
        assert len(rns) == n
        if self.__check_uniqueness(rns):
            print("all random numbers are unique...")
        print("CS 3430: S22: HW10: Problem 01: Unit Test 20: pass...")

    def test_hw10_prob01_ut21(self):
        print("\n***** CS3430: S22: HW10: Problem 01: Unit Test 21 ************")
        seed, start, stop, n = 1, 0, 1000, 10
        mtw = prng.mersenne_twister(n, x0=seed, start=start, stop=stop)()
        rns = [next(mtw) for _ in range(n)]
        print("Mersenne Twister random numbers: {}".format(rns))
        assert len(rns) == n
        if self.__check_uniqueness(rns):
            print("all random numbers are unique...")
        print("CS 3430: S22: HW10: Problem 01: Unit Test 21: pass...")

    # ================ Problem 2: Unit Tests: Random Image Art =====================

    # this UT should generate the left image on slide 10 in Lecture 20.
    def test_hw10_prob02_ut01(self):
        print("\n***** CS3430: S22: HW10: Problem 02: Unit Test 01 ************")
        w, h = 600, 600
        n = h * w
        a, b, m, seed = 214013, 2531011, 4294967291, 0
        data = prng.gen_lcg_data(a, b, m, n, seed=seed, option=1)
        prng.gen_pil_image(data, w, h, n)
        print("CS 3430: S22: HW07: Problem 02: Unit Test 01: pass")

    ### this UT should generate the middle image on slide 10 in Lecture 20.
    def test_hw10_prob02_ut02(self):
        print("\n***** CS3430: S22: HW10: Problem 02: Unit Test 02 ************")
        w, h = 600, 600
        n = h * w
        a, b, m, seed = 214013, 2531011, 4294967291, 0
        data = prng.gen_lcg_data(a, b, m, n, seed=seed, option=2)
        prng.gen_pil_image(data, w, h, n)
        print("CS 3430: S22: HW07: Problem 02: Unit Test 02: pass")

    ### this UT should generate the right image on slide 10 in Lecture 20.
    def test_hw10_prob02_ut03(self):
        print("\n***** CS3430: S22: HW10: Problem 02: Unit Test 03 ************")
        w, h = 600, 600
        n = h * w
        a, b, m, seed = 214013, 2531011, 4294967291, 0
        data = prng.gen_lcg_data(a, b, m, n, seed=seed, option=3)
        prng.gen_pil_image(data, w, h, n)
        print("CS 3430: S22: HW07: Problem 02: Unit Test 03: pass")

    ### this UT should generate the image with LCG a, b, m, seed = 12132445, (2**17 + 17), 2**36, 11235813
    def test_hw10_prob02_ut04(self):
        print("\n***** CS3430: S22: HW10: Problem 02: Unit Test 04 ************")
        w, h = 600, 600
        n = h * w
        a, b, m, seed = 12132445, (2 ** 17 + 17), 2 ** 36, 11235813
        data = prng.gen_lcg_data(a, b, m, n, seed=seed, option=1)
        prng.gen_pil_image(data, w, h, n)
        print("CS 3430: S22: HW07: Problem 02: Unit Test 04: pass")

    ### this UT generates the image with LCG a, b, m, seed in [0,600^2-1], (2**17 + 17), 2**36, 11235813
    def test_hw10_prob02_ut05(self):
        print("\n***** CS3430: S22: HW10: Problem 02: Unit Test 05 ************")
        w, h = 600, 600
        n = h * w
        a, b, m, seed = 12132445, (2 ** 17 + 17), 2 ** 36, 11235813
        data = prng.gen_lcg_data(a, b, m, n, seed=seed, option=2)
        prng.gen_pil_image(data, w, h, n)
        print("CS 3430: S22: HW07: Problem 02: Unit Test 05: pass")

    ### this UT generates the image with XORSHIFT seed=1 and a=1,b=3,c=10.
    def test_hw10_prob02_ut06(self):
        print("\n***** CS3430: S22: HW10: Problem 02: Unit Test 06 ************")
        w, h = 600, 600
        n = h * w
        a, b, c, seed = 1, 3, 10, 1
        data = prng.gen_xorshift_data(a, b, c, n, seed=seed, option=1)
        prng.gen_pil_image(data, w, h, n)
        print("CS 3430: S22: HW10: Problem 02: Unit Test 06: pass...")

    ### this UT generates the image with XORSHIFT seed in [1, 600^2] and a=1,b=3,c=10.
    ### this image should look less "random" than the one above.
    def test_hw10_prob02_ut06(self):
        print("\n***** CS3430: S22: HW10: Problem 02: Unit Test 06 ************")
        w, h = 600, 600
        n = h * w
        a, b, c = (
            1,
            3,
            10,
        )
        data = prng.gen_xorshift_data(a, b, c, n, option=2)
        prng.gen_pil_image(data, w, h, n)
        print("CS 3430: S22: HW10: Problem 02: Unit Test 06: pass...")

    ### this UT generates 1024x1024 image with XORSHIFT seed=13 and a=2,b=5,c=15.
    def test_hw10_prob02_ut07(self):
        print("\n***** CS3430: S22: HW10: Problem 02: Unit Test 07 ************")
        w, h = 1024, 1024
        n = h * w
        a, b, c, seed = 2, 5, 15, 13
        data = prng.gen_xorshift_data(a, b, c, n, seed=seed, option=1)
        prng.gen_pil_image(data, w, h, n)
        print("CS 3430: S22: HW10: Problem 02: Unit Test 07: pass...")

    ## this UT generates 1024x1024 image with XORSHIFT seed in [1, 1024^2], a=2,b=5,c=15.
    def test_hw10_prob02_ut08(self):
        print("\n***** CS3430: S22: HW10: Problem 02: Unit Test 08 ************")
        w, h = 1024, 1024
        n = h * w
        a, b, c, seed = 2, 5, 15, 13
        data = prng.gen_xorshift_data(
            a,
            b,
            c,
            n,
            seed=seed,
            option=2,
        )
        prng.gen_pil_image(data, w, h, n)
        print("CS 3430: S22: HW10: Problem 02: Unit Test 08: pass...")

    ### this UT generates 1024x1024 image with XORSHIFT seed=19, a=2,b=5,c=15.
    def test_hw10_prob02_ut09(self):
        print("\n***** CS3430: S22: HW10: Problem 02: Unit Test 09 ************")
        w, h = 1024, 1024
        n = h * w
        a, b, c, seed = 5, 9, 28, 19
        data = prng.gen_xorshift_data(a, b, c, n, seed=seed, option=1)
        prng.gen_pil_image(data, w, h, n)
        print("CS 3430: S22: HW10: Problem 02: Unit Test 09: pass...")

    ### this UT generates 1024x1024 image with mersenne twister seed=1, start=0, stop=1000
    def test_hw10_prob02_ut10(self):
        print("\n***** CS3430: S22: HW10: Problem 02: Unit Test 10 ************")
        w, h = 1024, 1024
        n = h * w
        seed, start, stop = 1, 0, 1000
        data = prng.gen_mersenne_twister_data(n, seed=seed, option=1)
        prng.gen_pil_image(data, w, h, n)
        print("CS 3430: S22: HW10: Problem 02: Unit Test 10: pass...")

    ### this UT generates 1024x1024 image with mersenne twister seed=[0, 1024^2-1], start=0, stop=1000
    ### this image should look very similar to the one generated by the previous method.
    def test_hw10_prob02_ut11(self):
        print("\n***** CS3430: S22: HW10: Problem 02: Unit Test 11 ************")
        w, h = 1024, 1024
        n = h * w
        start, stop = 0, 1000
        data = prng.gen_mersenne_twister_data(n, option=2)
        prng.gen_pil_image(data, w, h, n)
        print("CS 3430: S22: HW10: Problem 02: Unit Test 11: pass...")

    ### ================ Problem 3: Unit Tests =====================

    def test_hw10_prob03_ut01(self):
        print("\n***** CS3430: S22: HW10: Problem 03: Unit Test 01 ************")
        seq = [1, 5, 7, 8, 5, 1, 3, 4, 3, 3, 2, 2, 0, 7, 9, 8, 7, 4, 3, 1]
        n, lower_bound, upper_bound = 20, 0, 9
        v_stat, p_val = prng.equidistrib_test(seq, n, lower_bound, upper_bound)
        print("seq   = {}".format(seq))
        print("V     = {}".format(v_stat))
        print("p val = {}".format(p_val))
        print("CS 3430: S22: HW10: Problem 03: Unit Test 01: pass")

    def test_hw10_prob03_ut02(self):
        print("\n***** CS3430: S22: HW10: Problem 03: Unit Test 02 ************")
        a, b, m, n, seed = 214013, 2531011, 113, 5, 1
        lcgg = prng.lcg(a, b, m, n, x0=seed)()
        rns = [next(lcgg) for _ in range(n)]
        v_stat, p_val = prng.equidistrib_test(rns, n, 0, m - 1)
        print("seq   = {}".format(rns))
        print("V     = {}".format(v_stat))
        print("p val = {}".format(p_val))
        print("CS 3430: S22: HW10: Problem 03: Unit Test 02: pass")

    def test_hw10_prob03_ut03(self):
        print("\n***** CS3430: S22: HW10: Problem 03: Unit Test 03 ************")
        seed, start, stop, n = 0, 0, 100, 5
        mtw = prng.mersenne_twister(n, x0=seed, start=start, stop=stop)()
        rns = [next(mtw) for _ in range(n)]
        v_stat, p_val = prng.equidistrib_test(rns, n, start, stop)
        print("seq   = {}".format(rns))
        print("V     = {}".format(v_stat))
        print("p val = {}".format(p_val))
        print("CS 3430: S22: HW10: Problem 03: Unit Test 03: pass")

    def test_hw10_prob03_ut04(self):
        print("\n***** CS3430: S22: HW10: Problem 03: Unit Test 04 ************")
        seed, start, stop, n = 3, 0, 100, 5
        mtw = prng.mersenne_twister(n, x0=seed, start=start, stop=stop)()
        rns = [next(mtw) for _ in range(n)]
        v_stat, p_val = prng.equidistrib_test(rns, n, start, stop)
        print("seq   = {}".format(rns))
        print("V     = {}".format(v_stat))
        print("p val = {}".format(p_val))
        print("CS 3430: S22: HW10: Problem 03: Unit Test 04: pass")

    def test_hw10_prob03_ut05(self):
        print("\n***** CS3430: S22: HW10: Problem 03: Unit Test 05 ************")
        seed, start, stop, n = 3, 0, 100, 5
        mtw = prng.mersenne_twister(n, x0=seed, start=start, stop=stop)()
        rns = cs3430_s22_hw10_uts.__scale([next(mtw) for _ in range(n)], 0, 10)
        v_stat, p_val = prng.equidistrib_test(rns, n, start, stop)
        print("seq   = {}".format(rns))
        print("V     = {}".format(v_stat))
        print("p val = {}".format(p_val))
        print("CS 3430: S22: HW10: Problem 03: Unit Test 05: pass")

    def test_hw10_prob03_ut06(self):
        print("\n***** CS3430: S22: HW10: Problem 03: Unit Test 06 ************")
        a, b, m, n, seed = 214013, 2531011, 4294967296, 10, 0
        lcgg = prng.lcg(a, b, m, n, x0=seed)()
        start, stop = 0, 100
        rns = cs3430_s22_hw10_uts.__scale([next(lcgg) for _ in range(n)], start, stop)
        v_stat, p_val = prng.equidistrib_test(rns, n, start, stop)
        print("seq   = {}".format(rns))
        print("V     = {}".format(v_stat))
        print("p val = {}".format(p_val))
        print("CS 3430: S22: HW10: Problem 03: Unit Test 06: pass")

    def test_hw10_prob03_ut07(self):
        print("\n***** CS3430: S22: HW10: Problem 03: Unit Test 07 ************")
        a, b, m, n, seed = 214013, 2531011, 4294967296, 20, 13
        lcgg = prng.lcg(a, b, m, n, x0=seed)()
        start, stop = 0, 200
        rns = cs3430_s22_hw10_uts.__scale([next(lcgg) for _ in range(n)], start, stop)
        v_stat, p_val = prng.equidistrib_test(rns, n, start, stop)
        print("seq   = {}".format(rns))
        print("V     = {}".format(v_stat))
        print("p val = {}".format(p_val))
        print("CS 3430: S22: HW10: Problem 03: Unit Test 07: pass")

    def test_hw10_prob03_ut08(self):
        print("\n***** CS3430: S22: HW10: Problem 03: Unit Test 08 ************")
        a, b, m, n, seed = 214013, 2531011, 4294967296, 100, 13
        lcgg = prng.lcg(a, b, m, n, x0=seed)()
        start, stop = 0, 300
        rns = cs3430_s22_hw10_uts.__scale([next(lcgg) for _ in range(n)], start, stop)
        v_stat, p_val = prng.equidistrib_test(rns, n, start, stop)
        print("seq   = {}".format(rns))
        print("V     = {}".format(v_stat))
        print("p val = {}".format(p_val))
        print("CS 3430: S22: HW10: Problem 03: Unit Test 08: pass")

    def test_hw10_prob03_ut09(self):
        print("\n***** CS3430: S22: HW10: Problem 03: Unit Test 09 ************")
        a, b, m, n, seed = 214013, 2531011, 4294967296, 200, 13
        lcgg = prng.lcg(a, b, m, n, x0=seed)()
        start, stop = 0, 300
        rns = cs3430_s22_hw10_uts.__scale([next(lcgg) for _ in range(n)], start, stop)
        v_stat, p_val = prng.equidistrib_test(rns, n, start, stop)
        print("seq   = {}".format(rns))
        print("V     = {}".format(v_stat))
        print("p val = {}".format(p_val))
        print("CS 3430: S22: HW10: Problem 03: Unit Test 09: pass")

    def test_hw10_prob03_ut10(self):
        print("\n***** CS3430: S22: HW10: Problem 03: Unit Test 10 ************")
        a, b, c, n, seed = 1, 3, 10, 5, 1
        xsg = prng.xorshift(a, b, c, n, x0=seed)()
        start, stop = 0, 10
        rns = cs3430_s22_hw10_uts.__scale([next(xsg) for _ in range(n)], start, stop)
        v_stat, p_val = prng.equidistrib_test(rns, n, start, stop)
        print("seq   = {}".format(rns))
        print("V     = {}".format(v_stat))
        print("p val = {}".format(p_val))
        print("CS 3430: S22: HW10: Problem 03: Unit Test 10: pass...")

    def test_hw10_prob03_ut11(self):
        print("\n***** CS3430: S22: HW10: Problem 03: Unit Test 11 ************")
        a, b, c, n, seed = 1, 3, 10, 100, 1
        xsg = prng.xorshift(a, b, c, n, x0=seed)()
        start, stop = 0, 100
        rns = cs3430_s22_hw10_uts.__scale([next(xsg) for _ in range(n)], start, stop)
        v_stat, p_val = prng.equidistrib_test(rns, n, start, stop)
        print("seq   = {}".format(rns))
        print("V     = {}".format(v_stat))
        print("p val = {}".format(p_val))
        print("CS 3430: S22: HW10: Problem 03: Unit Test 11: pass...")

    def test_hw10_prob03_ut12(self):
        print("\n***** CS3430: S22: HW10: Problem 03: Unit Test 12 ************")
        a, b, c, n, seed = 2, 5, 15, 300, 1
        xsg = prng.xorshift(a, b, c, n, x0=seed)()
        start, stop = 10, 500
        rns = cs3430_s22_hw10_uts.__scale([next(xsg) for _ in range(n)], start, stop)
        v_stat, p_val = prng.equidistrib_test(rns, n, start, stop)
        print("seq   = {}".format(rns))
        print("V     = {}".format(v_stat))
        print("p val = {}".format(p_val))
        print("CS 3430: S22: HW10: Problem 03: Unit Test 12: pass...")

    def test_hw10_prob03_ut12(self):
        print("\n***** CS3430: S22: HW10: Problem 03: Unit Test 12 ************")
        a, b, c, n, seed = 2, 5, 15, 300, 1
        xsg = prng.xorshift(a, b, c, n, x0=seed)()
        start, stop = 10, 500
        rns = cs3430_s22_hw10_uts.__scale([next(xsg) for _ in range(n)], start, stop)
        v_stat, p_val = prng.equidistrib_test(rns, n, start, stop)
        print("seq   = {}".format(rns))
        print("V     = {}".format(v_stat))
        print("p val = {}".format(p_val))
        print("CS 3430: S22: HW10: Problem 03: Unit Test 12: pass...")

    def runTest(self):
        pass


if __name__ == "__main__":
    unittest.main()
