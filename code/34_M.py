#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 34_M
# Created by xc 27/03/2017

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        begin = 0
        end = len(nums)-1
        location = -1
        while begin <= end:
            mid = (begin + end) / 2
            if nums[mid] == target:
                location = mid
                break
            elif nums[mid] > target:
                end = mid-1
            else:
                begin = mid + 1
        if location == -1:
            return [-1, -1]

        i = location
        j = location
        while i >= 0 and nums[i] == target:
            i -= 1
        while j < len(nums) and nums[j] == target:
            j += 1
        return [i + 1, j - 1]

nums_list = [5, 7, 7, 8, 8, 10]
nums_list = []
target = 1
s = Solution()
print s.searchRange(nums_list, target)