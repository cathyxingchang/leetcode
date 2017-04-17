#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 441. Arranging Coins(E)
# Created by xc 17/04/2017
"""
    十分Easy的硬币问题
    每行一个两个三个四个一共能摆多少行
    对于k行,总共需要 (1+k)k/2这么多硬币
    (1+k)k/2 <= n
    (1+k)k <= 2n
    k^2 + k - 2n <=0
    k = (-1+sqrt(1+8n))/2
"""
import math
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = (-1 + math.sqrt(1 + 8 * n)) / 2
        return int(k)


n = 15
test = Solution()
print test.arrangeCoins(n)