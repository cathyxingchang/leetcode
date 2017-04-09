#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 11_M
# Created by xc 27/03/2017
"""
    题目看仔细了,都是水的问题,要认真审题
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        begin = 0
        end = len(height) - 1
        # 水量 两个数字较小的*距离
        max_water = min(height[begin], height[end]) * abs(begin - end)
        while begin < end:
            current_water = min(height[begin], height[end]) * abs(begin - end)
            if current_water > max_water:
                max_water = current_water
            else:
                if height[begin] > height[end]:
                    end -= 1
                else:
                    begin += 1
        return max_water

s = Solution()
height = [1,5,2,4,6]
print s.maxArea(height)