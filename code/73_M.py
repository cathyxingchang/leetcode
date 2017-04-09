#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 73_M
# Created by xc 21/03/2017

import copy
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row_dic = {}
        col_dic = {}
        for row in range(0, m):
            for col in range(0, n):
                if matrix[row][col] == 0:
                    row_dic[row] = 1
                    col_dic[col] = 1
        # 行置0
        zero_row_list = []
        for index in range(0, n):
            zero_row_list.append(0)
        for key in row_dic:
            matrix[key] = copy.deepcopy(zero_row_list)
        # 列置0
        for key in col_dic:
            for row in range(0, m):
                matrix[row][key] = 0

matrix = [[0, 2, 3], [3, 4, 5], [1, 5, 6]]
s = Solution()
print s.setZeroes(matrix)