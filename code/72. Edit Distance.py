#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 72. Edit Distance
# Created by xc 11/04/2017
"""
    感觉上,像是一道动态规划的题目
    d[i][j] 表示word1前i个字母和word[j]的前j个字母变换的次数
    d[i][j] = 如果ij相等,那么就是 min(d[i-1]d[j-1] , d[i-1][j] + 1, d[i][j-1]+ 1)
              如果ij不相等  那么就是  min(d[i-1]d[j-1] +1, d[i-1][j] + 1, d[i][j-1]+ 1 )
    
"""


class Solution(object):
    def minDistance(self, word1, word2):
        # 为了方便计算,在word1 和word 2之前插入一个单独的字符
        l1 = ['']
        l2 = ['']
        for item in word1:
            l1.append(item)
        for item in word2:
            l2.append(item)
        d = [[0 for col in range(0, len(l2))] for row in range(0, len(l1))]

        # 矩阵初始赋值
        d[0][0] = 0
        for i in range(1, len(l1)):
            d[i][0] = i
        for i in range(1, len(l2)):
            d[0][i] = i

        for i in range(1, len(l1)):
            for j in range(1, len(l2)):
                if l1[i] == l2[j]:
                    d[i][j] = min(d[i - 1][j - 1], d[i - 1][j] + 1, d[i][j - 1] + 1)
                else:
                    d[i][j] = min(d[i - 1][j - 1], d[i - 1][j], d[i][j - 1]) + 1
        return d[len(l1)-1][len(l2)-1]

word1 = 'abc'
word2 = 'bca'

word1 = 'mmm'
word2 = 'aaa'

word1 = 'dad'
word2 = 'bcad'
test = Solution()
print test.minDistance(word1, word2)
