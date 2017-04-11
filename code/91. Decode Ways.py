#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 91. Decode Ways
# Created by xc 11/04/2017

"""
    思路: 每次读取两个字符,如果是<=26 那么就推进两个,否则推进一个
    该思路下,超长的测试点过不了,复杂度太大了
    222 / 259 test cases passed.
"""
class Solution(object):
    def __init__(self):
        self.count = 0

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            if s[0] != '0':
                return 1
            else:
                return 0
        num0 = int(s[0])
        num1 = int(s[0] + s[1])
        if num0 > 0:
            self.process(s[1:])
        if 10 <= num1 <= 26:
            self.process(s[2:])
        return self.count

    def process(self, s):
        """
        从s串向后推进
        :param s: 
        :return: 
        """
        if len(s) == 0:
            self.count += 1
            return
        if len(s) == 1:
            if s[0] != '0':
                self.count += 1
            return
        num0 = int(s[0])
        num1 = int(s[0] + s[1])
        if num0 > 0:
            self.process(s[1:])
        if 10 <= num1 <= 26:
            self.process(s[2:])


test = Solution()
# 要注意为0的情况
s = '1204'
s = '13205'
s = "4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"
print test.numDecodings(s)