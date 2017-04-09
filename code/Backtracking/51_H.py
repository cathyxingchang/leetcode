#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 51_H
# Created by xc 27/03/2017
import copy
class Solution(object):
    def __init__(self):
        self.n = 0
        self.result = []

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        # 首先构建一个n*n的数组,用于存储当前的棋盘图
        checker_board = [['.' for i in range(0, n)] for j in range(0, n)]

        # 首先需要给定第一层放置的位置
        for col in range(0, n):
            # 遍历当前层的每一列
            checker_board[0][col] = 'Q'
            self.process(checker_board, 1)
            checker_board[0][col] = '.'
        #print len(self.result)
        return self.result

    def process(self, checker_board, layer):
        """
        n皇后的处理流程
        :param self:
        :param checker_board: 当前的棋盘格状态
        :param layer: 当前准备处理的层数(还没处理,函数内处理)
        :return:
        """
        if layer == self.n:
            # 已经到了最后一层了
            # 把checkboard 转化为字符串list
            tmp_result = [''.join(checker_board[i]) for i in range(0, self.n)]
            self.result.append(copy.deepcopy(tmp_result))
            return
        for col in range(0, self.n):
            flag = 0
            # 判定这个位置是否合法
            # 1. 判断这一列是否有Q
            for i in range(0, layer):
                if checker_board[i][col] == 'Q':
                    flag = 1
                    break
            # 2.对角线左上角
            i = layer - 1
            j = col - 1
            while i >= 0 and j >= 0 and flag == 0:
                if checker_board[i][j] == 'Q':
                    flag = 1
                    break
                i -= 1
                j -= 1

            # 3.对角线右上角
            i = layer - 1
            j = col + 1
            while i >= 0 and j < self.n and flag == 0:
                if checker_board[i][j] == 'Q':
                    flag = 1
                    break
                i -= 1
                j += 1

            if flag == 1:
                continue

            # 合法,则赋值
            checker_board[layer][col] = 'Q'
            # self.process(copy.deepcopy(checker_board), layer + 1)
            # 这里其实无需deepcopy因为后面你又改回来了
            self.process(checker_board, layer + 1)
            checker_board[layer][col] = '.'


s = Solution()
n = 8
print s.solveNQueens(n)