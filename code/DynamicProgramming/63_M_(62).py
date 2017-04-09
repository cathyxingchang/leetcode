#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 63_M_(62)
# Created by xc 22/03/2017

"""
    这道题是62题的扩展,
    还是路径规划的问题,这一次有些地方的路不能走
    其实就是状态方程有变化了
"""

import copy
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        col_list = []
        d = []
        for index in range(0, n):
            col_list.append(0)
        for index in range(0, m):
            d.append(copy.deepcopy(col_list))
        # 把一开始能确定的填上
        # 这里特别要小心,边界存在是1的情况 如果边界有一个1是1,那么这一行就都是1了
        # 所以需要给一个最初的位置
        if obstacleGrid[0][0] == 1:
            d[0][0] = 0
        else:
            d[0][0] = 1
        for index in range(1, m):
            if obstacleGrid[index][0] == 1:
                d[index][0] = 0
            else:
                d[index][0] = d[index-1][0]
        for index in range(1, n):
            if obstacleGrid[0][index] == 1:
                d[0][index] = 0
            else:
                d[0][index] = d[0][index-1]

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    d[i][j] = 0
                else:
                    d[i][j] = d[i-1][j]+d[i][j-1]
        return d[m-1][n-1]

s = Solution()
obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
print s.uniquePathsWithObstacles(obstacleGrid)