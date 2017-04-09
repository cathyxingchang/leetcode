#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 16_M
# Created by xc 22/03/2017

"""
    3Sum Closest: twoSum的一个扩展

"""
class Solution(object):
    def __init__(self):
        self.min_dist = 0
        self.min_list = []
        self.given_target = 0

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            # 长度小于3是无效的
            return 0

        self.min_dist = abs(nums[0] + nums[1] + nums[2] - target)
        self.min_list = [nums[0], nums[1], nums[2]]
        self.given_target = target
        # 首先排序
        nums.sort()
        for index in range(0, len(nums)-2):
            self.twoSum(self.given_target-nums[index], nums[index+1:])
            if self.min_dist == 0:
                return self.min_list[0] + self.min_list[1] + self.min_list[2]
        return self.min_list[0] + self.min_list[1] + self.min_list[2]

    def twoSum(self, target, nums):
        begin = 0
        end = len(nums)-1
        while begin < end:
            if nums[begin] + nums[end] > target:
                if abs(nums[begin] + nums[end] - target) < self.min_dist:
                    self.min_dist = abs(target - nums[begin] - nums[end])
                    self.min_list = [self.given_target - target, nums[begin], nums[end]]
                end -= 1
            elif nums[begin] + nums[end] < target:
                if abs(nums[begin] + nums[end] - target) < self.min_dist:
                    self.min_dist = abs(target - nums[begin] - nums[end])
                    self.min_list = [self.given_target - target, nums[begin], nums[end]]
                begin += 1
            else:
                self.min_dist = 0
                self.min_list = [self.given_target - target, nums[begin], nums[end]]
                break

s = Solution()
nums = [0, 1, 2]
target = 0
print s.threeSumClosest(nums, target)
