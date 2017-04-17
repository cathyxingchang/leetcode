#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 189. Rotate Array(E)
# Created by xc 17/04/2017
"""
    这道题要求用三种方式进行解决
    nums向右移动k位
    k = k%7
    等价于 ,后k位逆转,前n-k位逆转,最后全部逆转
    
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n != 0:
            k = k % n

            # 翻转前n-k位
            i = 0
            j = n - k - 1
            while i < j:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i += 1
                j -= 1

            # 翻转后k位
            i = n-k
            j = n-1
            while i < j:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i += 1
                j -= 1

            # 整体翻转
            i = 0
            j = n - 1
            while i < j:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i += 1
                j -= 1


nums = [1,2,3,4,5,6,7]
k = 0
test = Solution()
test.rotate(nums, k)