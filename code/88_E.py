#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 88_E
# Created by xc 15/03/2017

"""
    字符串类的问题
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        index1 = m - 1
        index2 = n - 1
        merge_index = m + n - 1
        while index1 >= 0 and index2 >= 0:
            if nums1[index1] > nums2[index2]:
                nums1[merge_index] = nums1[index1]
                index1 -= 1
            else:
                nums1[merge_index] = nums2[index2]
                index2 -= 1
            merge_index -= 1
        if index1 >= 0:
            # 说明index2 已经全都放进去了 index1中的数据保持原位
            pass
        if index2 >= 0:
            # index2 没有放置完成,剩下的位置全部放置index2
            while index2 >= 0:
                nums1[merge_index] = nums2[index2]
                index2 -= 1
                merge_index -= 1
            # 或者
            #nums1[0:merge_index+1] = nums2[0:index2+1]