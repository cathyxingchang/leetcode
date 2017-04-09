#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 137_M
# Created by xc 18/03/2017
"""
    找到数组中都出现四次,而只有一个出现一次的数字
    之前没有做过这样的题目,感觉没什么下手的方法,看了网上的解法,尝试一下.
    首先我们说明:
    对于二进制的每一位,如果这个数字出现了三次,那么这个位置的1的个数肯定是3的倍数
    所以我们用两个数字来控制每一位

    相当于用两组数(因为是按位运算,实际上是两个数)来模拟3
    Two one 数在这一层的位数 Twonew OneNew
    0   0   1               0       1
    0   0   0               0       0
    0   1   0               0       1
    0   1   1               1       0
    1   0   0               1       0
    1   0   1               0       0

    1   1   0 (不存在3 在3的时候就已经清零了)
    1   1   1

    公式推导;感觉公式推导是个困难 ^ 是异或
    oneNew = (one^B)&(~two)
    TwoNew = (Two^B)& (~oneNew)
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_two = 0
        count_one = 0

        for item in nums:
            count_one = (count_one ^ item) & (~count_two)
            count_two = (count_two ^ item) & (~count_one)

        return count_one


