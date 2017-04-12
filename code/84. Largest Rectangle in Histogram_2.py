#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 84. Largest Rectangle in Histogram
# Created by xing 2017/4/1
"""
    因为矩形肯定是以某一个矩阵为最高点构建的，而这个最高点的矩形所能成的形
    就是左右两端最后一次大于等于这个数的位置
    优化算法
"""
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        if len(heights) == 0:
            return 0
        # stack中存放的是索引
        stack = [0]
        # 保证最后一定会退栈
        heights.append(0)
        for index in range(1, len(heights)):
            if heights[index] >= heights[stack[-1]]:
                # 入栈
                stack.append(index)
            else:
                last_top_index = stack[-1]
                while len(stack) >= 1 and heights[stack[-1]] > heights[index]:
                    # 出栈栈顶元素并计算面积
                    if len(stack) == 1:
                        w = last_top_index - (-1)
                    else:
                        w = last_top_index - stack[-2]
                    h = heights[stack[-1]]
                    area = h * w
                    if area > max_area:
                        max_area = area
                    del stack[-1]
                # 入栈新元素
                stack.append(index)
        return max_area
test = Solution()
heights = [2,1,5,6,2,3]
heights = [1,1]
print test.largestRectangleArea(heights)