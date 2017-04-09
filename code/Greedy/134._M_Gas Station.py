#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 134._M_Gas Station
# Created by xc 29/03/2017
"""
    加油问题 迷迷糊糊的 也不知道怎么就过了,题目不难,但是index确实是晕啊
"""
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # 首先对cost排序
        sort_cost = sorted(enumerate(cost), key=lambda x: x[1])
        cost_index_list = [index for index, value in sorted(enumerate(cost), key=lambda x: x[1])]
        cost_value_list = [value for index, value in sorted(enumerate(cost), key=lambda x: x[1])]

        # 遍历cost 从最小的花销开始
        for index in cost_index_list:
            # index是当前花销最小的,该站作为起点,判断能否成功走一圈
            if self.drive(cost_index_list,index, gas, cost):
                return index
        return -1

    def drive(self, cost_index_list, index, gas, cost):
        """
        :param index: 起始站
        :param gas:
        :param cost:
        :return:
        """
        current_oil = 0
        current_station = index
        for i in range(0, len(gas)):
            if current_station == len(gas):
                current_station = 0
            if current_oil + gas[current_station] - cost[current_station] < 0:
                return False
            else:
                current_oil = current_oil + gas[current_station] - cost[current_station]
                i += 1
                current_station += 1
        return True


gas = [1,2,3]
cost = [1,2,3]
test = Solution()
print test.canCompleteCircuit(gas,cost)