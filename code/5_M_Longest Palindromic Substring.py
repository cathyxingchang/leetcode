#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 5_M_Longest Palindromic Substring
# Created by xc 28/03/2017

"""
    题目需要知道最短的回文串
    解法:暴力解法,遍历每一个字符串 o(n^3)的复杂度
    没想到竟然过了算法
    Runtime: 2882 ms
"""

import copy
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_length = 0
        max_palindrome = s[0]
        for begin in range(0, len(s)):
            for end in range(len(s) - 1, begin, -1):
                if self.isPalindrome(begin, end, s):
                    length = end - begin + 1
                    if length > max_length:
                        max_length = length
                        max_palindrome = copy.deepcopy(s[begin:end + 1])

        return max_palindrome

    def isPalindrome(self,begin,end,s):
        i = begin
        j = end
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

s = "aaa"
test = Solution()
print test.longestPalindrome(s)