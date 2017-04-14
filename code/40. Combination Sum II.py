#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 40. Combination Sum II
# Created by xc 14/04/2017
"""
    和上一题完全一样的思路呀
    
"""
class Solution(object):
    def __init__(self):
        self.result_dict = {}
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        num_set = []
        before = None
        current_sum = 0
        for i in range(0, len(candidates)):
            if before is None or candidates[i] != before:
                num_set.append(candidates[i])
                current_sum += candidates[i]
                self.process(num_set, current_sum, target, candidates[i+1:])
                current_sum -= candidates[i]
                num_set.pop()
            before = candidates[i]

        # 输出结果
        result = []
        for key in self.result_dict:
            result.append(list(key))
        return result

    def process(self, num_set, current_sum, target, candidates):
        """
        递归处理
        :param num_set: 当前已经在炫动的set里的
        :param current_sum: 当前的和
        :param target: 目标数字
        :param candidates: 当前的候选数字
        :return: 
        """
        if current_sum == target:
            self.result_dict[tuple(num_set)] = 1
            return
        if len(candidates) == 0:
            # 候选元素没有了
            return
        if current_sum > target:
            # 超过了
            return
        for i in range(0, len(candidates)):
            num_set.append(candidates[i])
            current_sum += candidates[i]
            self.process(num_set, current_sum, target, candidates[i+1:])
            num_set.pop()
            current_sum -= candidates[i]



candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
test = Solution()
print test.combinationSum2(candidates,target)