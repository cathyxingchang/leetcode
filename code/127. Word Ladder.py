#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 127. Word Ladder
# Created by xing 2017/4/2
import copy
class Solution(object):
    def __init__(self):
        self.lists = []

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # 首先把wordlist进行扩充
        word_length = len(beginWord)
        wordList.append(beginWord)
        # 首先构建每个word与之相连的word
        dict = {}
        for word in wordList:
            # 为当前的word构建的word构建一个与之相连的临接字典
            dict[word] = []
        # 填充临接字典
        for word in wordList:
            for index in range(0, word_length):
                for letter in range(97, 123):
                    # 字母替换
                    new_word = list(word)
                    if chr(letter) != new_word[index]:
                        new_word[index] = chr(letter)
                        if ''.join(new_word) in dict:
                            dict[word].append(''.join(new_word))
        # 广度优先遍历
        sets = dict[beginWord]
        dict.pop(beginWord)
        layer = 1
        while len(sets) != 0:
            layer += 1
            new_set = []
            if endWord in sets:
                return layer
            for item in sets:
                if item in dict:
                    link = dict[item]
                    for tmp in link:
                        if tmp in dict:
                            new_set.append(tmp)
                    dict.pop(item)
            sets = new_set
        return 0
