#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 39. Combination Sum
# Created by xc 12/04/2017

"""
    获得所有和为target值的数字的组合
    修改查询策略,当前元素为开头,只往后找,不往前找
    单次的大数字数据时间上不会缩小很多,但是很多测试样例总的时间短了
    顺利通过
    Your runtime beats 14.87% of python submission
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
        for index in range(0, len(candidates)):
            item = candidates[index]
            if last_num is not None:
                # 开头不需要重复的数字
                if last_num == item:
                    continue
            last_num = item
            current_sum += item
            current_list.append(item)
            # 优化修改
            # self.process(current_sum, current_list, target, candidates)
            self.process(current_sum, current_list, target, candidates[index:])
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
        for index in range(0, len(candidates)):
            item = candidates[index]
            current_sum += item
            current_list.append(item)
            # 优化修改
            # self.process(current_sum, current_list, target, candidates)
            self.process(current_sum, current_list, target, candidates[index:])

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