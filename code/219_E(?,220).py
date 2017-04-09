#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 219_E
# Created by xc 14/03/2017

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 字符串的长度小于k
        if len(nums) == 0 or k == 0:
            return False
        if len(nums) <= k:
            for index1 in range(0, len(nums)):
                for index2 in range(index1 + 1, len(nums)):
                    if nums[index1] == nums[index2]:
                        return True
            return False

        for index1 in range(0, len(nums)):
            for index2 in range(index1 + 1, len(nums)):
                if index2 - index1 > k:
                    break
                if nums[index1] == nums[index2]:
                    return True
        return False
