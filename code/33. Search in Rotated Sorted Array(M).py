#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 33. Search in Rotated Sorted Array(M)
# Created by xc 14/04/2017
"""
    参考了别人的算法才做出来
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        begin = 0
        end = len(nums) - 1
        while begin <= end:
            mid = (end + begin) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[begin]:
                # mid在左面
                if nums[mid] > target and nums[begin] <= target:
                    end = mid - 1
                else:
                    begin = mid + 1
                pass
            else:
                # mid在右面
                if nums[mid] <= target and nums[end] >= target:
                    begin = mid + 1
                else:
                    end = mid - 1
        return -1

nums = [4,5,6,7,0,1,2]
target = 3
test = Solution()
print test.search(nums, target)