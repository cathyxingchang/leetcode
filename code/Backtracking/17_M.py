#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 17_M
# Created by xc 24/03/2017

import copy
class Solution(object):
    def __init__(self):
        self.result = []
        self.map = {}
        self.map[0] = ""
        self.map[1] = ""
        self.map[2] = "abc"
        self.map[3] = "def"
        self.map[4] = "ghi"
        self.map[5] = "jkl"
        self.map[6] = "mno"
        self.map[7] = "pqrs"
        self.map[8] = "tuv"
        self.map[9] = "wxyz"

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        num_string = list(digits)
        num = int(num_string[0])
        tmp_result = []
        for index in range(0, len(self.map[num])):
            tmp_result.append(self.map[num][index])
            self.process(tmp_result, num_string[1:])
            tmp_result.pop()
        # self.result 拼接
        pinjie = [''.join(self.result[i]) for i in range(0, len(self.result))]
        return pinjie

    def process(self, tmp_result, num_string):
        """
        :param tmp_result:目前的结果
        :param num_string:当前待查询的数字
        :return:
        """
        if len(num_string) == 0:
            self.result.append(copy.deepcopy(tmp_result))
            return
        num = int(num_string[0])
        for index in range(0, len(self.map[num])):
            tmp_result.append(self.map[num][index])
            self.process(tmp_result, num_string[1:])
            tmp_result.pop()
        pass



digits_xing = ""
s = Solution()
print s.letterCombinations(digits_xing)