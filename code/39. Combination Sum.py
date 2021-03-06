#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 39. Combination Sum
# Created by xc 12/04/2017

"""
    获得所有和为target值的数字的组合
    167 / 168 test cases passed.
    超时了,有一个测试点不能顺利的通过
"""
import time
class Solution(object):
    def __init__(self):
        self.result = {}

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 首先,对候选数字进行排序,方便不对重复的数字进行处理
        candidates.sort()
        current_list = []
        current_sum = 0
        last_num = None
        for item in candidates:
            if last_num is not None:
                # 开头不需要重复的数字
                if last_num == item:
                    continue
            last_num = item
            current_sum += item
            current_list.append(item)
            self.process(current_sum, current_list, target, candidates)
            current_list.pop()
            current_sum -= item
        final_list = []
        for key in self.result:
            final_list.append(list(key))
        return final_list

    def process(self, current_sum, current_list, target, candidates):
        if current_sum > target:
            return
        if current_sum == target:
            self.result[tuple(sorted(current_list))] = 1
            return
        for item in candidates:
            current_sum += item
            current_list.append(item)
            self.process(current_sum, current_list, target, candidates)
            current_list.pop()
            current_sum -= item

start = time.clock()

candidatess = [92,71,89,74,102,91,70,119,86,116,114,106,80,81,115,99,117,93,76,77,111,110,75,104,95,112,94,73]
310
targets = 310
test = Solution()
print test.combinationSum(candidatess,targets)

end = time.clock()
total_time = (end - start)*1000
print total_time