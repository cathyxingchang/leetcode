#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 15_M
# Created by xc 21/03/2017
"""
    3Sum问题:
    排序后转化为2sum问题
    运行时间 1482ms
"""
import time

class Solution(object):
    def __init__(self):
        # 为了方便剔除重复的元素,使用字典进行保存
        self.dic = {}
        self.result = []

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 排序后转成2sum问题
        nums.sort()
        # 可以排除一部分重复的数据
        before_num = None
        for index in range(0, len(nums)-2):
            # 把3sum问题转化为2sum问题
            if before_num is None:
                before_num = nums[index]
                self.twoSum(nums[index+1:], nums[index]*(-1))
            else:
                if before_num == nums[index]:
                    # 重复数据不做处理
                    continue
                else:
                    self.twoSum(nums[index + 1:], nums[index] * (-1))

        for key in self.dic:
            num_set = [key[0], key[1], key[2]]
            self.result.append(num_set)
        return self.result

    def twoSum(self, nums, target):
        begin = 0
        end = len(nums)-1
        while begin < end:
            if nums[begin]+nums[end] == target:
                key = (-1 * target, nums[begin], nums[end])
                self.dic[key] = 1
                # 还需要找下一组和符合的
                end -= 1
                begin += 1
            elif nums[begin]+nums[end] > target:
                end -= 1
                pass
            else:
                begin += 1

nums = [-1, 0, 1, 2, -1, -4]
start = time.clock()
s = Solution()
print s.threeSum(nums)
end = time.clock()
total_time = (end - start)*1000
print "运行时间: %f ms" % total_time