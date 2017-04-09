#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 200_M
# Created by xc 08/03/2017

"""
    题目要求,计算岛屿数目
    思路:首先在周围补充一圈0,之后分析所有为1的位置.
    原本的思路是,如果该位置的左面和上面都不是1 那么就认为是新海岛
    00000
    00100
    01110
    00000
    但是这样的情况显然是不行的
    换个思路,以每个1元素为中心,向周围扩散,把所有是1的还连着的都放进去,同时置标志位为-1,下次检索的时候,这些是-1的就不考虑了
    递归思想,啊 递归做的还不错嘛~
"""
import copy
class Solution(object):
    def __init__(self):
        self.effect_grid = []
        self.origin_grid = []

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.origin_grid = copy.deepcopy(grid)
        island_count = 0
        # 构建一个"有效"矩阵 保存每个位置还是否有效
        self.effect_grid = copy.deepcopy(grid)
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                self.effect_grid[row][col] = True
        #
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col] == '1' and self.effect_grid[row][col] == True:
                    island_count += 1
                    # 把与这个点相连接1点的的effect都置为False
                    self.process(row, col)
        return island_count

    def process(self, row, col):
        # 处理 row,col 处,与之相连的点的 effect值
        if row < 0 or row >= len(self.origin_grid):
            # 行列超出范围
            return
        if col < 0 or col >= len(self.origin_grid[0]):
            # 列超出范围
            return
        if self.effect_grid[row][col] == False:
            # 当前结点已经是失效结点了,直接返回
            return
        # 不是失效的结点.
        if self.origin_grid[row][col] == '1':
            self.effect_grid[row][col] = False
            self.process(row - 1, col)
            self.process(row + 1, col)
            self.process(row, col + 1)
            self.process(row, col - 1)
        return
