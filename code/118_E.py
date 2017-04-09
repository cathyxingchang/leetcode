#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 118_E
# Created by xc 13/03/2017

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        result_list = []
        result_list.append([1])
        result_list.append([1, 1])
        # 每一层生成结果,index是层数
        for index in range(2, numRows):
            current_list = []
            current_list.append(1)
            for index_list in range(0, len(result_list[index-1])-1):
                number = result_list[index-1][index_list] + result_list[index-1][index_list + 1]
                current_list.append(number)
            current_list.append(1)
            result_list.append(current_list)
        return result_list
