#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 79. Word Search
# Created by xc 10/04/2017
"""
    给定一个字符串,判定字符矩阵中是否能找到这个字符串
    递归的思想,word每步进一步,就在四周找下一步
"""
class Solution(object):
    def __init__(self):
        self.flag = 0

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        used_matrix = [[0 for col in range(0, len(board[0]))] for row in range(0, len(board))]
        for i in range(0, len(board)):
            if self.flag == 1:
                break
            for j in range(0, len(board[0])):
                if self.flag == 1:
                    break
                self.process(word, used_matrix, board, i, j)
        if self.flag == 0:
            return False
        else:
            return True

    def process(self, word, used_matrix, board, row, col):
        """
        这个函数处理了当前word(从头开始),能否在board中找到下一条路
        :param word: 
        :param used_matrix: 
        :param board: 
        :param row: 
        :param col: 
        :return: 
        """
        if len(word) == 0:
            self.flag = 1
            return
        if row >= len(board) or row < 0 or col >= len(board[0]) or col < 0:
            return
        if word[0] == board[row][col] and used_matrix[row][col] == 0:
            used_matrix[row][col] = 1
            self.process(word[1:], used_matrix, board, row + 1, col)
            if self.flag == 1:
                return
            self.process(word[1:], used_matrix, board, row - 1, col)
            if self.flag == 1:
                return
            self.process(word[1:], used_matrix, board, row, col + 1)
            if self.flag == 1:
                return
            self.process(word[1:], used_matrix, board, row, col - 1)
            if self.flag == 1:
                return
            used_matrix[row][col] = 0

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
# T
word = ""
# T
#word = "SEE"
# F
#word = "ABCB"
word = "ABCCFC"


# 错误案例
board = ["aa","aa","aa"]
word = "aaaaaaa"
test = Solution()
print test.exist(board,word)