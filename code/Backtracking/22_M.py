#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 22_M
# Created by xc 24/03/2017

"""
    所有的括号
"""
import copy


class Solution(object):
    def __init__(self):
        self.result = []

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        left = n
        right = n
        current_list = '('
        self.process(left-1, right, current_list)
        return self.result

    def process(self, left, right, current_list):
        if left == 0 and right == 0:
            # 已经到了最后了
            self.result.append(copy.deepcopy(current_list))
            return
        if left != 0:
            tmp_list = copy.deepcopy(current_list)
            tmp_list += '('
            self.process(left-1, right, tmp_list)
        if right !=0 and left < right:
            # left > right的话说明是错误了,left == right的话,只能往里放left
            tmp_list = copy.deepcopy(current_list)
            tmp_list += ')'
            self.process(left, right-1, tmp_list)

s = Solution()
print s.generateParenthesis(0)

