#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 221. Maximal Square
# Created by xing 2017/4/1
class Solution(object):

    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        max_area = 0
        # 对矩阵进行处理
        heights = [[0 for col in range(0, len(matrix[0]))] for row in range(0, len(matrix))]
        for i in range(0, len(matrix[0])):
            heights[0][i] = int(matrix[0][i])
        for i in range(1, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == '0':
                    heights[i][j] = 0
                else:
                    heights[i][j] = heights[i-1][j] + 1

        # 针对heights的每一行，运行84题的算法
        for row in range(0, len(heights)):
            height = heights[row]
            area = self.largestRectangleArea(height)
            if area > max_area:
                max_area = area
        return max_area

    def largestRectangleArea(self, height):
        max_area = 0
        stack = [0]
        height.append(0)
        print height
        for index in range(1, len(height)):
            if height[index] >= height[stack[-1]]:
                stack.append(index)
            else:
                last_top_index = stack[-1]
                while len(stack) >= 1 and height[stack[-1]] > height[index]:
                    h = height[stack[-1]]
                    if len(stack) == 1:
                        w = last_top_index - (-1), h
                    else:
                        w = last_top_index - stack[-2]
                    if w >= h:
                        area = h * h
                    else:
                        area = 0
                    if area > max_area:
                        max_area = area
                    del stack[-1]
                stack.append(index)
        return max_area
