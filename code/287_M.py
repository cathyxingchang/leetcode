#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 287_M
# Created by xc 10/03/2017

"""
    找到重复的元素,只能用o(1)的空间和 O(n^2)的复杂度
    思路: 因为两个元素相同的话,那么异或就是0,所以每个元素都不断的异或,
    因为异或运算在两个数字相同时为0,当前总的异或结果不会变
    上面的思路不对
"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


