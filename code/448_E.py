#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 448_E
# Created by xc 09/03/2017


# 这个也不过,时间复杂度太大了么???
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict = {}
        result = []
        for item in nums:
            dict[item] = 1
        for index in range(1, len(nums)+1):
            if index not in dict.keys():
                # 字典里没有这个key
                result.append(index)
        return result

# 还是超时
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for index in range(1, len(nums)+1):
            if index not in nums:
                result.append(index)
        return result

# 以上的两个方法