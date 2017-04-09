#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 96_M
# Created by xc 23/03/2017

"""
    题目要求:对于一组数据,可以生成多少个同分异构的二叉搜索树
    f(0) = f(1) = 1
    f(2) = f(1)(0) + f(0)f(1)
    f(k) = f(k-1)f(0) + f(k-2)f(1) + ... + f(0)f(k-1)
    f(n) = f(n-1)f(0) + f(n-2)f(1) + ... + f(0)f(n-1)
    最终的结果是 C(2n,n)/(n+1)

"""


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = []
        for index in range(0, n + 1):
            d.append(0)
        d[0] = 1
        d[1] = 1
        for k in range(2, n+1):
            for index in range(k-1, -1, -1):
                d[k] += d[index] * d[k - index - 1]
        return d[n]

s = Solution()
print s.numTrees(5)