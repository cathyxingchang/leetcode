#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 500_E
# Created by xc 14/03/2017

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'], ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
               ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
        result = []
        for single_word in words:
            single_word_lower = single_word.lower()
            single_word_list = list(single_word_lower)
            if single_word_list[0] in row[0]:
                tag = 0
            elif single_word_list[0] in row[1]:
                tag = 1
            elif single_word_list[0] in row[2]:
                tag = 2
            else:
                # 首部字母非三行键盘
                continue
            state = True
            for letter in range(1, len(single_word_list)):
                if single_word_list[letter] not in row[tag]:
                    state = False
                    break
            # 直到最后一个字母都在里面
            if state:
                result.append(single_word)
        return result