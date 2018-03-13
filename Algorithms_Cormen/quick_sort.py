#! /usr/bin/env python3

import random

class QuickSort(object):
    class Partition(object):
        @staticmethod
        def simple(a, first, last):
            pivot = a[last]
            i = first - 1
            for j in range(first, last):
                if pivot > a[j]:
                    i += 1
                    a[i], a[j] = a[j], a[i]
            a[i + 1], a[last] = a[last], a[i + 1]
            return i + 1

        @staticmethod
        def randomized(a, first, last):
            i = random.randrange(first, last)
            a[i], a[last] = a[last], a[i]
            return QuickSort.Partition.simple(a, first, last)


    @staticmethod
    def sort(a, first=None, last=None, partition=Partition.simple):

        if first == None:
                first = 0
        if last == None:
                last = len(a) - 1

        if last > first:
            pivot_idx = partition(a, first, last)
            QuickSort.sort(a, first, pivot_idx-1, partition)
            QuickSort.sort(a, pivot_idx+1, last, partition)


# unit tests
import unittest

TEST_SIZE = 100
TEST_RANGE = 1000

class TestQuickSort(unittest.TestCase):
    def setUp(self):
        self.test = [random.randrange(TEST_RANGE) for _1 in range(TEST_SIZE)]
        self.expected = sorted(self.test)

    def tearDown(self):
        self.test = []
        self.expected = []

    def test_simple_partition(self):
        QuickSort.sort(self.test, partition=QuickSort.Partition.simple)
        self.assertEqual(self.test, self.expected)

    def test_randomized_partition(self):
        QuickSort.sort(self.test, partition=QuickSort.Partition.randomized)
        self.assertEqual(self.test, self.expected)


if __name__ == '__main__':
    unittest.main()
