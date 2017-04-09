#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 53_E
# Created by xc 19/03/2017

"""
    找到题目里面连续序列里最大的值
    思路:
    动态规划:
    开始想的是,从前往后,以当前元素为结尾的最大值.
    但是下一个元素因为是要跟上一个元素有联系的,这样的话,可能顺序就乱了.所以这样的顺序不对
        因为题目要求是连续,而下一个状态无法知道是不是前一个元素被使用了
        所以这个思路不对,再换个思路了.
    改成从d[i]为,从第i的元素开始的最大值
    为了保证顺序性,说明这个d[i]"必须必须必须必须"要使用上第i个元素

"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 因为是逆序,所以初始化所有状态
        if len(nums) == 0:
            return 0
        d = []
        max_sum = nums[-1]
        for index in range(0,len(nums)):
            d.append(0)

        d[len(nums)-1] = nums[-1]
        # 这里一定要注意细节,是否是逆序,
        for index in range(len(nums)-2, -1,-1):
            # 这里很关键,为了保证状态方程的有效性,一定保证nums[index]一定要被使用到
            d[index] = max(nums[index], nums[index] + d[index + 1])
            if d[index] > max_sum:
                max_sum = d[index]
        return max_sum


