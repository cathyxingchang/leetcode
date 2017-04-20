#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 45. Jump Game II (H)
# Created by xc 19/04/2017

"""
    之前也有类似的Jump Game 是问能不能跳到
    这道题默认是可以跳到的
    询问最短的跳数
    
    动态规划
    d[i]代表能跳到d[i]需要的最小步数
    d[i] = min(之前所有能跳到它这里的步数最小的)+ 1 
    
    方法超时:90 / 92 test cases passed.
"""


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = [-1 for i in range(0, len(nums))]
        d[0] = 0
        for i in range(1, len(nums)):
            # 如果每一步都是只跳一步,最多要跳i步
            min_jump = i
            for j in range(0, i):
                if i-j <= nums[j]:
                    # 可以达到
                    if d[j] + 1 < min_jump:
                        min_jump = d[j] + 1
            d[i] = min_jump
        return d[-1]

nums = [2,3,1,1,4]
test = Solution()
print test.jump(nums)


