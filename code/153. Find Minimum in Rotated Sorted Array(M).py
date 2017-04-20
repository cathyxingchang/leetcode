#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 153. Find Minimum in Rotated Sorted Array(M)
# Created by xc 18/04/2017
"""
    不会做 参考别人的算法
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return

        begin = 0
        end = len(nums) - 1
        min_num = nums[0]
        while begin < end:
            mid = (begin + end) / 2
            if nums[mid] > nums[end]:
                # 那就说明mid之前的数字都可以扔了
                begin = mid + 1
            else:
                # mid和其之前的元素是有可能的(删掉了后面大的)
                end = mid
        return nums[end]

