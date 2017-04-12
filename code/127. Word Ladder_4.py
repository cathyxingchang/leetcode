#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 127. Word Ladder
# Created by xing 2017/4/2
"""
    随用随生成字典
    双向bfs
"""
import time
class Solution(object):
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
        # 首先生成一个字典，里面存的是所有的word
        wordMap_begin = {}
        wordMap_end = {}
        for item in wordList:
            wordMap_begin[item] = 1
            wordMap_end[item] = 1
        if endWord not in wordMap_end:
            return 0

        # 广度优先遍历
        # 出发结点
        sets_begin = {}
        # 找到所有跟beginWord相连的字符，存进sets里
        for index in range(0, word_length):
            new_word = list(beginWord)
            for letter in "abcdefghijklmnopqrstuvwxyz":
                # 字母替换
                new_word[index] = letter
                tmp_word = ''.join(new_word)
                if tmp_word in wordMap_begin:
                    sets_begin[tmp_word] = 1
        # 终点结点
        sets_end = {}
        # 找到所有跟beginWord相连的字符，存进sets里
        for index in range(0, word_length):
            new_word = list(endWord)
            for letter in "abcdefghijklmnopqrstuvwxyz":
                # 字母替换
                new_word[index] = letter
                tmp_word = ''.join(new_word)
                if tmp_word in wordMap_begin:
                    sets_end[tmp_word] = 1

        layer = 1
        if endWord in sets_begin or beginWord in sets_end:
            return 2
        # 判断是否存在从重复
        for key_begin in sets_begin:
            for key_end in sets_end:
                if key_begin == key_end:
                    return layer * 2 + 1

        while len(sets_begin) != 0 and len(sets_end) != 0:
            layer += 1
            new_set_begin = {}
            new_set_end = {}
            for item in sets_begin:
                if wordMap_begin[item] == 1:
                    # 找到所有与item相连的
                    for index in range(0, word_length):
                        new_word = list(item)
                        for letter in "abcdefghijklmnopqrstuvwxyz":
                            # 字母替换
                            new_word[index] = letter
                            tmp_word = ''.join(new_word)
                            if tmp_word in wordMap_begin and wordMap_begin[tmp_word] == 1:
                                new_set_begin[tmp_word] = 1
                    wordMap_begin[item] = 0
            sets_begin = new_set_begin

            # 判断两个set是否重合
            for key_begin in sets_begin:
                for key_end in sets_end:
                    if key_begin == key_end:
                        return layer * 2

            for item in sets_end:
                if wordMap_end[item] == 1:
                    # 找到所有与item相连的
                    for index in range(0, word_length):
                        new_word = list(item)
                        for letter in "abcdefghijklmnopqrstuvwxyz":
                            # 字母替换
                            new_word[index] = letter
                            tmp_word = ''.join(new_word)
                            if tmp_word in wordMap_end and wordMap_end[tmp_word] == 1:
                                new_set_end[tmp_word] = 1
                    wordMap_end[item] = 0
            sets_end = new_set_end

            # 判断两个set是否重合
            for key_begin in sets_begin:
                for key_end in sets_end:
                    if key_begin == key_end:
                        return layer * 2 + 1
        return 0

s = Solution()
from bigger import big_arr, big_arr2
print time.time()
print s.ladderLength("sand", "acne", big_arr)  # 11
print time.time()
exit()
print s.ladderLength("nape", "mild", big_arr2) # 6
print time.time()

print s.ladderLength("kiss",
"tusk",
["miss","dusk","kiss","musk","tusk","diss","disk","sang","ties","muss"]) # 5
print s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) # 5