#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 198_E
# Created by xc 10/03/2017

"""
    动态规划,盗贼问题,不能连续偷两家,请问怎么偷利益最大化
    顺序通过
    推导出状态是很理想的
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        use_current = []
        use_current.append(nums[0])
        no_use_current = []
        no_use_current.append(0)

        for index in range(1, len(nums)):
            use_current.append(no_use_current[index - 1] + nums[index])
            no_use_current.append(max(use_current[index - 1], no_use_current[index - 1]))
        return max(no_use_current[len(nums)-1],use_current[len(nums)-1])