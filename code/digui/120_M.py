#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 120_M
# Created by xc 13/03/2017

"""
    递归算法并不能快速的计算出来,而且存在冗余
    而动态规划就是为了解决这个情况而产生的
    递归算法:失败!!!
    其余的样例都过了,只有一个大测试样例没有通过
    42 / 43 test cases passed. Status: Time Limit Exceeded
"""
import copy
class Solution(object):
    def __init__(self):
        self.triangle = []
        self.result = 0

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # 最后的值 设定初始值是最左面的一列值
        for index in range(0, len(triangle)):
            self.result += triangle[index][0]
        # 三角形的层数
        self.triangle = copy.deepcopy(triangle)
        self.process(0, 0, self.triangle[0][0])
        return self.result

    def process(self, current_layer, current_index, sum):
        """
        :param current_layer: 当前的层数 (从0开始)
        :param current_index: 位置
        :param sum: 到这个位置为止的和(已经计算了这个位置的数了)
        :return:
        """
        if current_layer == len(self.triangle)-1:
            # 已经到达了最后一层
            if sum < self.result:
                self.result = sum
            return
        if sum > self.result:
            # 已经大于最短路径了,减枝
            # 错误的,不要减枝,因为万一后面还有负数呢!!要注意有可能后面有负数
            # return
            pass
        self.process(current_layer + 1, current_index, sum + self.triangle[current_layer + 1][current_index])
        self.process(current_layer + 1, current_index + 1,
                     sum + self.triangle[current_layer + 1][current_index + 1])
        return

