#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 48. Rotate Image(M)
# Created by xc 18/04/2017
"""
    参考了别人的思路
    # 首先沿着主对角线进行对称操作
    # 按照中轴列,对列进行交替
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 首先沿着主对角线进行对称操作
        n = len(matrix)
        for i in range(0, n):
            for j in range(0, i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        print matrix
        # 按照中轴列,对列进行交替
        for i in range(0, n):
            for j in range(0, n / 2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][n-1-j]
                matrix[i][n-1-j] = tmp
        print matrix


matrix = [[1,2,3],[4,5,6],[7,8,9]]
test = Solution()
print test.rotate(matrix)