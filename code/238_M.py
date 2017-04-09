#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 238_M
# Created by xc 09/03/2017

# [1,2,3,4]
# [1,1,2,6]: 当前元素左面的乘积
# [24,12,4,1]
# 这样的话,我只要两个数组就可以了.
# 但是他又说,不要额外空间.那么说明我只要把right放进nums里,然后最后的result 直接放进left里,那么久符合了不开额外空间的需求
# 完美解决~~
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []

        left_product = []
        for i in range(0, len(nums)):
            left_product.append(1)
        right_product = []
        for i in range(0, len(nums)):
            right_product.append(1)

        # 计算每个位置当前元素左面的乘积
        current_product = 1
        for index in range(1, len(nums)):
            current_product *= nums[index-1]
            left_product[index] = current_product

        # 计算每个位置当前元素右面的乘积
        current_product = 1
        for index in range(len(nums)-2, -1, -1):
            current_product *= nums[index + 1]
            right_product[index] = current_product

        for index in range(0, len(nums)):
            result.append(left_product[index]*right_product[index])
        return result


