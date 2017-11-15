#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 476. Number Complement_E
# Created by xc 15/11/2017

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_list = []
        if num == 0:
            return 1
        while num != 0:
            num_list.append(num % 2)
            num /= 2
        # 遍历  累积
        print num_list

        pow_2 = 1
        result = 0
        for item in num_list:
            result += (1-item) * pow_2
            pow_2 *= 2
        return result

test = Solution()
num = 15
result = test.findComplement(num)
print result