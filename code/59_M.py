#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 59_M
# Created by xc 18/03/2017
"""
    题目要求:
    生成n^2数组
"""

import copy
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # 初始化数组
        col_list = []
        matrix = []
        for index in range(0, n):
            col_list.append(0)
        for index in range(0, n):
            matrix.append(copy.deepcopy(col_list))

        num = 1
        # 旋转的圈数
        if n % 2 == 0:
            circle = n/2
        else:
            circle = n / 2 + 1
        for circle_index in range(0, circle):
            for roll1 in range(circle_index, n - circle_index):
                matrix[circle_index][roll1] = num
                num += 1
            for roll2 in range(circle_index + 1, n - circle_index):
                matrix[roll2][n - circle_index - 1] = num
                num += 1
            for roll3 in range(n - circle_index - 2, circle_index - 1, -1):
                matrix[n - circle_index - 1][roll3] = num
                num += 1
            for roll4 in range(n - circle_index - 2, circle_index, -1):
                matrix[roll4][circle_index] = num
                num += 1
        return matrix

s = Solution()
print s.generateMatrix(3)


