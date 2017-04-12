#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 127. Word Ladder
# Created by xing 2017/4/2
"""
    随用随生成字典
    39 / 39 test cases passed.
    Status: Accepted
    Runtime: 948 ms
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
        wordMap = {}
        for item in wordList:
            wordMap[item] = 1

        # 广度优先遍历
        sets = {}
        # 找到所有跟beginWord相连的字符，存进sets里
        for index in range(0, word_length):
            new_word = list(beginWord)
            for letter in "abcdefghijklmnopqrstuvwxyz":
                # 字母替换
                new_word[index] = letter
                tmp_word = ''.join(new_word)
                if tmp_word in wordMap:
                    sets[tmp_word] = 1
        layer = 1
        while len(sets) != 0:
            layer += 1
            new_set = {}
            if endWord in sets:
                return layer
            for item in sets:
                if wordMap[item] == 1:
                    # 找到所有与item相连的
                    for index in range(0, word_length):
                        new_word = list(item)
                        for letter in "abcdefghijklmnopqrstuvwxyz":
                            # 字母替换
                            new_word[index] = letter
                            tmp_word = ''.join(new_word)
                            if tmp_word in wordMap and wordMap[tmp_word] == 1:
                                new_set[tmp_word] = 1
                    wordMap[item] = 0
            sets = new_set
        return 0

s = Solution()
from bigger import big_arr, big_arr2
start = time.clock()

print s.ladderLength("sand", "acne", big_arr)  # 11
end = time.clock()
total_time = (end - start)*1000
print total_time
print s.ladderLength("nape", "mild", big_arr2) # 6
