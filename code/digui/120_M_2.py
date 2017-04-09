#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 120_M_2
# Created by xc 13/03/2017

"""
    递归时间复杂度失败的话,不如试试动态规划呢
    # d[i][j] i,j位置的元素的当前的最大值,是前面的最大值加上自己这个位置
"""
import copy
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # 首先构建一个和triangle 一样的数组
        d = copy.deepcopy(triangle)
        d[0][0] = copy.deepcopy(triangle[0][0])
        for row in range(1, len(triangle)):
            for col in range(0, len(triangle[row])):
                if col == 0:
                    # 是第一列
                    d[row][col] = d[row - 1][col] + triangle[row][col]
                elif col == len(triangle[row])-1:
                    # 是最后一列
                    d[row][col] = d[row - 1][col - 1] + triangle[row][col]
                else:
                    d[row][col] = min(d[row - 1][col], d[row - 1][col - 1]) + triangle[row][col]
        # 最后找到最大的
        return min(d[len(triangle)-1])


