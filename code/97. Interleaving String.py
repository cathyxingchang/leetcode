#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 97. Interleaving String
# Created by xc 31/03/2017

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        s1_length = len(s1)
        s2_length = len(s2)
        if len(s1) + len(s2) != len(s3):
            return False
        # 构建一个二维的矩阵,行列是
        row = s1_length + 1
        col = s2_length + 1

        #

        # 初始化矩阵
        matrix = [[0 for i in range(0, col)] for j in range(0, row)]
        # 首先初始化矩阵的第一列和第一行
        # 第一列
        matrix[0][0] = True
        # 临时变量,辅助赋初值
        flag = True
        for index in range(1, row):
            if flag:
                if s1[index-1] == s3[index-1]:
                    matrix[index][0] = True
                else:
                    matrix[index][0] = False
                    flag = False
            else:
                matrix[index][0] = False
        flag = True
        for index in range(1, col):
            if flag:
                if s2[index - 1] == s3[index - 1]:
                    matrix[0][index] = True
                else:
                    matrix[0][index] = False
                    flag = False
            else:
                matrix[0][index] = False

        for i in range(1, row):
            for j in range(1, col):
                matrix[i][j] = (matrix[i-1][j] and s3[i+j-1] == s1[i-1]) or (matrix[i][j-1] and s3[i+j-1] == s2[j-1])
        #print matrix
        return matrix[-1][-1]




s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
test = Solution()
print test.isInterleave(s1,s2,s3)