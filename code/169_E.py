#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 169_E
# Created by xc 15/03/2017
"""
    思路:排序后找到中位数
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        mid_index = int(len(nums) / 2)
        return sorted_nums[mid_index]
