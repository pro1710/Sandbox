#!/usr/bin/env python3

class OrderStatistics():

    @staticmethod
    def min(lst: list):
        if not lst or len(lst) == 0:
            raise ValueError('empty list')

        m = lst[0]
        for el in lst[1:]:
            if el < m:
                m = el
        return m

    @staticmethod
    def max(lst: list):
        if not lst or len(lst) == 0:
            raise ValueError('empty list')

        m = lst[0]
        for el in lst[1:]:
            if el > m:
                m = el
        return m

    @staticmethod
    def min_max(lst: list):
        if not lst or len(lst) == 0:
            raise ValueError('empty list')

        if len(lst) % 2:
            min_ = max_ = lst[0]
            n = 1
        else:
            min_, max_ = lst[:2]
            n = 2

        for i in range(n, len(lst), 2):
            if lst[i+1] > lst[i]:
                lmin, lmax = lst[i], lst[i+1]
            else:
                lmin, lmax = lst[i+1], lst[i]

            if min_ > lmin:
                min_ = lmin

            if max_ < lmax:
                max_ = lmax

        return min_, max_




import unittest
import random

class TestOrderStatisticsMin(unittest.TestCase):
    @staticmethod
    def genTests(n, size, r):
        test_lists = [[random.randrange(r) for _1 in range(size)] for _2 in range(n)]
        for i, lst in enumerate(test_lists):
            test_name = 'test_min_{}'.format(i)
            test_method = lambda self: self.assertEqual(min(lst), OrderStatistics.min(lst))
            setattr(TestOrderStatisticsMin, test_name, test_method)

class TestOrderStatisticsMax(unittest.TestCase):
    @staticmethod
    def genTests(n, size, r):
        test_lists = [[random.randrange(r) for _1 in range(size)] for _2 in range(n)]
        for i, lst in enumerate(test_lists):
            test_name = 'test_max_{}'.format(i)
            test_method = lambda self: self.assertEqual(max(lst), OrderStatistics.max(lst))
            setattr(TestOrderStatisticsMax, test_name, test_method)

class TestOrderStatisticsMinMax(unittest.TestCase):
    @staticmethod
    def genTests(n, size, r):
        test_lists = [[random.randrange(r) for _1 in range(size)] for _2 in range(n)]
        for i, lst in enumerate(test_lists):
            test_name = 'test_min_max_{}'.format(i)
            test_method = lambda self: self.assertEqual((min(lst), max(lst)), (OrderStatistics.min_max(lst)))
            setattr(TestOrderStatisticsMax, test_name, test_method)

if __name__ == '__main__':

    TEST_PARAMS = (10**2, 10**2, 10**4)

    TestOrderStatisticsMin.genTests(*TEST_PARAMS)
    TestOrderStatisticsMax.genTests(*TEST_PARAMS)
    TestOrderStatisticsMinMax.genTests(*TEST_PARAMS)

    unittest.main()
