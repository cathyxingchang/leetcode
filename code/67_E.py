#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 67_E
# Created by xc 16/03/2017


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = list(a)
        b = list(b)
        new_a = a[::-1]
        new_b = b[::-1]
        # 给短的字符串补0
        if len(new_a) > len(new_b):
            # 给b后面补0
            for index in range(0,len(new_a)-len(new_b)):
                new_b.append(0)
        else:
            # 给a 后面补0
            for index in range(0,len(new_b)-len(new_a)):
                new_a.append(0)

        # 求和
        jinwei = 0
        sum = []
        for index in range(0, len(new_a)):
            tmp_sum = int(new_a[index]) + int(new_b[index]) + jinwei
            jinwei = int(tmp_sum / 2)
            number = tmp_sum % 2
            sum.append(number)
        if jinwei == 1:
            sum.append(1)

        # 翻转sum
        sum = sum[::-1]
        result = ""
        for item in sum:
            result += str(item)
        return result
