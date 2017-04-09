#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 32. Longest Valid Parentheses
# Created by xc 30/03/2017

"""
    找到最长最合理的括号匹配的个数
    之前的算法超时了
    需要修正
    227 / 229 test cases passed.
"""

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        left = 0
        right = 0
        stack = []
        result_stack = []
        for index in range(0, len(s)):
            if s[index] == '(':
                # 左括号入栈
                stack.append('(')
            else:
                # 右括号
                if len(stack) == 0:
                    # 右括号无法匹配 故这个)丢弃,不处理
                    pass
                else:
                    # 获取栈顶元素
                    # 消掉一个左括号同时在result_stack里放置当前匹配的位置
                    del stack[-1]
                    result_stack.append(index)


        # 最后输出一个结果 此时的如果rigth有数字,那么状态应该是一个断开的 左面比右面多的状态()
        if right * 2 > max_length:
            max_length = right * 2
        return max_length

s = "(()(((()"
test = Solution()
print test.longestValidParentheses(s)


