#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 89. Gray Code
# Created by xc 11/04/2017

"""
    如此暴力的解法,直接生产格雷码,竟然也过了测试点了....
"""
import math


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        num = int(math.pow(2, n))
        result.append(0)
        code = ['0' for i in range(0, n)]
        for index in range(1, num):
            if index % 2 != 0:
                code[-1] = self.change(code[-1])
                pass
            else:
                for i in range(n-1, -1, -1):
                    if code[i] == '1':
                        left = i - 1
                        break
                # 改变left
                code[left] = self.change(code[left])
            current_number = int(''.join(code), base=2)
            result.append(current_number)
        return result

    def change(self, code):
        if code == '0':
            return '1'
        else:
            return '0'

test = Solution()
print test.grayCode(20)


