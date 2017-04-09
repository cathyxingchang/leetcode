#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 42_H
# Created by xc 18/03/2017
"""
    接水问题:
    左老师讲过的,如何能接更多的水
"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0
        # 首先构建两个数组,分别保存每个位置的元素,左面最大的元素,和右面最大的元素
        left_max = []
        right_max = []
        for index in range(0, len(height)):
            left_max.append(0)
            right_max.append(0)

        current_left_max = height[0]
        for index in range(1, len(height)):
            if height[index] > current_left_max:
                current_left_max = height[index]
            left_max[index] = current_left_max

        current_right_max = height[len(height) - 1]
        for index in range(len(height)-1, -1, -1):
            if height[index] > current_right_max:
                current_right_max = height[index]
            right_max[index] = current_right_max

        # 存储的水量等于左面和右面里面两个最大值里较小的和自己的差值
        total_water = 0
        for index in range(0, len(height)):
            water = min(left_max[index], right_max[index]) - height[index]
            if water > 0:
                total_water += water
        return total_water
