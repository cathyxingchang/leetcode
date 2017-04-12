#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 4. Median of Two Sorted Arrays(H)
# Created by xc 12/04/2017


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        # 保证l1是较长的数组
        if l1 < l2:
            return self.findMedianSortedArrays(nums2, nums1)
        if l2 == 0:
            return nums1[(l1-1)/2]
        low = 0
        high = l2 * 2
        while low < high:
            mid2 = (low + high) / 2
            mid1 = (l1 + l2 - mid2)

