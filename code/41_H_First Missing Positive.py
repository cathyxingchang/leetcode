#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 41_M_First Missing Positive
# Created by xc 28/03/2017

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for item in nums:
            if item > 0:
                dict[item] = 1
        for index in range(1, len(nums)+2):
            if index not in dict:
                return index

nums = [-1,-1,3]
test = Solution()
print test.firstMissingPositive(nums)
