#!/usr/bin/env python
# -*- coding: utf-8 -*-

# xingchang
# Created by yangchao 02/04/2017
import time
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
        wordList.append(beginWord)
        # 首先构建每个word与之相连的word
        wordMap = {}
        for word in wordList:
            # 为当前的word构建的word构建一个与之相连的临接字典
            wordMap[word] = {}
        # 填充临接字典
        word_size = len(beginWord)
        for word in wordList:
            for index in range(word_size):
                tmpword = list(word)
                for i in range(97, 123):
                    letter = chr(i)
                    # 字母替换
                    if letter != tmpword[index]:
                        tmpword[index] = letter
                        new_word = ''.join(tmpword)
                        if new_word in wordMap:
                            wordMap[word][new_word] = 1
        print time.time(), 1
        # 广度优先遍历
        sets = {beginWord: 0}
        layer = 1
        while len(sets) != 0:
            new_set = {}
            if endWord in sets:
                return layer

            layer += 1
            for item in sets:
                for next_word in wordMap[item]:
                    if next_word not in new_set:
                        new_set[next_word] = 0
                wordMap[item] = {}
            sets = new_set
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