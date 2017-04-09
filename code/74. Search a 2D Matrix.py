#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 74. Search a 2D Matrix
# Created by xc 30/03/2017
"""
    思路:对先对行,后对列进行二分查找的过程
    复杂度是log(m)+log(n)
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0 :
            return False
        begin_row = 0
        end_row = len(matrix) - 1
        while begin_row <= end_row:
            mid = (begin_row + end_row) / 2
            if target == matrix[mid][0]:
                # 找到了
                return True
            elif target > matrix[mid][0]:
                begin_row = mid + 1
            else:
                end_row = mid - 1
        # 按照二分查找的思路,begin得到的是插入的位置,
        # 也就是begin的位置,是比target数据要大的
        if begin_row == 0:
            # 比最小的哪一行的第一个元素都要小
            return False
        # 下一步获取列坐标 行是begin-1的位置
        find_row = begin_row - 1
        begin_col = 0
        end_col = len(matrix[0]) - 1
        while begin_col <= end_col:
            mid = (begin_col + end_col) / 2
            if target == matrix[find_row][mid]:
                # 找到了
                return True
            elif target > matrix[find_row][mid]:
                begin_col = mid + 1
            else:
                end_col = mid - 1
        return False


test = Solution()
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

matrix = [[]]
print test.searchMatrix(matrix, 51)




