#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 35_E
# Created by xc 15/03/2017

"""
    找到数组的位置 这个显然是一个二分查找法
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        begin = 0
        end = len(nums)-1
        while begin <= end:
            mid = int((begin + end) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1
        return begin

