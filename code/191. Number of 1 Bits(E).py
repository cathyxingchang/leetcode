#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 191. Number of 1 Bits(E)
# Created by xc 16/04/2017

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            count += 1
            n &= (n-1)
        return count

test = Solution()
print test.hammingWeight(4)
