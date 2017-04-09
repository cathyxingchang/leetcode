#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 345_E
# Created by xc 14/03/2017

"""
    345. Reverse Vowels of a String
    只对字符串里的元音字母进行翻转
"""

import copy


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_s = list(s)
        # 一定要认真看题,考虑大小写的情况
        vowels_set = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # 设定两个指针,来移动用来翻转元音字母
        begin = 0
        end = len(list_s) - 1
        while True:
            while begin < len(list_s) and list_s[begin] not in vowels_set:
                begin += 1
            while end >= 0 and list_s[end] not in vowels_set:
                end -= 1
            if begin < end:
                # 元素翻转
                tmp = list_s[begin]
                list_s[begin] = copy.deepcopy(list_s[end])
                list_s[end] = copy.deepcopy(tmp)
                begin += 1
                end -= 1
            else:
                break

        return "".join(list_s)

