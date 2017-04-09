# -*- coding: utf-8 -*-

# 64_M
# Created by xc 22/03/2017

"""
   64. Minimum Path Sum 是62,63,64 前面的题目的扩展
   到ij的位置的
   d[i][j] = min(d[i-1][j],d[i][j-1])+value[i][j]
"""
import copy
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        col_list = []
        for j in range(0, n):
            col_list.append(0)
        d = []
        for i in range(0, m):
            d.append(copy.deepcopy(col_list))
        d[0][0] = grid[0][0]
        # 初始化第一列和第一行
        for row in range(1, m):
            d[row][0] = d[row - 1][0] + grid[row][0]
        for col in range(1, n):
            d[0][col] = d[0][col - 1] + grid[0][col]

        for i in range(1, m):
            for j in range(1, n):
                d[i][j] = min(d[i - 1][j], d[i][j - 1]) + grid[i][j]

        return d[m-1][n-1]

gird = [[0]]
s = Solution()
print s.minPathSum(gird)
