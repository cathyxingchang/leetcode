#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 78_M
# Created by xc 20/03/2017

"""
    思路:
    生成组合的升级版
"""
import copy


class Solution(object):
    def __init__(self):
        self.tmp_result = []
        self.combine_result = []

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        for counts in range(0, len(nums)+1):
            # 生成counts这么多数字的组合
            self.combine_result = []
            self.combine(nums, counts)
            result.extend(copy.deepcopy(self.combine_result))
        return result

    def combine(self, current_nums, counts):
        # 生成数组nums中,counts个数的组合_
        if counts == 0:
            self.combine_result.append(copy.deepcopy(self.tmp_result))
            return
        for index in range(0, len(current_nums)-counts + 1):
            self.tmp_result.append(current_nums[index])
            if index < len(current_nums)-1:
                self.combine(current_nums[index + 1:], counts - 1)
            else:
                self.combine([], counts - 1)
            self.tmp_result.pop()

numsxing = [1, 2, 3]
s = Solution()
print s.subsets(numsxing)
