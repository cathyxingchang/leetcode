#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 121_E_(122~123)
# Created by xc 02/03/2017

"""
    思路: 收益问题

"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        max_profit = 0
        # 感觉需要保存,从某个数字开始,后面最大的值,以及最大值的索引 max_list
        #   这里还是需要的,因为下面不管哪种优化情况,都处理不了,[100,99,98,97...0]这种纯逆序的数列
        max_list = []
        for index in range(0, len(prices)):
            max_list.append(0)
        max_list[len(prices) - 1] = prices[len(prices) - 1]
        # 保存已经遍历过的数组的最大值
        tmp_max = prices[len(prices) - 1]
        for index in range(len(prices) - 2, -1, -1):
            if prices[index] > tmp_max:
                tmp_max = prices[index]
            max_list[index] = tmp_max
        # max_list 中保存的是从当前元素开始,后面的最大值
        # 那是不是我遍历一遍,就可以了呢
        for buy_index in range(0, len(prices)):
            profit = max_list[buy_index]-prices[buy_index]
            if profit > max_profit:
                max_profit = profit


        return max_profit
