#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 401. Binary Watch(E)
# Created by xc 16/04/2017
"""
    递归的二进制表盘
"""

class Solution(object):
    def __init__(self):
        self.time_set = []
        self.result = []
        self.binary_list = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num == 0:
            return ["0:00"]
        # 一共十个二进制位置
        for i in range(0, 10):
            self.time_set.append(i)
            self.process(i + 1, num - 1)
            self.time_set.pop()
        return self.result

    def process(self, begin, num):
        # 首先计算当前时间和分钟
        hours = 0
        minute = 0
        for item in self.time_set:
            if item <= 3:
                hours += self.binary_list[item]
            else:
                minute += self.binary_list[item]
        if hours > 11:
            return
        if minute >= 60:
            return

        # 判断是否结束
        if num == 0:
            # 完成一组
            if minute < 10:
                final_time = str(hours) + ':0' + str(minute)
            else:
                final_time = str(hours) + ':' + str(minute)
            self.result.append(final_time)
        if (10 - begin) < num:
            # 点不够了
            return
        for i in range(begin, 10):
            self.time_set.append(i)
            self.process(i + 1, num-1)
            self.time_set.pop()
num = 9
test = Solution()
print test.readBinaryWatch(num)


