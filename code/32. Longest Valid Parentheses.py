#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 32. Longest Valid Parentheses
# Created by xc 30/03/2017

"""
    找到最长最合理的括号匹配的个数
    超时了
    226 / 229 test cases passed.

"""

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        max_length = 0
        while start < len(s):
            if s[start] == ')':
                start += 1
                continue
            left = 1
            right = 0
            for index in range(start + 1, len(s)):
                if s[index] == '(':
                    left += 1
                else:
                    right += 1
                if right > left:
                    # 右括号比左括号多了,不合法
                    break
                if right == left:
                    # 当前状态下是合法的
                    if right * 2 > max_length:
                        max_length = right*2
            # 查找下一轮
            start += 1
        return max_length

s = "((((((((((((("
test = Solution()
print test.longestValidParentheses(s)


