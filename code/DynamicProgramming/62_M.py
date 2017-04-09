#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 62_M
# Created by xc 22/03/2017
"""
    动态规划问题:
    d[i][j] = d[i-1][j]+d[i][j-1]

"""
import copy

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        col_list = []
        d = []
        for index in range(0, n):
            col_list.append(0)
        for index in range(0, m):
            d.append(copy.deepcopy(col_list))
        # 把一开始能确定的填上
        for index in range(0, m):
            d[index][0] = 1
        for index in range(0, n):
            d[0][index] = 1

        for i in range(1, m):
            for j in range(1, n):
                d[i][j] = d[i-1][j]+d[i][j-1]
        return d[m-1][n-1]

s = Solution()
print s.uniquePaths(1,2)
