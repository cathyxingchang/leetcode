#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 167. Two Sum II - Input array is sorted(E)
# Created by xc 17/04/2017

"""
    twosum的简单的问题, 本身有序,需要返回下标
"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        begin = 0
        end = len(numbers) - 1
        while begin < end:
            if numbers[begin] + numbers[end] == target:
                return [begin + 1, end + 1]
            elif numbers[begin] + numbers[end] > target:
                end -= 1
            else:
                begin += 1

numbers = [2, 3, 5]
target = 6
test = Solution()
print test.twoSum(numbers, target)