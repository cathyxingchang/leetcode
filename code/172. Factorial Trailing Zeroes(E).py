#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 172. Factorial Trailing Zeroes(E)
# Created by xc 17/04/2017
"""
    统计阶乘里面5的个数
"""

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            count += n / 5
            n = n / 5
        return count
