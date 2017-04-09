#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 46_M
# Created by xc 13/03/2017
import copy
class Solution(object):
    def __init__(self):
        self.result = []

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.process(nums, 0, len(nums) - 1)
        return self.result

    def process(self, num_list, begin, end):
        # 生成 num_list的从begin到end的区间的全排列
        if begin == end:
            # 一组全排列生成了
            self.result.append(num_list)
            self.result[len(self.result) - 1] = copy.deepcopy(num_list)
            return
        for index in range(begin, end + 1):
            # 每个元素都当一次头,放置在最前面
            tmp = num_list[begin]
            num_list[begin] = num_list[index]
            num_list[index] = tmp
            self.process(num_list, begin + 1, end)
            # 处理完再交换回来
            tmp = num_list[begin]
            num_list[begin] = num_list[index]
            num_list[index] = tmp
