#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 387_E
# Created by xc 14/03/2017

"""
    方法一:
    93 / 104 test cases passed.
    无法通过长测试样例
"""
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        # 设定初始的tag标志位
        tag = []
        for index in range(0, len(s)):
            tag.append(0)

        for index1 in range(0, len(s)):
            if tag[index1] == 1:
                continue
            for index2 in range(index1 + 1, len(s)):
                if tag[index2] == 1:
                    continue
                if s[index1] == s[index2]:
                    tag[index1] = 1
                    tag[index2] = 1
            if tag[index1] == 0:
                return index1
        return -1

