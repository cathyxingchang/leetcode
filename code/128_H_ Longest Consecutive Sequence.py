#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 128_H_ Longest Consecutive Sequence
# Created by xc 28/03/2017

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        max_length = 0
        for item in nums:
            dict[item] = 1
        for key in dict:
            if dict[key] == 0:
                # 之前已经被检索过了
                continue
            i = key
            j = key
            while i in dict:
                dict[i] = 0
                i -= 1
            while j in dict:
                dict[j] = 0
                j += 1

            length = (j - 1) - (i + 1) + 1
            if length > max_length:
                max_length = length
        return max_length

nums = []
test = Solution()
print test.longestConsecutive(nums)