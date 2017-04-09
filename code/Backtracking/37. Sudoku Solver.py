#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 37. Sudoku Solver
# Created by xc 31/03/2017

"""
    数独的解
    安下心来,好好的做题,丢掉那些乱七八糟的东西,静下心来 好好做题
"""

import copy
class Solution(object):
    def __init__(self):
        self.result = False

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        new_board = [[0 for j in range(0, 9)] for i in range(0, 9)]
        for i in range(0, 9):
            for j in range(0, 9):
                new_board[i][j] = board[i][j]

        for i in range(0, 9):
            if self.result:
                break
            for j in range(0, 9):
                if self.result:
                    break
                if new_board[i][j] == '.':
                    for num in range(1, 10):
                        new_board[i][j] = str(num)
                        self.process(new_board, i, j)
                        if self.result:
                            break
                        new_board[i][j] = '.'
        board = copy.deepcopy(new_board)
        print board

    def process(self, new_board, i, j):
        if not self.isLegal(i, j, new_board):
            # 这个位置不合法,返回
            return
        # 判断一下这个数独当前是不是已经结束了
        end = True
        for row in range(0, 9):
            if not end:
                break
            for col in range(0, 9):
                if new_board[row][col] == '.':
                    end = False
                    break
        if end:
            self.result = True
            return

        for i in range(0, 9):
            for j in range(0, 9):
                if new_board[i][j] == '.':
                    for num in range(1, 10):
                        new_board[i][j] = str(num)
                        self.process(new_board, i, j)
                        if self.result:
                            break
                        new_board[i][j] = '.'
                    # 无论如何都找不到
                    if new_board[i][j] == '.':
                        return

    def isLegal(self, i, j, board):
        num = board[i][j]
        for index in range(0, 9):
            if index != i and board[index][j] == num:
                return False
        for index in range(0, 9):
            if index != j and board[i][index] == num:
                return False
        # 所在的小方块
        row = i / 3
        start_row = 3 * row
        col = j / 3
        start_col = 3 * col
        for p in range(start_row, start_row + 3):
            for q in range(start_col, start_col + 3):
                if p != i and j != q and board[p][q] == num:
                    return False
        return True

board1 = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
board1 = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
test = Solution()
test.solveSudoku(board1)
