#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 168. Excel Sheet Column Title(E)
# Created by xc 27/04/2017

import string
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""
        letter_map = {}
        index = 0
        for letter in string.uppercase:
            letter_map[index] = letter
            index += 1
        while n != 0:
            result += letter_map[(n-1) % 26]
            n = (n-1) / 26
        return result[::-1]


n = 26
test = Solution()
print test.convertToTitle(n)
