#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 413_M
# Created by xc 10/03/2017
"""
    找到数列里面,连续三个或者三个以上的等差数列,并统计所有数列的个数
"""
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        #
        if len(A) < 3:
            return 0
        count = 0
        this_list_count = 0
        d = [0, 0, ]
        for index in range(2, len(A)):
            if A[index] - A[index - 1] == A[index - 1] - A[index - 2]:
                # 符合数列的形式
                state = d[index-1] + 1
                d.append(state)
                this_list_count += state
            else:
                # 连续差值一样的数字断了.需要把上一个连续序列的放进去
                count += this_list_count
                this_list_count = 0
                d.append(0)
        # 把最后一个list放进来
        count += this_list_count
        return count
