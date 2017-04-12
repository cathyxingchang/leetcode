#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 90. Subsets II (M)
# Created by xc 11/04/2017

import itertools
class Solution(object):
    def __init__(self):
        self.result_map = {}
        self.result = []

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        for i in range(0, len(nums)+1):
            self.generate_combinations(nums, i)
            pass
        return self.result

    def generate_combinations(self, nums, m):
        # 生成m个数字的组合数
        # 直接调用库函数
        iter = itertools.combinations(nums, m)
        for item in iter:
            item = list(item)
            item.sort()
            if tuple(item) not in self.result_map:
                self.result.append(item)
                self.result_map[tuple(item)] = 1

nums = [4,4,4,1,4]
test = Solution()
print test.subsetsWithDup(nums)