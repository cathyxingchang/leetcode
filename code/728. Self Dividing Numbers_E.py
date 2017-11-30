#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 728. Self Dividing Numbers_E
# Created by xc 30/11/2017

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for num in range(left, right+1):
            if self.isSelfDividingNumber(num):
                result.append(num)
        return result

    def isSelfDividingNumber(self, num):
        if num == 0:
            return False
        tmp = num
        while tmp != 0:
            current = tmp % 10
            if current == 0 or num % current != 0:
                return False
            tmp /= 10
        return True


test = Solution()
left = 0
right =22
print test.selfDividingNumbers(left, right)

