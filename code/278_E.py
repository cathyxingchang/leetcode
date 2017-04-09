#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 278_E
# Created by xc 14/03/2017

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 二分查找发
        begin = 1
        end = n
        while begin < end:
            mid = int(begin + end) / 2
            # 如果你把ver = (low + high)/2; 那就会出现超时错误，因为直接相加可能溢出，仅此一点，剩下的很简单
            # 故网上有优化如下:
            # ver = low + (high - low) / 2;
            if isBadVersion(mid):
                end = mid
            else:
                # 当前位置是正确的
                begin = mid + 1
        return begin


