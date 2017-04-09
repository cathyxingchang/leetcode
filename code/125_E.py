#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 125_E
# Created by xc 15/03/2017

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        begin = 0
        end = len(s)-1
        s = s.lower()
        while True:
            # 这里又是特别注意的顺序问题 and 前后两个条件,是有顺序的
            while begin <= len(s)-1 and self.is_alphanumeric(s[begin]) == False:
                begin += 1
            while end >= 0 and self.is_alphanumeric(s[end]) == False:
                end -= 1
            if begin == end:
                # 到达了中心点的位置
                return True
            if begin > end:
                # 已经移动到错位的部分了
                return True
            # 大小写转换
            if s[begin] != s[end]:
                return False
            begin += 1
            end -= 1

    def is_alphanumeric(self,letter):
        if letter >= 'a' and letter <= 'z' or letter >= 'A' and letter <= 'Z' or letter >= '0' and letter <= '9':
            return True
        else:
            return False
