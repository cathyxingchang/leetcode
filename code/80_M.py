#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 80_M
# Created by xc 21/03/2017

"""
    删除数组中的重复元素:
    策略: 两个指针,一个指着当前,一个往后(其实你从题目中的要求就知道,不需要处理超过数组长度的部分)
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        new_index = 0
        tag = 0
        for index in range(1, len(nums)):
            if nums[index] == nums[new_index]:
                tag += 1
                if tag == 1:
                    # 重复了一次,这一次是有效的
                    new_index += 1
                    nums[new_index] = nums[index]
            else:
                # 不相等
                tag = 0
                new_index += 1
                nums[new_index] = nums[index]
        return new_index+1


nums = [1,1,1]
s = Solution()
a= s.removeDuplicates(nums)
print a
