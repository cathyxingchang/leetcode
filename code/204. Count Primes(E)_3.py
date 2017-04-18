#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 204. Count Primes(E)
# Created by xc 17/04/2017
"""
    统计质数的个数
    解法二：厄拉多塞筛法
    参考别人的算法
    http://blog.csdn.net/lisonglisonglisong/article/details/45309651
"""
import time
import math
class Solution(object):
    def __init__(self):
        self.state_set = []
        self.n = 0

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        self.state_set = [True for i in range(0, n)]
        self.n = n

        count = 0
        i = 2
        while i < n:
            if i * i > n:
                break
            if self.state_set[i]:
                self.eladuosai(i)
            i += 1
        self.state_set[2] = True
        for i in range(2, n):
            if self.state_set[i]:
                count += 1
        return count

    def eladuosai(self, num):
        i = num + num
        while i < self.n:
            self.state_set[i] = False
            i += num
        pass


start = time.clock()
test = Solution()
print test.countPrimes(1500000)
end = time.clock()
total_time = (end - start)*1000
print total_time