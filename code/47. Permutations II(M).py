#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 47. Permutations II(M)
# Created by xc 14/04/2017
"""
    全排列,如何避免重复
    最基本的全排列是会有重复的,一方面可以使用字典去重,但是应该在生成的时候,就及时跳过一些重复元素
"""
import copy
class Solution(object):
    def __init__(self):
        self.result = []

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 首先 按照全排列的算法写
        permute_list = []
        for i in range(0, len(nums)):
            permute_list.append(nums[i])
            self.process(permute_list, nums[0: i] + nums[i + 1:])
            permute_list.pop()
        return self.result

    def process(self, permute_list, nums):
        if len(nums) == 0:
            self.result.append(copy.deepcopy(permute_list))
            # self.result.append(permute_list)
            return
        else:
            for i in range(0, len(nums)):
                permute_list.append(nums[i])
                self.process(permute_list, nums[0: i] + nums[i + 1:])
                permute_list.pop()


nums1 = [1,1,2]
test = Solution()
print test.permuteUnique(nums1)