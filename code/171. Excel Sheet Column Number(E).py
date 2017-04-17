#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 171. Excel Sheet Column Number(E)
# Created by xc 17/04/2017
"""
    计算excel表格的数字 相当于是一个26进制 
"""
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for item in s:
            result = result * 26 + (ord(item) - ord('A') + 1)
        return result
s = "AZ"
test = Solution()
print test.titleToNumber(s)