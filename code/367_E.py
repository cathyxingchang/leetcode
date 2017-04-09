#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 367_E
# Created by xc 14/03/2017
"""
 二分查找法
"""
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0 or num ==1:
            return True
        begin = 1
        end = int(num / 2)
        while begin <= end:
            mid = int((begin + end) / 2)
            result = mid * mid
            if result > num:
                end = mid - 1
            elif result < num:
                begin = mid + 1
            else:
                return True
        return False