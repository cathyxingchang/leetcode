#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 75_M_Sort Colors
# Created by xc 29/03/2017

"""
        一道有关于排序算法的问题
        冒泡排序
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp
        #return nums
