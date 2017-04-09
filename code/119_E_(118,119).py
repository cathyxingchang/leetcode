#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 119_E_(118,119)
# Created by xc 13/03/2017
"""
    完全和118一样的思路,只是最后把最后一层输出出去
    归纳就算法有点冗余
"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]

        result_list = []
        result_list.append([1])
        result_list.append([1, 1])
        # 每一层生成结果,index是层数
        for index in range(2, rowIndex+1):
            current_list = []
            current_list.append(1)
            for index_list in range(0, len(result_list[index-1])-1):
                number = result_list[index-1][index_list] + result_list[index-1][index_list + 1]
                current_list.append(number)
            current_list.append(1)
            result_list.append(current_list)
        return result_list[-1]
