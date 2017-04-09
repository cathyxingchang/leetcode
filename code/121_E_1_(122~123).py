#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 121_E_(122~123)
# Created by xc 02/03/2017

"""
    思路: 收益问题

    这个优化的思路是好的,但是可以优化的方式是无效的 还是处理不了特殊的情况

    但是我觉得,这个题虽然做的很麻烦 而且还做错了,但是这个思路是很好的!

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
        # 设定一个当前最小的且值最大的开头,后面比他大的数字,就直接筛掉了
        current_min_start = prices[0]
        # 感觉需要保存,从某个数字开始,后面最大的值,以及最大值的索引 max_list
        #   这里还是需要的,因为下面不管哪种优化情况,都处理不了,[100,99,98,97...0]这种纯逆序的数列
        max_list = []
        for index in range(0,len(prices)):
            max_list.append(0)
        max_list[len(prices)-1] = prices[len(prices)-1]
        # 保存已经遍历过的数组的最大值
        tmp_max = prices[len(prices)-1]
        for index in range(len(prices)-2,-1,-1):
            if prices[index] > tmp_max:
                tmp_max = prices[index]
            max_list[index] = tmp_max

        current_max_end = max(prices)
        current_max_index = prices.index(max(prices))
        for buy_index in range(0, len(prices)):
            if prices[buy_index] > current_min_start:
                # 当前的买入价高于之前最小的买入价,则说明一定不是最优
                continue
            if buy_index < current_max_index:
                # 在买入价低于最低买入价的情况下,
                # 再分析当前buy的索引是否大于 current_max_index 如果不大于,则说明售出价在买入价之后,直接更新最大值
                profit = current_max_end - prices[buy_index]
                max_profit = profit
                current_min_start = prices[buy_index]
                continue
            for sale_index in range(buy_index, len(prices)):
                # buy 小,且 最大卖出价的索引在buy之前
                profit = prices[sale_index]-prices[buy_index]
                if profit > max_profit:
                    max_profit = profit
                    current_min_start = prices[buy_index]
                    current_max_end = prices[sale_index]
                    current_max_index = sale_index
        return max_profit
