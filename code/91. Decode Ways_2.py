#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 91. Decode Ways
# Created by xc 11/04/2017

"""
    思路: 每次读取两个字符,如果是<=26 那么就推进两个,否则推进一个
    在最初的想法里,超长的字符串不能顺利通过测试点,复杂度太大,相当于每一个都往后推进
    更换为动态规划的思路
    d[i] 代表前i个字符串的字符串的情况
    d[i] = d[i-1],+ d[i-2]  (前一种情况要求当前不为0,后一种要求当前位和前一位构成的数字小于26)
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
        d = [0 for i in range(0, len(s))]

        # 感觉前两位比较难考虑
        if s[0] == '0':
            return 0
        if s[1] == '0' and int(s[0] + s[1]) <= 26:
            # 第一位非0,前两位构成10数字
            d[0] = 1
            d[1] = 1
        if s[1] != '0' and int(s[0] + s[1]) <= 26:
            # 第一位非0,前两位构成非10数字
            d[0] = 1
            d[1] = 2
        if s[1] != '0' and int(s[0] + s[1]) > 26:
            d[0] = 1
            d[1] = 1


        for index in range(2, len(s)):
            if s[index] != '0':
                d[index] += d[index - 1]
            if 10 <= int(s[index-1] + s[index]) <= 26:
                d[index] += d[index - 2]
        return d[-1]



test = Solution()
# 要注意为0的情况
s = '1204'
s = '13205'
s = "4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"
# 带有0的部分都是很容易产生错误的
#s = '10'
#s = '00'
s = '27'
s = '301'
s = '1204'
s = '1309'

print test.numDecodings(s)