#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 11_M
# Created by xc 13/03/2017

"""
    水槽问题,计算一个高高低低的水槽能储存多少水
    某一个位置的水槽能放进的最大的水量 就是它左面最大和右面最大里面较小的那个,然后跟自己的差
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        current_left_max = height[0]
        left_max = []
        for index in range(0, len(height)):
            left_max.append(0)
        for index in range(1, len(height)):
            # 计算当前元素左面最大的数字
            if height[index-1] > current_left_max:
                current_left_max = height[index-1]
            left_max[index] = current_left_max

        right_max = []
        current_right_max = height[len(height)-1]
        # 为了方便,这里我们直接先生成一个右面最大的数组,便于从最后向前放置数字
        for index in range(0, len(height)):
            right_max.append(0)
        for index in range(len(height)-2, -1, -1):
            # 计算当前元素右面最大的数字
            if height[index + 1] > current_right_max:
                current_right_max = height[index + 1]
            right_max[index] = current_right_max

        # 计算每个位置存水量
        sum = 0
        for index in range(0, len(height)):
            water = min(left_max[index], right_max[index]) - height[index]
            if water > 0:
                sum += water
        return sum
