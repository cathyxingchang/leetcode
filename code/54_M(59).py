#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 54_M(59)
# Created by xc 22/03/2017

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        num = 1
        n = len(matrix)
        result = []
        # 旋转的圈数
        if n % 2 == 0:
            circle = n / 2
        else:
            circle = n / 2 + 1
        for circle_index in range(0, circle):
            for roll1 in range(circle_index, n - circle_index):
                result.append(matrix[circle_index][roll1])
            for roll2 in range(circle_index + 1, n - circle_index):
                result.append(matrix[roll2][n - circle_index - 1])
            for roll3 in range(n - circle_index - 2, circle_index - 1, -1):
                result.append(matrix[n - circle_index - 1][roll3])
            for roll4 in range(n - circle_index - 2, circle_index, -1):
                result.append(matrix[roll4][circle_index])
        return result

matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
s = Solution()
print s.spiralOrder(matrix)