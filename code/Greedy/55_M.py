#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 55_M
# Created by xc 24/03/2017

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return True
        max_pool = 0
        for index in range(0, len(nums)):
            if index <= max_pool:
                # 当前元素是之前可达的
                # 计算当前的位置的步进长度
                step = nums[index]
                current_max_step = index + step
                if current_max_step > max_pool:
                    max_pool = current_max_step
                if max_pool >= len(nums)-1:
                    return True
            if index > max_pool:
                # 之前的元素都不能达到这里
                return False

s = Solution()
#nums = [2,3,1,1,4]
nums = []
print s.canJump(nums)