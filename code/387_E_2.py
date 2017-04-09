#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 387_E_2
# Created by xc 14/03/2017

"""
    方法二:
    由于方法一无法通过长样例,由于都是26个字母表,所以我们可以通过控制tag_Alphabet的位数来判断
    也就是这次只设定26个tag位,来简化运算

    这次通过了.感觉算法的策略真的挺关键的
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        tag_alphabet = []
        for index in range(0, 26):
            tag_alphabet.append(0)
        #s = list(s)
        for index1 in range(0, len(s)):
            # 遍历当前字符串的每一个位置
            if tag_alphabet[ord(s[index1])-ord('a')] == 1:
                # 这个字母之前已经存在过了
                continue
            for index2 in range(index1 + 1, len(s)):
                if s[index1] == s[index2]:
                    # 后面出现了重复字母,这个字母已经出现过了
                    tag_alphabet[ord(s[index1])-ord('a')] = 1
                    break
            # 后面都没有出现过这个字母
            if tag_alphabet[ord(s[index1])-ord('a')] == 0:
                return index1
        return -1

