#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 204. Count Primes(E)
# Created by xc 17/04/2017
"""
    统计质数的个数
    注意审题:题目中说的是 小于n的
    18 / 20 test cases passed.
    超时
"""

import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(1, n):
            count += self.is_primes(i)
        return count

    def is_primes(self, num):
        if num == 2:
            return 1
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return 0
        return 1
