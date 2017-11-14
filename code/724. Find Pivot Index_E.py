#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 724. Find Pivot Index_E
# Created by xc 14/11/2017

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        left_sum = [0]
        right_sum = [0]
        sum = 0
        for index in range(0, len(nums)):
            sum += nums[index]
            left_sum.append(sum)
        sum = 0
        for index in range(len(nums) - 1, -1, -1):
            sum += nums[index]
            right_sum.append(sum)
        right_sum = right_sum[::-1]
        #print left_sum
        #print right_sum
        for index in range(1, len(right_sum)):
            if left_sum[index-1] == right_sum[index]:
                return index -1
        return -1








#nums = [1,7,3,6,5,6]
#nums = [1,2,3]
#nums = []
#nums = [-1,-1,-1,-1,-1,0]
#nums = [-1,-1,0,1,0,-1]
#nums = [-1,-1,-1,0,1,1]
nums = [-1,-1,0,1,1,0]
test = Solution()
result = test.pivotIndex(nums)
print result