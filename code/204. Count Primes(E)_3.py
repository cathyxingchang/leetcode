#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 204. Count Primes(E)
# Created by xc 17/04/2017
"""
    统计质数的个数
    注意审题:题目中说的是 小于n的
    直接遍历的方法是会超时的,那么改变一个思路,在判断是否是质数的时候,用比它的根号小的质数进行判断
    还是超时19 / 20 test cases passed.
    在 1500000 这个测试点崩溃
"""

import math
class Solution(object):
    def __init__(self):
        self.primes_set = []

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0

        for i in range(2, n):
            count += self.is_primes(i)
        print self.primes_set
        return count

    def is_primes(self, num):
        if num == 2:
            self.primes_set.append(num)
            return 1

        for item in self.primes_set:
            if item*item > num:
                break
            if num % item == 0:
                return 0
        self.primes_set.append(num)
        return 1

test = Solution()
print test.countPrimes(999983)