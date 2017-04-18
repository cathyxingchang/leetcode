#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 151. Reverse Words in a String(M)
# Created by xc 18/04/2017

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_list = s.split()
        print str_list
        if len(str_list) == 0:
            return ""
        begin = 0
        end = len(str_list) - 1
        while begin < end:
            tmp = str_list[begin]
            str_list[begin] = str_list[end]
            str_list[end] = tmp
            begin += 1
            end -= 1
        result_str = ""
        for index in range(0, len(str_list)-1):
            result_str += str_list[index]
            result_str += ' '
        result_str += str_list[-1]
        return result_str

s = "the sky is blue"
s = " "
test = Solution()
print test.reverseWords(s)